from uvicorn import run
from fastapi import FastAPI

app = FastAPI(title="my backend!")


if __name__ == "__main__":
    run("main:app", port=3000)
