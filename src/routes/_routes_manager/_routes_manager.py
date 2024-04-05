from fastapi import FastAPI
from src.proj_types import func

class RoutesManager:

    def __init__(self, app: FastAPI, routes: dict[str, func]):
        self.app = app
        self.routes = routes
    
    def attach(self):
        for path, route in self.routes.items():
            method = self.app.__getattribute__(route.__name__)
            method(path=path)(route)
