
# def occupied (y,t):
#     n = len(y)
#     x = 0
#     for i in range(n):
#         if (y[i] == "C" and t[i] == 'C'):
#          x = x+1
#     print(x)         
# occupied("CC..C", "CCC.C")

# def language (x):
#     z=x.lower()
#     n = len(x)
#     t = 0
#     s=0
#     for i in range(n):
#         if (z[i] == "t"):
#             t =t+1
#         elif (z[i] == 's'):
#             s=s+1
#     if t > s:
#         print ('English')
#     else:
#         print ('French')
# language('The red cat sat on the mat.')

# def honi(x):
    
#     y = x.lower()
#     n = len(x)
#     z=0
 
#     searchtext = "honi"
#     index = 0

#     for i in range(n):
#         if (y[i] == searchtext[index]):
#             index = index + 1
#             if (index == len(searchtext)-1):
#                 z = z+1
#                 index = 0
#     print (z)

# honi('HHHHOOONNNNIIII')

# def doublecount(x):
#   y = x.lower()
#   n = len(y)
#   z = 0
#   for i in range(n-1):
#       if (y[i]==y[i+1]):
#           z= z+1
#   print(z)
# doublecount('ufheuiwofjewiiijewjwfiivuissiiiii')

def stringcheck(x,y):
  n = len(y)
  m = len(x)

  z = 0
  for i in range (n-m):      
    f = True
    for j in range (m):
      if(y[i+j] != x[j]):
        f = False
    if (f == True): 
      z = z + 1

  print(z)
stringcheck('anc', 'nrricuancanccharemancfiosankc')