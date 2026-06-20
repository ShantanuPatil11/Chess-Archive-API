from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.services.analytics_service import (
    get_player_stats
)

router = APIRouter()


@router.get("/analytics/{username}")
def analytics(
    username: str,
    db: Session = Depends(get_db)
):
    return get_player_stats(db, username)