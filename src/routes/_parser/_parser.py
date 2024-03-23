import os
from importlib import import_module

from src.routes._routes_manager._route import RouteBase

class Parser:

    def __init__(self, routes_path: str = "src/routes"):
        self.routes: dict[RouteBase, str] = {}
        self.routes_base_path = routes_path
        self.modules_base_path = routes_path.replace("/", ".")

    def parse(self, base_path:str="/"):
        path = os.path.abspath(f"src/routes{base_path}")
        files = os.listdir(path)

        for file in files:

            if file.startswith("_"):
                continue

            file_abs_path = fr"{path}\{file}"

            if os.path.isdir(file_abs_path):
                self.parse(f"{base_path}{file}/")
            
            else:
                module_name = file.replace(".py", "")
                module_path = f"{self.modules_base_path}.{module_name}"
                func = import_module(module_path).Route
                self.routes.update({func: base_path})
