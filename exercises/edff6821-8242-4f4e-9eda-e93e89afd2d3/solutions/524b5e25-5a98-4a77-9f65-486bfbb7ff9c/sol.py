text = "John Kowalski met Jeanne Francis Lagarde in Paris in May."

def anonymize(text):
    words = text.split() 
    uppers = [x[0].isupper() for x in [' '] + words + [' ']]
    for i in range(len(words)):
        if uppers[i+1] and (uppers[i] or uppers[i+2]):
            words[i] = "???"
    return " ".join(words)

print (anonymize(text))