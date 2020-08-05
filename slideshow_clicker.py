from starlette.applications import Starlette
from starlette.endpoints import WebSocketEndpoint
from starlette.routing import Route, WebSocketRoute
from starlette.websockets import WebSocketDisconnect
from starlette.responses import Response
from os import system, environ


async def main_page(request):
    with open("main.html") as f:
        main_page_html = f.read()

    return Response(main_page_html, media_type="text/html")


async def press_ws(websocket):
    await websocket.accept()

    try:
        while True:
            data = await websocket.receive_bytes()
            if len(data) and data[0]:
                system("xdotool keydown space")
            else:
                system("xdotool keyup space")
    except WebSocketDisconnect:
        pass

    await websocket.close()


app = Starlette(routes=[Route("/", main_page), WebSocketRoute("/press", press_ws)])

if __name__ == "__main__":
    import uvicorn

    try:
        port = int(environ.get("PORT", "8000"))
        uvicorn.run(app=app, host="0.0.0.0", port=port)
    except ValueError:
        print("Invalid value for PORT!")
