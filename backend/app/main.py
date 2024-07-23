from fastapi import FastAPI
from backend.app.api.router import api_router
from fastapi.middleware.cors import CORSMiddleware
from neomodel import config


app = FastAPI()
config.DATABASE_URL = 'bolt://neo4j:holamundo@localhost:7687'

app.include_router(api_router)

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
