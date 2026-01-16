from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.features.get_buildings import router as get_buildings_router
from app.features.add_buildings import router as add_buildings_router

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:80",
    "http://127.0.0.1",
    "http://127.0.0.1:80",
    "http://tba4250s02.it.ntnu.no"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(get_buildings_router, prefix="/buildings")
app.include_router(add_buildings_router, prefix="/buildings")


@app.get("/health")
def health():
    return {"status": "ok"}
