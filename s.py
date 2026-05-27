content = """
s = 'Hello'

def say_hi(name):
    print(s + name)
    
class Greet:
        pass
    """

with open("./my_module.py", "w") as fp:
    fp.write(content)
