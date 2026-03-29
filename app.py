from fastapi import FastAPI, Body
from env.environment import CustomerSupportEnv
from env.models import Action

app = FastAPI()
env = CustomerSupportEnv()

@app.post("/reset")
def reset(dummy: dict = Body(default={})):
    obs = env.reset()
    return {
        "observation": obs.model_dump()
    }

@app.post("/step")
def step(action: Action):
    obs, reward, done, info = env.step(action)

    return {
        "observation": obs.model_dump(),
        "reward": float(reward),
        "done": bool(done),
        "info": info
    }
