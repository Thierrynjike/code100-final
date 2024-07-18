def solution(data):

    names = set([cat["alt"].split(":")[0] for cat in data])
    widths = sorted([cat["width"] for cat in data])
    heigths = sorted([cat["height"] for cat in data])
    formats = {}

    for cat in data:
        ext = cat["filename"].split(".")[-1]
        if ext in formats:
            formats[ext] += 1
        else:
            formats[ext] = 1

    return {
        "uniquenames": len(names),
        "widest": widths[-1],
        "tallest": heigths[-1],
        "formats": formats,
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
