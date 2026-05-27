import my_module as md
import math

try:
    print(md.s)
    md.say_hi(" Charles")
except NameError:
    print("Variable 's' does not exists!")

x = math.sqrt(81)
print(x)
all = dir(math)
print(all)
