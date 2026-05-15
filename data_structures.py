# Tuples

animal_tuple = ("Yellow anaconda", "reptile", 30.5, 20)

print(animal_tuple)


first_index= animal_tuple.index("Yellow anaconda")
print(first_index)
print(animal_tuple[0:2])
print(animal_tuple[-3:])

new_animal_tuple = animal_tuple + ("swamp", False)
print(new_animal_tuple)

new_animal_tuple = new_animal_tuple + (False,)
print(new_animal_tuple)
print(len(new_animal_tuple))

name, group, av_weight, av_lifespan, region, herb, omni = new_animal_tuple

print(name)
print(group)
print(av_weight)
print(av_lifespan)
print(region)
print(herb)
print(omni)