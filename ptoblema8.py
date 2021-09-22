ora=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
t=[4,5,6,7,9,10,11,12,13,14,15,16,19,20,23,25,27,21,18,17,8,3,2]
print('temperatura medie',round(sum(t)/24))
print('temperatura maxima',max(t))
print('temperatura minima',min(t))
print('ora cu temperatura maxima',ora[t.index(max(t))])
print('ora cu temperatura minima',ora[t.index(min(t))])