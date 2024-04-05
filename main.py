from uvicorn import run
from fastapi import FastAPI

from src.env import Env
from src.routes import Parser
from src.routes import RoutesManager


app = FastAPI(title="my backend!")

parser = Parser()
routes = parser.parse()
print(routes)

manager = RoutesManager(app=app, routes=routes)
manager.attach()


if __name__ == "__main__":
    port: int = int(Env.get("PORT"))
    run(app=app, port=port)
