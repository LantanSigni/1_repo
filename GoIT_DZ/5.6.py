def is_spam_words(text, spam_words, space_around=False):

    text = text.lower()
    for spam_word in spam_words:
        spam_word = spam_word.lower()

        if space_around:
            if f" {spam_word} " in f" {text} " or text.startswith(f"{spam_word} ") or text.endswith(f" {spam_word}") or f" {spam_word}." in f" {text} ":
                return True
        else:
            if spam_word in text:
                return True
    return False
