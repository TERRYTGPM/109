import pandas as pd
import csv
import statistics

df = pd.read_csv("data.csv")

heightlist = df["Height"].tolist()
weightlist = df["Weight"].tolist()

hmean = statistics.mean(heightlist)
hmode = statistics.mode(heightlist)
hmedian = statistics.median(heightlist)
hsd = statistics.stdev(heightlist)

#print(hsd)
#print(hmean)
#print(hmedian)
#print(hmode)
e = len(heightlist)

hs1, he1, hs2, he2, hs3, he3 = hmean-hsd, hmean+hsd, hmean-2*hsd, hmean+2*hsd, hmean-3*hsd, hmean+3*hsd

heightlist1 = [result for result in heightlist if result>hs1 and result<he1]
heightlist3 = [result for result in heightlist if result>hs3 and result<he3]
heightlist2 = [result for result in heightlist if result>hs3 and result<he2]
per1 = len(heightlist1)/e * 100
per3 = len(heightlist3)/e * 100
per2 = len(heightlist2)/e * 100
print(per1)
print(per2)
print(per3)
