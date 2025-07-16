


# def main():
#     x = int(input("What's x? "))
#     print(f"x squared is {square(x)}")

# def square(n):
#     # return n ** 2
#     return pow(n, 2)

# main()























def main():
    # Output without passing the expected arguments
    hello()

    # Output using our own function
    name = input("What is your name? ").strip().title()
    hello(name)

def hello(to = "World"):
    print(f"Hello, {to}")

main()