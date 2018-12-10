import pandas as pd
import matplotlib.pyplot as plt
from pymongo import MongoClient

data = list(MongoClient().pexes.comparisions.find({}, {
        'random_player': 1,
        'memory_player': 1,
        'mem_size': 1
    }))

data_frame = pd.DataFrame(data)
data_frame.plot(x='mem_size', y=['random_player', 'memory_player'], label=['Random player', 'Memory player'])
plt.legend(loc='upper left')
plt.xlabel('memory size')
plt.ylabel('number of cards (doubles)')
plt.show()
plt.savefig('out.png')
