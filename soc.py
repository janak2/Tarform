import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os


def signed_int(x):
    x = int(x, 16)
    if x >= int("80", 16):
        x -= int("100", 16)
    return x


voltage_can = "10000500"
base_dir = "data"
out_dir = "current"
for file_name in os.listdir(base_dir):
    print(file_name)
    df = pd.read_csv(os.path.join(base_dir, file_name), dtype=str)
    df = df[df["canID"] == voltage_can]

    df["data1"] = df["data1"].map(lambda x: signed_int(x))
    for i in [2, 3, 4, 7]:
        col = "data" + str(i)
        df[col] = df[col].map(lambda x: int(x, 16))
    df["current"] = (df["data1"] * 256 + df["data2"]) * 0.1
    df["charge"] = (df["data3"] * 256 + df["data4"]) * 0.1
    df["soc"] = df["data7"]

    df = df.drop(columns=["data" + str(i) for i in range(1, 9)])
    df.to_csv(os.path.join(out_dir, file_name), index=False)
    break
