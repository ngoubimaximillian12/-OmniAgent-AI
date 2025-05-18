from fastapi import Request

async def add_user_tag(request: Request, call_next):
    request.state.user_id = request.headers.get("X-User-ID", "default")
    response = await call_next(request)
    return response
