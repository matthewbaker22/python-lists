planet_list = ["Mercury", "Mars"]

# === Append ===
planet_list.append("Jupiter")
planet_list.append("Saturn")

# === Extend ===
planet_list.extend(["Uranus", "Neptune"])

# === Insert ===
planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")

# === Append Again ===
planet_list.append("Pluto")

spacecraft = [
    ("Cassini", "Saturn"),
    ("Viking", "Mars")
    # ("Ethos", "Venus")
]

for planet in planet_list:
    for craft in spacecraft:
        if craft[1] == planet:
            print(planet, "has been visited by", craft[0])
    