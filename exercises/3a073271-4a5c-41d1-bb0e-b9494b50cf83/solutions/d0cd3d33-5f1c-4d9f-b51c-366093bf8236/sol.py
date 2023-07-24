text = "I   don't  know   why    it   takes so  much     space.  "
def text_clean(text):
    while True:
        l = len(text)
        text = text.replace('  ', ' ')
        if l == len(text): break
    return text
