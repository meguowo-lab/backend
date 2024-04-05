from datetime import datetime, timezone


class BaseException(Exception):
    
    def __init__(self, msg: str) -> None:

        cur_time = datetime.now(timezone.utc).strftime("%d-%m-%Y, %H:%M:%S")
        log_msg = f"{cur_time}: {msg}"
        
        super().__init__(log_msg)
