text = "I   don't  know   why    it   takes so  much     space.  "
def text_clean(text):
    while True:
        l = len(text)
        text = text.replace('  ', ' ')
        if {{gap}}: break
    return text
        
print(text_clean(text))

# exp output
# I don't know why it takes so much space. 
