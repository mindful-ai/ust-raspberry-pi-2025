def responder():
    received = yield "ready"
    while True:
        response = f"Received: {received}"
        received = yield response


gen = responder()
print(next(gen))          # 'ready'
print(gen.send("ping"))   # 'Received: ping'
print(gen.send("pong"))   # 'Received: pong'
