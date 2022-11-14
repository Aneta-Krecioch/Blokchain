#1 Create two variables – one with your name and one with your age

user_name=input('Your name: ')
user_age=input('Your age: ')

#2 Create a function which prints your data as one string
"""def print_user_data():
    print(name + '-' + age)
print_user_data()"""

def greet (name, age):
    print('Hello ' + name + ' ,I am ' + age)
greet(user_name,user_age)

#3 Create a function which prints ANY data (two arguments) as one string
"""def print_concatenated_data(el1, el2):
    print(el1 + '-' + el2)
print_user_data(name, age)"""

def sum(a, b):
    print(a+'-'+b)
sum(user_name, user_age)

#4 Create a function which calculates and returns the number of decades you already lived (e.g. 23 = 2 decades)

def numbers_of_decades(age):
    decades=age // 10
    return decades

decades = numbers_of_decades(int(user_age))
print(decades)