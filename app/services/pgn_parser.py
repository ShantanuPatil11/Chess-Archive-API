import re


def count_moves(pgn: str) -> int:
    moves = re.findall(r"\d+\.", pgn)
    return len(moves)