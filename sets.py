eat_plants = {"Giraffe", "Elephant", "Bear", "Rabbit", "Fox"}
print(eat_plants)
eats_meat = set(["Lion", "Tiger","Bear", "Hawk", "Fox","Lion"])
print(eats_meat)
print(type(eat_plants))

print("Lion" in eats_meat)

eat_plants.add("Cow")
print(eat_plants)

eats_meat.update({"Leopard", "Cheetah"})
print(eats_meat)

eats_meat.discard("Rabbit")
print(eats_meat)

all_animals = eats_meat.union(eat_plants)
print(all_animals)

omnivores = eats_meat.intersection(eat_plants)
print(omnivores)

carnivores = eats_meat.difference(eat_plants)
print(carnivores)


eats_plants_subset = eat_plants.issubset(all_animals)
print(eats_plants_subset)