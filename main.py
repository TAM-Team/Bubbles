import socket
import sys

import uvicorn
from fastapi import FastAPI
from rest_framework import routers

# router = routers.SimpleRouter()
#
# app = FastAPI(docs_url=None,redoc_url=None)
# app.include_router(router, prefix="/v1")
#
# hostname = socket.gethostname()
#
# version = f"{sys.version_info.major}.{sys.version_info.minor}"
#
#
# @app.get("/")
# async def read_root():
#     return {
#         "name": "visualroll",
#         "host": hostname,
#         "version": f"Hello world! From FastAPI running on Uvicorn. Using Python {version}"
#     }

app = FastAPI()

hostname = socket.gethostname()

version = f"{sys.version_info.major}.{sys.version_info.minor}"


@app.get("/")
async def read_root():
    return {
        "name": "my-app",
        "host": hostname,
        "version": f"Hello world! From FastAPI running on Uvicorn. Using Python {version}"
    }