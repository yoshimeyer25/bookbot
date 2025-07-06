def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    chars = {}
    for t in text:
        if t == " " or t == "\n":
            continue
        c = t.lower()
        try:
            chars[c] += 1
        except KeyError:
            chars[c] = 1
    return chars
