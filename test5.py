import random

l = [random.randint(1, 6)  for i in range(picks)]
picks = 10000
times = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0}

for i in l:
    if i == 1:
        times["1"] += 1
    elif i == 2:
        times["2"] += 1
    elif i == 3:
        times["3"] += 1
    elif i == 4:
        times["4"] += 1
    elif i == 5:
        times["5"] += 1
    else:
        times["6"] += 1

prob = [ (i * 100) / picks for i in times.values() ]
print(times)
print(prob)
