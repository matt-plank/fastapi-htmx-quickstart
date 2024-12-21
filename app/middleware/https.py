from fastapi import Request
from fastapi.responses import RedirectResponse


async def middleware(request: Request, call_next):
    protocol = request.headers.get("X-Forwarded-Proto")

    if protocol != "https":
        return RedirectResponse(request.url.replace(scheme="https"))

    return await call_next(request)
