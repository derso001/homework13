import uvicorn
import redis.asyncio as redis

from fastapi import FastAPI
from fastapi_limiter import FastAPILimiter
from src.routers.contacts import router as contact_rout
from src.routers.auth import router as auth_rout

import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.include_router(contact_rout)
app.include_router(auth_rout)

@app.on_event("startup")
async def startup():
    r = await redis.Redis(host=os.getenv('REDIS_HOST'), port=os.getenv('REDIS_PORT'), db=0, encoding="utf-8",
                          decode_responses=True)
    await FastAPILimiter.init(r)

if __name__ == "__main__":
    uvicorn.run(
        "main:app", host="0.0.0.0", port=8000,
    )