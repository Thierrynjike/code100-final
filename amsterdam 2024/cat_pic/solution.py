from collections import Counter

def solution(data):
    # Use set comprehension for better memory efficiency
    names = {cat["alt"].split(":")[0] for cat in data}
    
    # Use max() instead of sorting for O(n) instead of O(n log n)
    widest = max(cat["width"] for cat in data)
    tallest = max(cat["height"] for cat in data)
    
    # Use Counter for efficient counting
    formats = Counter(cat["filename"].split(".")[-1] for cat in data)

    return {
        "uniquenames": len(names),
        "widest": widest,
        "tallest": tallest,
        "formats": dict(formats),
    }


print(
    solution(
        [
            {
                "width": 200,
                "height": 300,
                "filename": "5klvugfffl.gif",
                "alt": "Whiskers: ginger cat.",
            },
            {
                "width": 800,
                "height": 600,
                "filename": "fpocczf87fl.jpg",
                "alt": "Bootsy: grey cat.",
            },
            {
                "width": 400,
                "height": 900,
                "filename": "5pocczf87fl.jpg",
                "alt": "Whiskers: white cat.",
            },
            {
                "width": 200,
                "height": 300,
                "filename": "5k9kof87fl.webp",
                "alt": "Mortimer: tabby cat.",
            },
        ]
    )
)
