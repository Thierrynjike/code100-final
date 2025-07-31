import requests as req
import json


def solution(data):
    out = {}
    for elem in data.keys():
        try:
            response = req.get(data[elem]["URL"])
            response.raise_for_status()
            content = response.content.decode()

            if data[elem]["format"] == "csv":
                # Count data rows, excluding header and empty lines
                lines = [line.strip() for line in content.split('\n') if line.strip()]
                out[elem] = max(0, len(lines) - 1)  # Subtract header row
            elif data[elem]["format"] == "json":
                # Parse JSON and count items
                try:
                    json_data = json.loads(content)
                    out[elem] = len(json_data) if isinstance(json_data, list) else 1
                except json.JSONDecodeError:
                    out[elem] = 0
            else:  # HTML format
                # Simple parsing to count data elements
                # This is a basic approach - in production might use BeautifulSoup
                out[elem] = content.count('<')  # Count HTML elements as proxy for data items
        except Exception as e:
            # Handle network errors gracefully
            out[elem] = 0

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
