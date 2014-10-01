# Demonstriert die Identitaet F(n+1)*F(n-1) - F(n)**2 = (-1)**n

n = 30
i = 2
fiblist = [0, 1]
while i < n:
        fiblist.append(fiblist[i-2]+fiblist[i-1])
        i+=1

for i in range(1, n-1):
        print i, ": \t ", fiblist[i-1]*fiblist[i+1]-fiblist[i]**2, "\t ", (-1)**i, "\t", (fiblist[i-1]*fiblist[i+1]-fiblist[i]**2==(-1)**n)
