from fastapi import FastAPI
from routes.users import user


app = FastAPI(
    title="FastAPI & Postgresql",
    description="A REST API using FastAPI(Python) and Postgresql",
    version="0.0.1",
    openapi_tags=[{
        "name": "users",
        "description": "users endpoints"
    }]
)

app.include_router(user)
