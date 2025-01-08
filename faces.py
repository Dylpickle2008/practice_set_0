def main():
    emoticon = input("Tell me an emoticon and I'll convert it to emoji pls!")
    emoticon = emoji(emoticon)

def emoji(emoticon):
    emoticon = emoticon.replace(":)", "🙂")
    emoticon = emoticon.replace(":(", "🙁")
    print(f"Here is ur emoji: {emoticon}")
    return emoticon

main()