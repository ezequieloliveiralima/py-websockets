import asyncio
import pathlib
import ssl
import websockets

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)

cert_pem = pathlib.Path(__file__).with_name('server.crt')

ssl_context.load_verify_locations(cert_pem)

async def hello():
    uri = 'wss://localhost:8765'
    async with websockets.connect(uri, ssl=ssl_context) as websocket:
        name = input('What\'s yout name? ')

        await websocket.send(name)
        print(f'> {name}')

        greeting = await websocket.recv()
        print(f'< {greeting}')


asyncio.get_event_loop().run_until_complete(hello())