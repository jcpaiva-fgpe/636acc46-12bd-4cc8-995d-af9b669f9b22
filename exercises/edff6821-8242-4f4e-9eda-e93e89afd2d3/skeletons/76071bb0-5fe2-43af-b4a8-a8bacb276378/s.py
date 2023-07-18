text = "John Kowalski met Jeanne Francis Lagarde in Paris in May."

def anonymize(text):
    words = text.split() 
    uppers = [{{gap}} for x in [' '] + words + [' ']]
    for i in range(len(words)):
        if {{gap}} and ({{gap}} or {{gap}}):
            words[i] = "???"
    return " ".join(words)

print (anonymize(text))