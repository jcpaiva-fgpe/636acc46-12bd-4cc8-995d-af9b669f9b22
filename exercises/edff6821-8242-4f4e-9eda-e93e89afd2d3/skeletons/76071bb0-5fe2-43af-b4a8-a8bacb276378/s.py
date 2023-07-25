text = "John Kowalski met Jeanne Francis Lagarde in Paris in May."

def anonymize(text):
    words = text.split() 
    uppers = [x[0].isupper() for x in [' '] + words + [' ']]
    for i in range(len(words)):
        if uppers[i+1] and ({{gap}}):
            words[i] = "???"
    return " ".join(words)

print (anonymize(text))

# exp output
# ??? ??? met ??? ??? ??? in Paris in May.
