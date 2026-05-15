'''
where = input("You're lost in the forest. Go left or right? ").lower()
while where == "right":
    where = input("You're lost in the forest. Go left or right? ").lower()
print("You got out of the lost forest!")
'''
'''
n = int(input("please enter a value: "))
while n > 0:
    print(n)
    n -= 1
''' 
'''
n = 0
where = input("Go left or right? ")
while where == "right":
    n += 1
    if n >= 2:
        print("You're lost")
    where = input("Go left or right? ")
print("You got out of the lost forest!")
'''
'''
n = 0
while n < 5:
    print(n)
    n += 1
'''

x = 4
i = 1
factorial = 1
while i <= x:
    factorial = factorial * i
    i += 1
print(f'{x} factorial is {factorial}')