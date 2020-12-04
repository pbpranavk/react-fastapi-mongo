from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.server.routes.obj import router as SimpleRouter

app = FastAPI()
app.include_router(SimpleRouter, tags=["Simple"], prefix="/simple")

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
