def solution(dico):
    out = []
    lists = dico["linkedList"]
    top = dico["top"]

    current = [elem for elem in lists if elem["id"] == top][0]
    out.append(current["value"])
    lists.remove(current)

    current_id = current["id"]
    current_next = current["next"]

    while len(lists) > 1:
        current = [elem for elem in lists if elem["id"] == current_next][0]
        current_next = current["next"]
        current_id = current["id"]
        out.append(current["value"])
        lists.remove(current)

    if lists != []:
        out.append(lists[0]["value"])

    return out


print(
    solution(
        {
            "linkedList": [
                {"id": "b", "value": 2, "next": "c"},
                {"id": "c", "value": 3, "next": None},
                {"id": "a", "value": 1, "next": "b"},
            ],
            "top": "a",
        }
    )
)
