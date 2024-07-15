import faust

app = faust.App(
    'hello_world',
    broker='kafka://localhost:9092',
    # Be explicit about using in-memory Table storage
    store='memory://',
    value_serializer='raw',
)

greetings_topic = app.topic('greetings')

@app.agent(greetings_topic)
async def greet(greetings):
    async for greeting in greetings:
        print(greeting)
