
def main():
    # Prompt the user for an input
    emoji = input("How do you feel, Happy - :) or Sad - :(? ")

    # calling the convert function
    convert(emoji)

    # Print converted message
    print(convert(emoji))

# Defining the convert function
def convert(emoji):
    if ":)" in emoji:
        return emoji.replace(":)", "🙂")
    else:
        return emoji.replace(":(", "🙁")
    
main()