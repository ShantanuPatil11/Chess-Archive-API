from sqlalchemy import Column, Integer, String, Text
from .database import Base


class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)

    game_url = Column(String, unique=True)

    date = Column(String)

    white_username = Column(String)
    white_rating = Column(Integer)

    black_username = Column(String)
    black_rating = Column(Integer)

    result = Column(String)

    opening = Column(String)

    moves_count = Column(Integer)

    time_control = Column(String)

    pgn = Column(Text)