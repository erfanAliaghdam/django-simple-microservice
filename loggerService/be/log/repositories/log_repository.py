from log.models import Log


class LogRepository:
    

    def create_log(
        self,
        user_id,
        request_time,
        user_ip,
        user_device,
    ):
        log = Log.objects.create(
            user_device=user_device,
            user_ip=user_ip,
            user_id=user_id,
            request_time=request_time
        )
        return log
