list_of_numbers = list(range(0,30,5))
for i in list_of_numbers:
    pass

animals = ['Great White Shark', 'Blue Whale', 'African Elephant', 'Bald Eagle','Orangutan', 'Tiger', 'Panda', 'Koala']

animals_we_have_seen = []
for animal in animals:
    animals_we_have_seen.append(animal)
#print(f"we saw these animals: \n {animals_we_have_seen}")

animals_tuple = tuple(animals)
#print(animals_tuple)
animals_set= set(animals)
#print(animals_set)
for animal in animals:
    print(animal)
    if animal == "Bald Eagle":
        print('Bald Eagle Found')
        break
print(f'The least animal checked ={animal}')
