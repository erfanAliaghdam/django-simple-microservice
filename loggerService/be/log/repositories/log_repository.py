from log.models import Log


class LogRepository:
    def create_log(
        self,
        user_id: int | str,
        request_time: str,
        user_ip: str,
        user_device: str,
    ) -> Log:
        log = Log.objects.create(
            user_device=user_device,
            user_ip=user_ip,
            user_id=user_id,
            request_time=request_time,
        )
        return log

    def check_if_new_device_has_logged_in_by_user_id(
        self, user_id: int | str, new_user_device: str
    ) -> bool:
        return Log.objects.filter(user_id=user_id).last().user_device != new_user_device
