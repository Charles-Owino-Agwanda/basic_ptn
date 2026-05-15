'''
verb = input("Enter a verb: ")
print("I can ", verb, " better than you")
print(f"I can {verb} better than you")
print("I can {} better than you".format(verb))
output=((verb + " ")*5)
print(output.strip())
'''
'''
x = int(input('What x to find the cube root of? '))
g = int(input('what guess to start with? '))
print('current estimate cubed = ', g**3)
next_g = g - ((g**3 -x)/(3*g**2))
print('next guess to try = ', next_g)
'''
'''
number = 8
user_input = int(input("guess a number: "))
print(user_input == number)
'''
'''
pset_time = 8
sleep_time = 14

if (pset_time + sleep_time) > 24:
    print("impossible")
elif (pset_time + sleep_time) >=24:
    print("full_schedule")
else:
    left_over = abs(24 -pset_time - sleep_time)
    print(left_over, "h of free time!")
print("end of day")
'''

'''
x = int(input("x: "))
y = int(input("y: "))
if x == y:
    print(x, "is the same as", y)
else:
    print("These are not equal!")
'''
'''
x = int(input("x: "))
y = int(input("y: "))
if x == y:
    print("x and y are equal")
    if y != 0:
        print("Therefore, x/y is", x/y)
elif x < y:
    print("x is smaller")
else:
    print("y is smaller")
print("thanks")
'''
my_num = 8
guess = int(input("Enter a guess: "))
if guess > my_num:
    print("Your guess is high")
elif guess < my_num:
    print("Your guess is too low")
else: 
    print("Your guess is the same as my secret")
print("Try again!!")
