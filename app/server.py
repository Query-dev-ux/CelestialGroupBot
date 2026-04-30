from aiohttp import web


async def handle_ping(request: web.Request) -> web.Response:
    return web.Response(text="OK")


async def start_server(host: str = "0.0.0.0", port: int = 8080) -> web.AppRunner:
    app = web.Application()
    app.router.add_get("/ping", handle_ping)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, host, port)
    await site.start()
    return runner
