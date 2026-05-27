import mod2 as md
import platform

a = md.person1["age"]
print(a)

x = platform.uname()
# print(x)

y = dir(platform)
# print(x)


# print("__file__ attribute:", md.__file__)
# print("__doc__ attribute:", md.__doc__)
# print("__name__ attribute:", md.__name__)
print("____dict__attribute:", md.__dict__)
