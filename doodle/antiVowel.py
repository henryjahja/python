def anti_vowel(text):
    for eachLetter in text:
        if eachLetter.lower() in ['a','e','i','o','u']:
                text = text.replace(eachLetter, '')
    return text
