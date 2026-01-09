from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.features.get_buildings import router as buildings_router

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:80",
    "http://localhost:81",
    "http://127.0.0.1",
    "http://127.0.0.1:80",
    "http://127.0.0.1:81",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(buildings_router, prefix="/buildings")


@app.get("/health")
def health():
    return {"status": "ok"}
