# finde Primzahlen von 2 bis primemax
#
primemax = 2000000

primeliste = [2, 3, 5, 7 ]
p = 11
while p < primemax:
    t = 3
    while  t*t <= p :
      if p % t == 0 :
          break
      t += 2
    if t*t > p :
        primeliste.append(p)
    p += 2

print len(primeliste)
print primeliste[-10:]
