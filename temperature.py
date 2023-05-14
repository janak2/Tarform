import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

can = "10000002"
base_dir = "data"
out_dir = "temperature"
for file_name in os.listdir(base_dir):
    print(file_name)
    df = pd.read_csv(os.path.join(base_dir, file_name), dtype=str)
    df = df[df["canID"] == can]
    for i in range(1, 4):
        col = "data" + str(i)
        df[col] = df[col].map(lambda x: int(x, 16))
    df["data1"] = df["data1"] - 100
    df["data2"] = df["data2"] - 100
    df["data3"] = df["data3"] - 100

    df = df.drop(columns=["data" + str(i) for i in range(4, 9)])
    df.to_csv(os.path.join(out_dir, file_name), index=False)
