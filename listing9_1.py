from datetime import datetime
from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response

router = web.RouteTableDef()

@router.get("/time")
async def time(request: Request) -> Response:
    today = datetime.today()
    result = {
        "month": today.month,
        "day": today.day,
        "time": str(today.time()),
        "req.hdrs": str(request.headers)
    }

    return web.json_response(result)

app = web.Application()
app.add_routes(router)
web.run_app(app)
