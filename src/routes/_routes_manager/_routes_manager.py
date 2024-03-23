from fastapi import FastAPI

from src.routes._routes_manager._route import RouteBase

class RoutesManager:

    def __init__(self, app:FastAPI, routes: dict[RouteBase, str]):
        self.app = app
        self.routes = routes
    
    def attach_routes(self):
        for route, path in self.routes.items():
            method = self.app.__getattribute__(route.method)
            method(path=path)(route.route_func)
