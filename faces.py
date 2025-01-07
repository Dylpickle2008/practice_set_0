mydict = {58,41,58,40}

def main():
    happy = input("Tell me something. I will judge you!").translate(mydict)
    moral(happy)

def moral(face):
    print("I think, {face}")

main()