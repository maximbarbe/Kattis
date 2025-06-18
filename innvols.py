from collections import*;w=input();o=len(w);c=Counter([w[i:j] for i in range(o) for j in range(i+1,o+1)]);t=[*c.keys()];t.sort(key=lambda e:(-c[e],e))
for k in t:print(c[k],k)