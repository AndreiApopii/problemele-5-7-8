zi=['luni','marti','miercuri','joi','vineri','sambata','duminica']
v=[1432,5467,1256,658,3487,76545,1657]
print('venitul saptamanal',sum(v))
print('media venitului zilnic',round(sum(v)//7))
print('cel mai mare venit-',zi[v.index(max(v))])
print('venitul cel mai mic-',zi[v.index(min(v))])