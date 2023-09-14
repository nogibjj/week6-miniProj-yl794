'''
main function here
'''
import polars as pl
import matplotlib.pyplot as plt

def plot_polar(data):
    plt.hist(data[::,1].to_numpy(), edgecolor="b")
    plt.title("Statics of students' grades")
    plt.xlabel("Grade")
    plt.ylabel("Num")
    plt.savefig("RESULT.png")


if __name__ == "__main__":
    df = pl.read_csv("test.csv")
    stats = {
        "mean": df[::,1].mean(),
        "std": df[::,1].std()
    }
    res = {"grades" :stats}
    plot_polar(df)