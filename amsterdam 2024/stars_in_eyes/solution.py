import math


def solution(data):

    out = int(
        sum(
            [
                (elem["width"] * elem["height"])
                - math.pi * elem["width"] * elem["height"] / 4
                for elem in data
            ]
        )
    )

    return out


print(
    solution(
        [
            {"width": 200, "height": 300},
            {"width": 200, "height": 150},
            {"width": 100, "height": 100},
        ]
    )
)
