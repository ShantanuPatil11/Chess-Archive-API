from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Game

from app.services.chesscom_service import (
    get_archives,
    get_games_from_archive
)

from app.services.pgn_parser import count_moves

router = APIRouter()


@router.post("/import/{username}")
def import_games(username: str, db: Session = Depends(get_db)):

    archives = get_archives(username)

    archive_urls = archives.get("archives", [])

    archive_urls.reverse()

    imported = 0

    for archive_url in archive_urls:

        games_data = get_games_from_archive(archive_url)

        games = games_data.get("games", [])

        games.reverse()

        for game in games:

            if imported >= 100:
                break

            existing = db.query(Game).filter(
                Game.game_url == game["url"]
            ).first()

            if existing:
                continue

            pgn = game.get("pgn", "")

            db_game = Game(
                game_url=game.get("url"),
                date=game.get("end_time"),

                white_username=game["white"]["username"],
                white_rating=game["white"]["rating"],

                black_username=game["black"]["username"],
                black_rating=game["black"]["rating"],

                result=game["white"]["result"],

                opening="Unknown",

                moves_count=count_moves(pgn),

                time_control=game.get("time_control"),

                pgn=pgn
            )

            db.add(db_game)

            imported += 1

        if imported >= 100:
            break

    db.commit()

    return {
        "username": username,
        "imported_games": imported
    }