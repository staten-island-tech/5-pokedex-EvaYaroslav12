
text = "the red cat sat on the mat."
amountt = text.count("t")
amountT = text.count("T")
amounts = text.count('s')
amountS = text.count('S')
if amountt+amountT > amounts+amountS:
    print('English')
else:
    print('French')