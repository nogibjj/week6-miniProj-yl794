'''
main function here
'''
import polars as pl
import matplotlib.pyplot as plt

def plot_distribution(data):
    plt.hist(data[::,1].to_numpy(), edgecolor="k")
    plt.title("Distribution of grades")
    plt.xlabel("grades")
    plt.ylabel("Count")
    plt.savefig(f"grades_distribution.png")

def analyze(input):
    res = {}
    stats = {
        "mean": input[::,1].mean(),
        "median": input[::,1].median(),
        "std": input[::,1].std()
    }
    res["grades"] = stats
    return res

if __name__ == "__main__":
    df = pl.read_csv("data.csv")
    res = analyze(df)
    for col, values in res.items():
        print(f"Statistics for {col}:")
        for stat, value in values.items():
            print(f"{stat}: {value}")
        print("\n")

    plot_distribution(df)