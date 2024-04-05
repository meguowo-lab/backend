import os
from importlib import import_module

from src.proj_types import func


class Parser:

    def __init__(self, root: str = "src/routes"):
        self.routes_root = root
        self.modules_root = root.replace("/", ".")

    def parse(self, base_path:str="/") -> dict[str, func]:
        routes: dict[str, func] = {}

        abs_path = os.path.abspath(f"{self.routes_root}{base_path}")
        files = os.listdir(abs_path)

        for file in files:

            if file.startswith("_"):
                continue

            file_abs_path = fr"{abs_path}\{file}"

            if os.path.isdir(file_abs_path):
                routes.update(self.parse(f"{base_path}{file}/"))
            
            else:
                module_name = file.replace(".py", "")
                module_base_path = base_path.replace("/", ".")
                module_path = f"{self.modules_root}{module_base_path}{module_name}"
                module = import_module(module_path)
                route_method = [func for func in dir(module) if func in ["get", "post", "delete", "put"]]
                route = module.__getattribute__(route_method[0])
                routes.update({f"{base_path}{module_name}": route})
        
        return routes
