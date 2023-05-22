from fastapi import FastAPI, Request
from rasa.core.agent import Agent
from rasa.core.interpreter import RasaNLUInterpreter
from rasa.core.utils import EndpointConfig
from rasa.model import get_model
import asyncio
from fastapi import FastAPI, Form
import uvicorn

model_path = r"models\nlu"
interpreter = RasaNLUInterpreter(model_path)
model_directory = get_model(r"models")
endpoint = EndpointConfig(url="http://localhost:5055/webhook")
agent = Agent.load(model_directory, interpreter=interpreter,
                   action_endpoint=endpoint)


app = FastAPI()


@app.post("/message")
def chatbot_handler(user_text: str = Form(...)):
    loop = asyncio.new_event_loop()
    response = loop.run_until_complete(agent.handle_text(user_text))
    return {"response": response[0]['text']}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=84)
