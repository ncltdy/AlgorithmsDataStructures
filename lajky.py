from typing import List


def likes(names: List[str]):
    if len(names) == 0:
        print("nikdo to nelajkoval")
    elif len(names) == 2:
        print(f"{names[0]} a {names[1]} to lajkovali")
    elif len(names) == 3:
        print(f"{names[0]}, {names[1]} a {names[2]} to lajkovali")
    elif len(names) >= 4:
        print(f"{names[0]}, {names[1]} a další {len(names)-2} lidé to lajkovali")



likes([])
likes(["Petr"])
likes(["Petr", "Ana"])
likes(["Petr", "Ana", "Marek"])
likes(["Petr", "Ana", "Marek", "Ola"])