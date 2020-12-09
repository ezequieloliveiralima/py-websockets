In my journey at Python, take a look at this websockets client-server :)

To run:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Choose some example to run:
1. server-client:
    Simplest way to connect websocket, and emmits some message.

2. server-client-ssl:
    Same the above example, but with TLS security layer.
    Follow the instructions to create a certificate:
    https://devcenter.heroku.com/articles/ssl-certificate-self

3. server-webclient:
    Simplest way to connect websocket server and webbrowser, webbrowser only receives current time.

4. server-webclient-counter:
    This example allows webbrowser interact with the server, how many clients you want.

Enjoy, I hope this can help all of you.

Thanks to: https://websockets.readthedocs.io/en/stable/intro.html