mammals = ["Lion", "Elephant", "Dolphin"]


range_list = list(range(0,11,2))
birds = list(("Eagle", "Penguin", "Parrot"))

print(mammals)
print(range_list)
print(birds)

animals_combined = mammals + birds
print(animals_combined)

mammals_copy = mammals.copy()
print(mammals_copy)

animals_grouped = [mammals, birds]
print(animals_grouped)

print(animals_grouped.index(mammals))
print(animals_grouped.index(birds))
print(mammals.index("Lion"))

print(range_list[3])

print(animals_grouped[0][0:2])

mammals_copy.append(["cat", "dog"])
print(mammals_copy)
mammals_copy.extend(["Bear", "Horse"])
print(mammals_copy)
mammals_copy.insert(2, "Tiger")
print(mammals_copy)

del mammals_copy[2]
print(mammals_copy)

mammals_copy.remove("Dolphin")
print(mammals_copy)

first_mammal= mammals_copy.pop(0)
print(first_mammal)
print(mammals_copy)


print(mammals)
mammals.sort()
print(mammals)
mammals.sort(reverse=True)
print(mammals)
print(animals_combined)
animals_sorted = sorted(animals_combined, reverse=True)
print(animals_sorted)

boolean_list = [False, True]
print(any(boolean_list))
print(all(boolean_list))