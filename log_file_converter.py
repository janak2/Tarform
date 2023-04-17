import pandas as pd
from datetime import datetime

f = open(
    "/Users/janakagrawal/Documents/GitHub/Tarform/InternalLogFiles/2022-12/2022-12-05.log"
)

data_dict = {}
data_dict['timestamp'] = []
data_dict['canID'] =[]
data_dict['canbus'] = []
data_dict['data1'] = []
data_dict['data2'] = []
data_dict['data3'] = []
data_dict['data4'] = []
data_dict['data5'] = []
data_dict['data6'] = []
data_dict['data7'] = []
data_dict['data8'] = []

lines = f.readlines()

for line in lines:
    if 'can' in line:
        line = line[:-1]
        groups = line.split(" ")

        ts = float(groups[0][1:-1])
        ts = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

        canbus = groups[1]

        sgroups = groups[2].split("#")
        canID = sgroups[0]

        bytes = [sgroups[1][i:i+2] for i in range(0, 15, 2)]

        data_dict['timestamp'].append(ts)
        data_dict['canbus'].append(canbus)
        data_dict['canID'].append(canID)
        for i in range(8):
            data_dict['data'+str(i+1)].append(bytes[i])


df = pd.DataFrame(data_dict)
df.to_csv("data/2022-12-05.log")

