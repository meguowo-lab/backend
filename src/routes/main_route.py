from src.routes import RouteBase

class Route(RouteBase):
    method = "get"

    @staticmethod
    async def route() -> str:
        return "hello here! this is main page!"
    
    route_func = route
