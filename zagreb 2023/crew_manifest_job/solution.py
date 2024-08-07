def solution(ships):

    jobs = list(
        set(
            [
                ship["job"]
                for ship in ships
                if "job" in ship.keys()
                and "age" in ship.keys()
                and ship["age"].isnumeric()
                and int(ship["age"]) > 25
            ]
        )
    )
    return sorted(jobs)


print(
    solution(
        [
            {
                "name": "Malcolm Reynolds",
                "ship": "Serenity",
                "job": "Captain",
                "age": "n/a",
            },
            {
                "name": "Philip J. Fry",
                "ship": "Planet Express Ship",
                "job": "Delivery Boy",
                "age": "25",
            },
            {
                "name": "Geordi La Forge",
                "ship": "USS Enterprise NCC-1701-D",
                "job": "Chief Engineer",
                "age": "n/a",
            },
            {
                "name": "Derrial Book",
                "ship": "Serenity",
                "job": "Shepherd",
                "age": "210",
            },
            {
                "name": "Jayne Cobb",
                "ship": "Serenity",
                "job": "Public Relations",
                "age": "n/a",
            },
            {"name": "Parker", "ship": "Nostromo", "age": "35"},
            {"name": "Janek", "ship": "Prometheus", "job": "Captain", "age": "42"},
            {
                "name": "Professor Hubert J. Farnsworth",
                "ship": "Planet Express Ship",
                "job": "Owner",
                "age": "190",
            },
            {"name": "Kaylee Frye", "ship": "Serenity", "job": "Mechanic", "age": "23"},
            {"name": "Brett", "ship": "Nostromo", "job": "Engineer", "age": "n/a"},
            {"name": "Holly", "ship": "Red Dwarf", "job": "Computer", "age": "n/a"},
            {"name": "Bortus", "ship": "Orville", "job": "Second Officer", "age": "39"},
            {
                "name": "R2-D2",
                "ship": "Millennium Falcon",
                "job": "Astromech Droid",
                "age": "n/a",
            },
            {
                "name": "Zaphod Beeblebrox",
                "ship": "Heart of Gold",
                "job": "President of the Galaxy",
                "age": "n/a",
            },
            {
                "name": "Hikaru Sulu",
                "ship": "USS Enterprise NCC-1701",
                "job": "Helmsman",
                "age": "n/a",
            },
            {
                "name": "James Tiberius Kirk",
                "ship": "USS Enterprise NCC-1701",
                "job": "Captain",
                "age": "30",
            },
            {"name": "Ravel", "ship": "Prometheus", "job": "Medic", "age": "n/a"},
            {
                "name": "Leonard McCoy",
                "ship": "USS Enterprise NCC-1701",
                "job": "Doctor",
                "age": "n/a",
            },
            {
                "name": "Gordon Malloy",
                "ship": "Orville",
                "job": "Helmsman",
                "age": "31",
            },
            {"name": "River Tam", "ship": "Serenity", "age": "17"},
            {
                "name": "Deanna Troi",
                "ship": "USS Enterprise NCC-1701-D",
                "job": "Counselor",
                "age": "30",
            },
            {
                "name": "Wesley Crusher",
                "ship": "USS Enterprise NCC-1701-D",
                "job": "Ensign",
                "age": "16",
            },
            {"name": "Chance", "ship": "Prometheus", "job": "Mechanic", "age": "32"},
            {"name": "Dallas", "ship": "Nostromo", "job": "Captain", "age": "39"},
            {
                "name": "Meredith Vickers",
                "ship": "Prometheus",
                "job": "Executive Officer",
                "age": "n/a",
            },
            {
                "name": "Jean-Luc Picard",
                "ship": "USS Enterprise NCC-1701-D",
                "job": "Captain",
                "age": "n/a",
            },
            {
                "name": "Elizabeth Shaw",
                "ship": "Prometheus",
                "job": "Archaeologist",
                "age": "n/a",
            },
            {"name": "Yaphit", "ship": "Orville", "job": "Engineer", "age": "168"},
            {"name": "Jonesy", "ship": "Nostromo", "job": "Cat", "age": "10"},
            {
                "name": "William Riker",
                "ship": "USS Enterprise NCC-1701-D",
                "job": "First Officer",
                "age": "n/a",
            },
            {
                "name": "Arthur Dent",
                "ship": "Heart of Gold",
                "job": "Sandwich Maker",
                "age": "n/a",
            },
            {
                "name": "Doctor John A. Zoidberg",
                "ship": "Planet Express Ship",
                "job": "Doctor",
                "age": "86",
            },
            {"name": "Cat", "ship": "Red Dwarf", "job": "Evolved Cat", "age": "n/a"},
            {
                "name": "Luke Skywalker",
                "ship": "Millennium Falcon",
                "job": "Jedi",
                "age": "n/a",
            },
            {
                "name": "Trillian",
                "ship": "Heart of Gold",
                "job": "Mathematician",
                "age": "n/a",
            },
            {"name": "Lister", "ship": "Red Dwarf", "job": "Technician", "age": "n/a"},
            {
                "name": "C3PO",
                "ship": "Millennium Falcon",
                "job": "Protocol Droid",
                "age": "n/a",
            },
            {
                "name": "Dave Lister",
                "ship": "Red Dwarf",
                "job": "Third Technician",
                "age": "n/a",
            },
            {
                "name": "Inara Serra",
                "ship": "Serenity",
                "job": "Companion",
                "age": "n/a",
            },
            {
                "name": "Data",
                "ship": "USS Enterprise NCC-1701-D",
                "job": "Science Officer",
                "age": "n/a",
            },
            {
                "name": "Millburn",
                "ship": "Prometheus",
                "job": "Biologist",
                "age": "n/a",
            },
            {
                "name": "Turanga Leela",
                "ship": "Planet Express Ship",
                "job": "Captain",
                "age": "31",
            },
            {
                "name": "Hermes Conrad",
                "ship": "Planet Express Ship",
                "job": "Accountant",
                "age": "50",
            },
            {"name": "Ford", "ship": "Prometheus", "job": "Geologist", "age": "32"},
            {
                "name": "Alara Kitan",
                "ship": "Orville",
                "job": "Chief of Security",
                "age": "23",
            },
            {
                "name": "Nyota Uhura",
                "ship": "USS Enterprise NCC-1701",
                "job": "Communications Officer",
                "age": "n/a",
            },
            {
                "name": "Spock",
                "ship": "USS Enterprise NCC-1701",
                "job": "First Officer",
                "age": "n/a",
            },
            {
                "name": "Beverly Crusher",
                "ship": "USS Enterprise NCC-1701-D",
                "job": "Chief Medical Officer",
                "age": "n/a",
            },
            {"name": "Edward Mercer", "ship": "Orville", "job": "Captain", "age": "42"},
            {
                "name": "Isaac",
                "ship": "Orville",
                "job": "Science and Engineering Officer",
                "age": "400",
            },
            {
                "name": "Ellen Ripley",
                "ship": "Nostromo",
                "job": "Warrant Officer",
                "age": "30",
            },
            {
                "name": "Han Solo",
                "ship": "Millennium Falcon",
                "job": "Captain",
                "age": "n/a",
            },
            {
                "name": "Amy Wong",
                "ship": "Planet Express Ship",
                "job": "Intern",
                "age": "21",
            },
            {
                "name": "Kryten",
                "ship": "Red Dwarf",
                "job": "Service Mechanoid",
                "age": "n/a",
            },
            {
                "name": "Lord Nibbler",
                "ship": "Planet Express Ship",
                "job": "Pet",
                "age": "5",
            },
            {
                "name": "Claire Finn",
                "ship": "Orville",
                "job": "Chief Medical Officer",
                "age": "40",
            },
            {"name": "Lambert", "ship": "Nostromo", "job": "Navigator", "age": "n/a"},
            {
                "name": "Arnold Rimmer",
                "ship": "Red Dwarf",
                "job": "Second Technician",
                "age": "n/a",
            },
            {
                "name": "Kelly Grayson",
                "ship": "Orville",
                "job": "First Officer",
                "age": "36",
            },
            {
                "name": "Bender Bending Rodriguez",
                "ship": "Planet Express Ship",
                "job": "Bending Unit",
                "age": "n/a",
            },
            {"name": "John LaMarr", "ship": "Orville", "job": "Navigator", "age": "32"},
            {
                "name": "Marvin",
                "ship": "Heart of Gold",
                "job": "Paranoid Android",
                "age": "30",
            },
            {"name": "Wash", "ship": "Serenity", "job": "Pilot", "age": "n/a"},
            {"name": "David", "ship": "Prometheus", "job": "Android", "age": "210"},
            {
                "name": "Worf",
                "ship": "USS Enterprise NCC-1701-D",
                "job": "Security Officer",
                "age": "n/a",
            },
            {
                "name": "Pavel Chekov",
                "ship": "USS Enterprise NCC-1701",
                "job": "Navigator",
                "age": "22",
            },
            {"name": "Simon Tam", "ship": "Serenity", "job": "Doctor", "age": "28"},
            {
                "name": "Zoe Washburne",
                "ship": "Serenity",
                "job": "First Mate",
                "age": "n/a",
            },
            {
                "name": "Princess Leia Organa",
                "ship": "Millennium Falcon",
                "job": "Princess",
                "age": "n/a",
            },
            {
                "name": "Ford Prefect",
                "ship": "Heart of Gold",
                "job": "Writer",
                "age": "n/a",
            },
            {
                "name": "Chewbacca",
                "ship": "Millennium Falcon",
                "job": "Co-pilot",
                "age": "200",
            },
            {
                "name": "Obi-Wan Kenobi",
                "ship": "Millennium Falcon",
                "job": "Jedi",
                "age": "60",
            },
            {
                "name": "Charlie Holloway",
                "ship": "Prometheus",
                "job": "Archaeologist",
                "age": "n/a",
            },
            {
                "name": "Kane",
                "ship": "Nostromo",
                "job": "Executive Officer",
                "age": "32",
            },
            {"name": "Ash", "ship": "Nostromo", "job": "Science Officer", "age": "210"},
            {
                "name": "Montgomery Scott",
                "ship": "USS Enterprise NCC-1701",
                "job": "Chief Engineer",
                "age": "n/a",
            },
        ]
    )
)
