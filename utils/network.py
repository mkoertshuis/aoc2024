import requests
from bs4 import BeautifulSoup
from http.cookiejar import MozillaCookieJar
from pathlib import Path

ROOT = Path(__file__).parent.parent

# Load cookies for authentication
cookies = MozillaCookieJar()
try:
    cookies.load(ROOT / "cookies.txt", ignore_discard=True, ignore_expires=True)
except FileNotFoundError:
    print(
        "There is no cookies file.\nPlease add your AoC \
            cookies.txt file to the root directory."
    )
    raise

# Create the session with the cookies
s = requests.Session()
s.cookies.update(cookies)


def get_input(day: int = 1, year: int = 2024) -> str:
    """Get the input"""
    r = s.get(f"https://adventofcode.com/{year}/day/{day}/input")
    return r.text


def post_answer(answer, day: int = 1, level: int = 1, year: int = 2024) -> str:
    """Post the answer to a question using the cookies"""
    url = f"https://adventofcode.com/{year}/day/{day}/answer"

    data = {"level": level, "answer": str(answer)}

    r = s.post(url, data=data)

    soup = BeautifulSoup(r.text, "html.parser")
    # As of 2023 there is only a single paragraph here
    return soup.find("p").get_text()
