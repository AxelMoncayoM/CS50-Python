
def main():
    emoji = input("Use an emoji: ")
    print(emoji)
    emoji = convert(emoji)
    print(emoji)


def convert(emoji):
    emoji = emoji.replace(":)", "🙂").replace(":(", "🙁")
    return emoji

main()

