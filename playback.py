mydict = {32:46}

def main():
    slow = input("Tell me a joke!").translate(mydict)
    rewind(slow)

def rewind(slow_speech):
    print(f"I can't hear you please speak slower: {slow_speech}")


main()