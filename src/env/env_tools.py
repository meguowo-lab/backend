import os

class Env:
    @staticmethod
    def get(name: str) -> str:
        var = os.environ.get(name)
        if var is None:
            raise KeyError(f"var {name} doesnt exists in .env")
        return var
