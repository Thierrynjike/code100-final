def solution(liste):

    list_dico = {elem: sorted(elem) for elem in liste}
    values = list(list_dico.values())
    out = []
    for k, v in list_dico.items():
        if k not in out and values.count(v) > 1:
            out.append(k)

    return sorted(out)


print(solution(["kiwi", "melon", "apple", "lemon"]))
