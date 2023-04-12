import emoji

def translate_to_emoji(text):
    words = text.split()
    translated = []
    for word in words:
        try:
            emoji_word = emoji.emojize(f":{word.lower()}:")
            translated.append(emoji_word)
        except:
            translated.append(word)
    return " ".join(translated)
