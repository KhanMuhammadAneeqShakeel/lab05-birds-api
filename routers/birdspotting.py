from fastapi import APIRouter, Depends
from sqlmodel import Session
from database import get_session
from models.birdspotting import BirdSpotting, BirdSpottingCreate
from repositories import birdspotting as repo

router = APIRouter(prefix="/birdspotting", tags=["BirdSpotting"])


@router.get("/")
def get_all(session: Session = Depends(get_session)):
    return repo.get_all(session)


@router.get("/{spotting_id}")
def get_one(spotting_id: int, session: Session = Depends(get_session)):
    return repo.get_one(session, spotting_id)


@router.post("/")
def create(data: BirdSpottingCreate, session: Session = Depends(get_session)):
    spotting = BirdSpotting.from_orm(data)
    return repo.insert(session, spotting)