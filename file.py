import pandas as pd

#import numpy as np
#dataframe4 = pd.DataFrame(np.random.rand(5, 3), columns=['X', 'Y', 'Z'])
#print(dataframe4)

# read the CSV with an encoding that handles non-UTF8 characters (e.g. pound signs)
dataset = pd.read_csv("data.csv", encoding="latin1")
#print(dataset)

#print(dataset.head()) 
#print(dataset.tail())
#print(dataset.info())
#print(dataset.describe())