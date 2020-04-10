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
    ("Viking", "Mars"),
    ("Ethos", "Venus")
]

for craft in spacecraft:
    print(craft[0], "has visited", craft[1])