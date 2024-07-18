import requests as req
import pandas as pd


def solution(data):
    acting = 0
    movies = 0
    bands = 0
    out = {}
    for elem in data.keys():
        response = req.get(data[elem]["URL"])

        if data[elem]["format"] == "csv":
            out[elem] = len(response.content.decode().split("\n"))
        elif data[elem]["format"] == "json":
            out[elem] = len(response.content.decode().split("\n"))
        else:
            out[elem] = len(response.content.decode().split("\n"))

    return out


print(
    solution(
        {
            "acting": {
                "format": "csv",
                "URL": "https://puzzles.code100.dev/puzzles/manchester-united/acting.csv",
            },
            "movies": {
                "format": "json",
                "URL": "https://puzzles.code100.dev/puzzles/manchester-united/movies.json",
            },
            "bands": {
                "format": "HTML",
                "URL": "https://puzzles.code100.dev/puzzles/manchester-united/bands.html",
            },
        }
    )
)
