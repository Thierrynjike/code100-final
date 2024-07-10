import json


def solution(lbx, upx, lby, upy, max_right, x1, y1, r1, x2, y2, r2, points):
    out = []

    def is_valid(x, y):
        return x >= lbx and x <= max_right and y >= lby and y <= upy

    for p in points:
        x, y = p
        if is_valid(x, y):
            if (lbx <= x <= upx) and (lby <= y <= upy):
                out.append(p)
            elif r1**2 <= (x - x1) ** 2 + (y - y1) ** 2 <= r2**2:
                out.append(p)
            elif r1**2 <= (x - x2) ** 2 + (y - y2) ** 2 <= r2**2:
                out.append(p)

    return len(out)


data = json.load(open("dataset.json", "r"))

width = data["width"]
height = data["height"]
lbx = 145
upx = 165
lby = 75
upy = 225
max_right = 485
x1 = 250
y1 = 150
r1 = 55
x2 = 410
y2 = 150
r2 = 75
points = data["coords"]

print(solution(lbx, upx, lby, upy, max_right, x1, y1, r1, x2, y2, r2, points))
