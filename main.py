import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")

sns.set_style("whitegrid")
sns.set_palette("Set2")
# 1) Trend 
sns.lineplot(x="Month",y="Sales",data=df,marker='o', linewidth=3)
plt.title("Monthly Sales Trend", fontsize=16, fontweight="bold")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.savefig("sales_trend.png", dpi=300, bbox_inches="tight")
plt.clf()

# 2) Profit comparision
sns.barplot(x="Month",y="Profit",data=df)
plt.title("Monthly Profit", fontsize=16, fontweight="bold")
plt.savefig("profit_bar.png", dpi=300, bbox_inches="tight")
plt.clf()

# 3) Relation
sns.scatterplot(x="Sales",y="Profit",data=df, s=100)
plt.title("Sales vs Profit",fontsize=16)
plt.savefig("relation.png", dpi=300, bbox_inches="tight")
plt.clf()

# 4) Correlation
corr = df.corr(numeric_only=True)
sns.heatmap(corr , annot=True, cmap="coolwarm" , linewidths=1)
plt.title("Correlation Matrix", fontsize=16)
plt.savefig("heatmap.png", dpi=300, bbox_inches="tight")

print("Done: PNG File Saved")