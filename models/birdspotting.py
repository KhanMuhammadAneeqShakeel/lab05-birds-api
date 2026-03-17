from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field


class BirdSpottingBase(SQLModel):
    bird_id: int
    spotted_at: datetime
    location: str
    observer_name: str
    notes: Optional[str] = None


class BirdSpotting(BirdSpottingBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class BirdSpottingCreate(BirdSpottingBase):
    pass