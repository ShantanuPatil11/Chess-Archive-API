from sqlalchemy.orm import Session
from app.models import Game


def get_player_stats(db: Session, username: str):

    username = username.lower()

    games = db.query(Game).all()

    player_games = []

    for game in games:

        white = game.white_username.lower()
        black = game.black_username.lower()

        if white == username or black == username:
            player_games.append(game)

    total_games = len(player_games)

    long_games = len(
        [g for g in player_games if g.moves_count >= 40]
    )

    avg_moves = round(
        sum(g.moves_count for g in player_games) / total_games,
        2
    ) if total_games else 0

    highest_rating_faced = 0

    for game in player_games:

        if game.white_username.lower() == username:
            highest_rating_faced = max(
                highest_rating_faced,
                game.black_rating
            )

        else:
            highest_rating_faced = max(
                highest_rating_faced,
                game.white_rating
            )

    return {
        "username": username,
        "total_games": total_games,
        "long_games": long_games,
        "average_moves": avg_moves,
        "highest_rating_faced": highest_rating_faced
    }