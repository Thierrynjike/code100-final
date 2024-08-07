def solution(ships):

    ship_dico = {}

    for ship in ships:
        if ship["ship"] in ship_dico.keys():
            ship_dico[ship["ship"]] += 1
        else:
            ship_dico[ship["ship"]] = 1

    out = [{"name": k, "crewcount": v} for k, v in ship_dico.items()]
    return out


print(
    solution(
        [
            {
                "name": "Philip J. Fry",
                "ship": "Planet Express Ship",
                "job": "Delivery Boy",
                "age": 25,
            },
            {
                "name": "Luke Skywalker",
                "ship": "Millennium Falcon",
                "job": "Jedi",
                "age": -1,
            },
            {
                "name": "Marvin",
                "ship": "Heart of Gold",
                "job": "Paranoid Android",
                "age": 30,
            },
            {
                "name": "Pavel Chekov",
                "ship": "USS Enterprise NCC-1701",
                "job": "Navigator",
                "age": 22,
            },
            {
                "name": "Doctor John A. Zoidberg",
                "ship": "Planet Express Ship",
                "job": "Doctor",
                "age": 86,
            },
            {"name": "Kaylee Frye", "ship": "Serenity", "job": "Mechanic", "age": 23},
            {"name": "Simon Tam", "ship": "Serenity", "job": "Doctor", "age": 28},
        ]
    )
)
