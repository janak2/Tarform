import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

voltage_can = "10000001"
base_dir = "data"
out_dir = "voltage"
for file_name in os.listdir(base_dir):
    print(file_name)
    df = pd.read_csv(os.path.join(base_dir, file_name), dtype=str)
    df = df[df["canID"] == voltage_can]
    for i in range(1, 9):
        col = "data" + str(i)
        df[col] = df[col].map(lambda x: int(x, 16))
    df["data1"] = df["data1"] * 0.01 + 2.00
    df["data2"] = df["data2"] * 0.01 + 2.00
    df["data3"] = df["data3"] * 0.01 + 2.00
    df["total"] = (
        df["data6"] * (256**3)
        + df["data4"] * (256**1)
        + df["data7"] * (256**2)
        + df["data5"]
    ) * 0.01

    df = df.drop(columns=["data" + str(i) for i in range(4, 9)])
    df.to_csv(os.path.join(out_dir, file_name), index=False)
