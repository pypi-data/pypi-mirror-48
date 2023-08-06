####
Ubot
####

A *very* minimal class that implements a Telegram bot trigger-response loop plus some endpoint utilities. Can (should) be extended depending on needs.

Why yet another Python Telegram bot framework?
===============================================
| This framework was born from my need to have a simple, easily-maintainable, async-first, server-independent solution to develop Telegram bots. It doesn't attempt to implement the full API, but it offers a handy way to perform requests while leaving the developer free to do what he wants with the response thus not incurring in extra parsing overhead.
| The development is driven by my needs or (eventually) feature requests, a list of what is missing can be found at the bottom of this readme.
| What set this bot apart from the "competition" is:

- method chaining to generate requests, easier on IDEs code completion and more readable than long 10-params functions
- fully async request handling for high responsiveness
- doesn't depend on any other framework to handle the networking side
- simple to understand, easy to maintain
- caches media files ids with barely any effort (and if you backup the cache in a db you can make it persistent)

Quickstart
==========

.. code-block:: python

    import asyncio
    import json

    import uvicorn

    from ubot import Bot, Trigger
    from ubot.endpoints import SendMessage

    loop = asyncio.get_event_loop()
    bot = Bot('token', loop=loop)

    # add a simple trigger
    @bot.trigger
    class CustomTrigger(Trigger):
        async def match(self, update, bot):
            return True

        async def trigger(self, update, bot)
            req = SendMessage(YOUR_USER_ID, 'test').serialize()
            bot.api_request(req)

    # prepare the ASGI class to push updates into the bot
    class App:
        def __init__(self, scope):
            assert scope['type'] == 'http'
            self.scope = scope

        async def __call__(self, receive, send):
            if self.scope['path'] == WEBHOOK_PATH and self.scope['method'] == 'POST':

                body = []
                more_body = True

                while more_body:
                    message = await receive()
                    body.append(message.get('body', b'').decode('utf-8'))
                    more_body = message.get('more_body', False)

                body = ''.join(body)
                body = json.loads(body)
                bot.push_update(body)

            await send({
                'type': 'http.response.start',
                'status': 204,  # noqa: S001
                'headers': [
                    [b'content-type', b'text/plain'],
                ]
            })
            await send({
                'type': 'http.response.body'
            })

    # remoe the loop and http parameters if you're not using PyPy
    server = uvicorn.Server(uvicorn.Config(
        app=App, host='0.0.0.0', port=8080, loop='asyncio', http='h11'))

    # start the server and the bot
    loop.run_until_complete(asyncio.gather[
         bot.start(),
         server.serve(),
         loop=loop
     ])

Resources
=========
- Docs: https://strychnide.github.io/ubot/

**TODO:** documentation, unit tests, support sticker, passport, payments, games
