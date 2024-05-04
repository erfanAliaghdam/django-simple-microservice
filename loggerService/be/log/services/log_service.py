from log.repositories import LogRepository
from log.models import Log
from app.producer import publish
import json


class LogService:
    def __init__(self) -> None:
        self.log_repository = LogRepository()

    def create_log(
        self,
        user_id: str,
        user_ip: str,
        request_time: str,
        user_device: str,
        user_email: str,
    ) -> Log:
        # check if new device logged in
        if self.log_repository.check_if_new_device_has_logged_in_by_user_id(
            user_id=user_id, new_user_device=user_device
        ):
            print("neew device logged in .")
            data = {
                "user_id": user_id,
                "user_email": user_email,
                "user_device": user_device,
                "request_time": request_time,
            }
            publish("user_new_device_login", json.dumps(data), "mail")
        log = self.log_repository.create_log(
            user_id=user_id,
            user_ip=user_ip,
            request_time=request_time,
            user_device=user_device,
        )
        return log
