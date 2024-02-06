def main():
    emoticon = input("type an emoticon ")
    convert(emoticon)


def convert(to):
    print(to.replace(":)", "🙂").replace(":(", "🙁"))


main()
