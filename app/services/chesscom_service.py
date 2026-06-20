import requests

BASE_URL = "https://api.chess.com/pub/player"


def get_archives(username):

    url = f"{BASE_URL}/{username}/games/archives"

    response = requests.get(
        url,
        headers={"User-Agent": "ChessArchiveAPI"}
    )

    print("\n========== DEBUG ==========")
    print("URL:", url)
    print("STATUS:", response.status_code)
    print("RESPONSE:")
    print(response.text[:500])
    print("===========================\n")

    return response.json()


def get_games_from_archive(archive_url):

    response = requests.get(
        archive_url,
        headers={"User-Agent": "ChessArchiveAPI"}
    )

    return response.json()