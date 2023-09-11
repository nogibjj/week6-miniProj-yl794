'''
main function here
'''
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    dataframe = pd.read_csv("./test.csv")
    # analyze
    target = dataframe[" \"Final\""]
    print("Mean: ", target.mean())
    print("Median: ", target.median())
    plt.scatter(dataframe["name"], dataframe[" \"Final\""])
    plt.savefig("result.png")