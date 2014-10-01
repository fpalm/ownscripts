# Berechnet die ersten n Fibonacci-Zahlen

n = 30
i = 2
fiblist = [0, 1]
while i < n:
	fiblist.append(fiblist[i-2]+fiblist[i-1])
	i+=1

print fiblist
