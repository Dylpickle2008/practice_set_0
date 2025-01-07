def main():
    loudest = input("SCREAM in your loudest capital voice!!! ").strip().casefold()
    lower(loudest)


def lower(loudest):
    print(f"Be quiet, this is a library bro, {loudest}")

main()