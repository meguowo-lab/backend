from uvicorn import run
from fastapi import FastAPI

from src.env import Env
from src.routes import Parser
from src.routes import RoutesManager

app = FastAPI(title="my backend!")
parser = Parser()
parser.parse()
manager = RoutesManager(app=app, routes=parser.routes)
manager.attach_routes()


if __name__ == "__main__":
    port: int = int(Env.get("PORT"))
    run("main:app", port=port)
