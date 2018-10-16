import pandas as pd
import matplotlib.pyplot as plt
from pymongo import MongoClient


table100 = list(MongoClient().pexes.winners.find({"table_size": 100}, {"rounds": 1, "mem_size": 1}))
table200 = list(MongoClient().pexes.winners.find({"table_size": 200}, {"rounds": 1, "mem_size": 1}))

table200frame = pd.DataFrame(table100)
table200frame.plot(x='rounds', y='mem_size')
table500frame = pd.DataFrame(table200)
table500frame.plot(x='rounds', y='mem_size')
plt.show()