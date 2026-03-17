from sqlmodel import Session, select
from models.birdspotting import BirdSpotting


def get_all(session: Session):
    return session.exec(select(BirdSpotting)).all()


def get_one(session: Session, spotting_id: int):
    return session.get(BirdSpotting, spotting_id)


def insert(session: Session, spotting: BirdSpotting):
    session.add(spotting)
    session.commit()
    session.refresh(spotting)
    return spotting