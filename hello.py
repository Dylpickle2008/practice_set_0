#Old Code

"""#ask for user name
name = input("What's your name? ")


#remove whitespace

name = name.strip

#capitalize user name

name = name.title()

#say hello

print(f"hello", name)"""


#Old Code Cont.

"""#ask for user name/whitespace/capitalize
name = input("What's your name? ").strip().title()


def hello():
    print(f"Hello, {name}")   #define function

hello()   #call function"""




def main():
    name = input("What is your name? ").strip().title()
    hello(name)


def hello(user_name):                              #cannot use same parameter as in main function
    print(f"Hello, {user_name}")                   


main()