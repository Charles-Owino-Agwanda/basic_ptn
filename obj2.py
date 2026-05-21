class tree:
    def __init__(self, species, height, age):
        self.species = species
        self.height = height
        self.age = age
        
    def grow(self):
        self.height +=1
        
    def reseed(self):
        print(f"The {self.species} tree disperses seeds for new trees")
        
class pine(tree):
    def cone_count(self):
        print(f"The {self.species} tree has many cones.")
        
class oak(tree):
    def budding(self):
        print(f"The {self.species} tree is budding new leaves.")
        
    
pine_tree = pine("Pine", 15, 50)
oak_tree = oak("oak", 100, 20)

oak_tree.grow()
pine_tree.grow()

#oak_tree.budding()
#pine_tree.cone_count()