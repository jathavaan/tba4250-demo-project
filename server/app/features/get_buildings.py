from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.common.deps import get_session

router = APIRouter()


@router.get("/")
def get_buildings(session: Session = Depends(get_session)):
    pass
