import emoji

english = input("Emoji: ")
Emoji = emoji.emojize(english, language="alias")
print(f"Output: {Emoji}")
