import time

from starlette.middleware.base import BaseHTTPMiddleware

class LoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(
        self,
        request,
        call_next
    ):

        start_time = time.time()

        response = await call_next(request)

        process_time = time.time() - start_time

        print(
            f"""
            METHOD: {request.method}
            URL: {request.url}
            STATUS: {response.status_code}
            TIME: {process_time}
            """
        )

        return response