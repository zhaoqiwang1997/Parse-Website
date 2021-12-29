# visualisations

# libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# use seaborn style
# upgrade it with "pip install seaborn --upgrade"
sns.set_theme()

def clean(x):
    x = x.replace("+", "").replace(",", "")
    return float(x)

# create data and picture
file_path = "/Users/wangzhaoqi/Desktop/Parse_Website/nft.csv"
with open(file_path, "r", encoding="UTF8") as f:
    df = pd.read_csv(f)

    # clean the data to float
    df["followers"] = df["followers"].apply(clean)
    print(df)
    print(df.dtypes)

    # use the plot function
    df.plot(x="Date", y="followers", kind="line", title="Growth", figsize=(8, 6))

    # save plot to the file (must above plt.show())
    plt.savefig("trend.png", dpi=300)

    plt.show()
