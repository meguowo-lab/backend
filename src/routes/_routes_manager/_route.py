from typing import Literal, Callable, Any

class RouteBase():

    method: Literal["get", "post", "delete", "put"] = "get"    
    route_func: None | Callable[..., Any]
        