import asyncio
import aiohttp
from aiohttp import web
import json
import ssl
import telepot

TOKEN = '' # your bot token here
API_URL = 'https://api.telegram.org/bot%s/sendMessage' % TOKEN
WEBHOOK_HOST = ''
WEBHOOK_PORT = 8443
WEBHOOK_LISTEN = '0.0.0.0'  # In some VPS you may need to put here the IP addr
WEBHOOK_URL_BASE = "https://{}:{}".format(WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/{}/".format(TOKEN)
WEBHOOK_SSL_CERT = './key.crt'  # Path to the ssl certificate
WEBHOOK_SSL_PRIV = './dom.key'


async def handler(request):
    data = await request.json()

    print('test1')

    headers = {
        'Content-Type': 'application/json'
    }
    message = {
        'chat_id': data['message']['chat']['id'],
        'text': data['message']['text']
    }
    async with aiohttp.ClientSession(loop=loop) as session:
        print('test2')
        async with session.post(API_URL,
                                data=json.dumps(message),
                                headers=headers) as resp:
            try:
                print('success')
                assert resp.status == 200
            except:
                print('fail')
                return web.Response(status=500)
    return web.Response(status=200)


def hello(request):
    return web.Response(status=200, body="Hello world!")


async def init_app(loop):
    app = web.Application(loop=loop, middlewares=[])
    app.router.add_post('/api/v1', handler)
    app.router.add_get('/hello', hello)
    return app

if __name__ == '__main__':
    bot = telepot.Bot(TOKEN)
    bot.deleteWebhook()
    # Set webhook
    bot.setWebhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH,
                 certificate=open(WEBHOOK_SSL_CERT, 'r'))

    loop = asyncio.get_event_loop()
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain(WEBHOOK_SSL_CERT, WEBHOOK_SSL_PRIV)
    try:
        app = loop.run_until_complete(init_app(loop))
        web.run_app(app, port=80, ssl_context=context)
    except Exception as e:
        print('Error create server: %r' % e)
    finally:
        pass
    loop.close()
