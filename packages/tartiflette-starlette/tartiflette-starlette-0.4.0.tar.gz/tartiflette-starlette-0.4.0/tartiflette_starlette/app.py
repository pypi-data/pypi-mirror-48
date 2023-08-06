import typing

from starlette.routing import Lifespan, Route, Router
from starlette.types import Receive, Scope, Send
from tartiflette import Engine

from .datastructures import GraphiQL, GraphQLRequestState
from .endpoints import GraphiQLEndpoint, GraphQLEndpoint
from .middleware import GraphQLMiddleware


class TartifletteApp:
    def __init__(
        self,
        *,
        engine: Engine = None,
        sdl: str = None,
        graphiql: typing.Union[bool, GraphiQL] = True,
        path: str = "/",
        schema_name: str = "default",
    ):
        if engine is None:
            assert sdl, "`sdl` expected if `engine` not given"
            engine = Engine(sdl=sdl, schema_name=schema_name)

        assert engine, "`engine` expected if `sdl` not given"

        self.engine = engine

        if graphiql is True:
            graphiql = GraphiQL()

        routes = []

        if graphiql and graphiql.path is not None:
            routes.append(Route(path=graphiql.path, endpoint=GraphiQLEndpoint))

        graphql_route = Route(path=path, endpoint=GraphQLEndpoint)
        routes.append(graphql_route)

        self.app = GraphQLMiddleware(
            Router(routes=routes),
            state=GraphQLRequestState(
                engine=self.engine,
                graphiql=graphiql,
                graphql_endpoint_path=graphql_route.path,
            ),
        )
        self.lifespan = Lifespan(on_startup=self.startup)
        self._started_up = False

    async def startup(self):
        await self.engine.cook()
        self._started_up = True

    async def __call__(self, scope: Scope, receive: Receive, send: Send):
        if scope["type"] == "lifespan":
            await self.lifespan(scope, receive, send)
        else:
            if not self._started_up:
                raise RuntimeError(
                    "GraphQL engine is not ready.\n\n"
                    "HINT: you must register the startup event handler on the "
                    "parent ASGI application.\n"
                    "Starlette example:\n\n"
                    "   app.mount('/graphql', graphql)\n"
                    "   app.add_event_handler('startup', graphql.startup)"
                )
            await self.app(scope, receive, send)
