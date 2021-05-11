import random
import statistics
import plotly.figure_factory as ff

diceresult = []

for i in range(0, 1000):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    diceresult.append(dice1 + dice2)

mean = sum(diceresult)/len(diceresult)
sd = statistics.stdev(diceresult)

median = statistics.median(diceresult)
mode = statistics.mode(diceresult)

fig = ff.create_distplot([diceresult], ["result"], show_hist = False)

print(sd)
print(mean)
print(median)
print(mode)
fig.show()