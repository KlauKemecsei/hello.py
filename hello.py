"""Basic Function WS
First of all, create a local repository in a new folder named basic_function_hello and add a new file hello.py

1.) Task 1 - printing hello

As the product owner, I would like to have a script that is able to write a hello world message to the terminal!

your task is to use the print built-in function

COMMIT IT"""

print("Hello World!")


"""2.) Task 2 - customized print

As a product owner, I would like to see customized print to see more personal greetings!

The name for greeting comes from user input

your task is to read a name from the user and print hello name (name comes from input)

COMMIT IT"""

name = input("Please, give me your name: ")
print(f"Hello {name} !")


"""3.) Task 3 - carry out to function

As an architect, I would like to see more usable code to have the maintainability and reusability in the stable!

your task is to create a function hello() without parameter, the function has to work as the previous task described

COMMIT IT"""

def hello():
    name = input("Please, give me your name: ")
    print(f"Hello {name} !")
    


"""4.) Task 4 - Open to extend

As an architect, I won't provide a reusable, parameterizable function in order to have one single responsibility in the hello() function.
One responsibility is to read user input other one is to greet.

your task is to change the hello() function to hello(name) and have the same solution as before say hello name
Az Ön feladata az, hogy a hello() függvényt hello(név) függvényre változtassa, 
és ugyanolyan megoldást kapjon, mint korábban say hello name
COMMIT IT"""


def hello(name):
    print(f"Hello {name} !")

name = input("Please, give me your name: ")

hello(name)


"""5.) Task 5 - Handle defaults

As a product owner, I would like to see a 'hello world'

your task is to solve this by using a keyword argument

COMMIT IT"""

def hello(name="World"):
    print(f"Hello {name} !")


hello()



"""6.) Task 6 - who greet who

As a product owner, I would like to see who is greeting who.

your task is to change the hello function to have two parameters hello(send_name, receive_name)

By the calling, you should use naming arguments in order to use arguments in a different order."""

def hello(send_name, receive_name):
    print(f"{send_name} says hello to {receive_name}")




"""7.) Task 7 - Greet everyone

As the product owner, I would like to see that the hello function has unlimited arguments and it is able to say hello to everyone!

your task is to use variable arguments in order to solve it"""
def hello(*args):
    print(f"Hello to {', '.join(args)}")