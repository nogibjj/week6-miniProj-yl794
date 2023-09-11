import pandas as pd
import matplotlib.pyplot as plt
from pandas_profiling import ProfileReport


def csvfile(main_data):
    csv = pd.read_csv(main_data)
    return csv


# read the CSV file
df = csvfile("titanic_main_data.csv")

# compute summary statistics
summary = df.describe()

# plot a histogram of the "Age" column
plt.hist(df["Age"], bins=10)
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Histogram of Age")
plt.show()


# generate a analyse report
def report_csvfile():
    csv2 = pd.read_csv("titanic_main_data.csv")
    csv_report = csv2.loc[0:301, ["Age", "Pclass"]]
    profile = ProfileReport(
        csv_report, title="Titanic People Age Report", explorative=True
    )
    profile.to_file("data_profiling_report.html")