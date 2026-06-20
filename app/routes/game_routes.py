from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Game

router = APIRouter()


@router.get("/games")
def get_games(db: Session = Depends(get_db)):

    games = db.query(Game).all()

    return [
        {
            "id": g.id,
            "date": g.date,
            "white_username": g.white_username,
            "white_rating": g.white_rating,
            "black_username": g.black_username,
            "black_rating": g.black_rating,
            "moves_count": g.moves_count,
            "time_control": g.time_control
        }
        for g in games
    ]


@router.get("/games/long")
def get_long_games(db: Session = Depends(get_db)):

    games = db.query(Game).filter(
        Game.moves_count >= 40
    ).all()

    return [
        {
            "id": g.id,
            "white_username": g.white_username,
            "black_username": g.black_username,
            "moves_count": g.moves_count
        }
        for g in games
    ]


@router.get("/games/upsets")
def get_upsets(db: Session = Depends(get_db)):

    games = db.query(Game).all()

    upsets = []

    for g in games:

        # Lower-rated White beats higher-rated Black
        if (
            g.white_rating < g.black_rating and
            g.result == "win"
        ):
            upsets.append({
                "winner": g.white_username,
                "winner_rating": g.white_rating,
                "loser_rating": g.black_rating,
                "difference": g.black_rating - g.white_rating
            })

        # Lower-rated Black beats higher-rated White
        elif (
            g.black_rating < g.white_rating and
            g.result != "win"
        ):
            upsets.append({
                "winner": g.black_username,
                "winner_rating": g.black_rating,
                "loser_rating": g.white_rating,
                "difference": g.white_rating - g.black_rating
            })

    return sorted(
        upsets,
        key=lambda x: x["difference"],
        reverse=True
    )


@router.get("/game/{game_id}/pgn")
def get_pgn(game_id: int, db: Session = Depends(get_db)):

    game = db.query(Game).filter(
        Game.id == game_id
    ).first()

    if not game:
        return {"error": "Game not found"}

    return {
        "id": game.id,
        "pgn": game.pgn
    }