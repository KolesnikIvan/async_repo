"""simplest wsgi app"""
# def application(env, start_response):
#     start_response("200 OK", [("Content-Type", "text/html")])
#     return [b"WSGI hello world"
#             ]

async def application(scope, receive, send):
    await send({
        "type": "http.response.start",
        "status": 200,
        "headers": [[b"content-type", b"text/html"]]
    })
    await send({"type": "http.response.body", "body": b"ASGI hello!"})
