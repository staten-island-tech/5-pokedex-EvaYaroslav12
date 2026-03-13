def voronivil(villages):
    n = len(villages)
    villages.sort()
    listy=[]
    for i in range(n-2):
       neighborhood = (villages[i+2] - villages[i])/2
       listy.append(neighborhood)
    listy.sort()
    print(min(listy))
voronivil([16, 0, 10 , 4, 15])