def solution(word):
    out = 0
    num = ""
    state = 1
    for c in word:
        if c.isnumeric() and state == 1:
            state = 0
            num += c
        elif c.isnumeric() and state == 0:
            num += c
        elif (num != "") and (not c.isnumeric()):
            out += int(num)
            state = 0
            num = ""

    if num != "":
        out += int(num)
    return out


print(
    solution(
        "P9jktv501L3x37245XbA7RQD213K8EiU672ZmWgY8OcN09FhSfBzVnGdIyHlMqCw6Xo248Rj3Ts5491Uh47Em7Pw5k1Qn8Lg3Ft9Yz0Kp8Bv2Nq7Ic4Dx6Jm3Gy1Ha4Ws2Vb5Lu9Or6Tn3Xm4Zg1Nh8Qw5Lr0Fe7Ks3Zx2Hb6Vn8Mj7Oa4Gp5Yn9Xq2Bv7Jc4Hx6Dm1Fg4It3Vy5Ws2Qp8Lu3Nn0Or8En3Km4Jg1Hb7Yv5Xs9Kp6Tn3Xm4Zg1Nh8Qw5Lr0Fe7Ks3Zx2Hb6Vn8Mj7Oa4Gp5Yn9Xq2Bv7Jc4Hx6Dm1Fg4It3Vy5Ws2Qp8Lu3Nn0Or8En3Km4Jg1Hb7Yv5Xs9Kp6Tn3Xm4Zg1Nh8Qw5Lr0Fe7Ks3Zx2Hb6Vn8Mj7Oa4Gp5Yn9Xq2Bv7Jc4Hx6Dm1Fg4It3Vy5Ws2Qp8Lu3Nn0Or8En3Km4Jg1Hb7Yv5Xs9Kp6Tn3Xm4Zg1Nh8Qw5Lr0Fe7Ks3Zx2Hb6Vn8Mj7Oa4Gp5Yn9Xq2Bv7Jc4Hx6Dm1Fg4It3Vy5Ws2Qp8Lu3Nn0Or8En3Km4Jg1Hb7Yv5Xs9Kp6Tn3Xm4Zg1Nh8Qw5Lr0Fe7Ks3Zx2Hb6Vn8Mj7Oa4Gp5Yn9Xq2Bv7Jc4Hx6Dm1Fg4It3Vy5Ws2Qp8Lu3Nn0Or8En3Km4Jg1Hb7Yv5Xs9Kp6Tn3Xm4Zg1Nh8Qw5Lr0Fe7Ks3Zx2Hb6Vn8Mj7Oa4Gp5Yn9Xq2Bv7Jc4Hx6Dm1Fg4It3Vy5Ws2Qp8Lu3Nn0Or8En3Km4Jg1Hb7Yv5Xs9Kp6Tn3Xm4Zg1Nh8Qw5Lr0Fe7Ks3Zx2Hb6Vn8Mj7Oa4Gp5Yn9X"
    )
)
