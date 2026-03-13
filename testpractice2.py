def countletter(text):
    
    texty = text.lower()
    amountt = text.count("t")
    amounts = text.count('s')
    if amountt > amounts:
        print('English')
    else:
        print('French')
countletter("the red cat sat on the mat.")