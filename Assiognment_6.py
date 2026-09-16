# 1
# import numpy as np
# import matplotlib.pyplot as plt

# M = float(input("Enter the value of M: "))

# x = np.linspace(-10, 10, 100)

# y1 = M * x**2
# y2 = M * np.sin(x)

# plt.figure(figsize=(8, 5))

# plt.plot(x, y1, linestyle='--', label='y = M*x²')
# plt.plot(x, y2, linestyle='-', label='y = M*sin(x)')

# plt.title("Mathematical Functions")
# plt.xlabel("X")
# plt.ylabel("Y")

# plt.legend()
# plt.grid(True)

# plt.show()


# 2
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# subjects = ["Maths", "Python", "DBMS", "OS", "AI"]
# scores = [85, 90, 78, 88, 95]

# df = pd.DataFrame({
#     "Subject": subjects,
#     "Score": scores
# })

# print(df)

# plt.figure(figsize=(8, 5))

# ax = sns.barplot(
#     x="Subject",
#     y="Score",
#     data=df,
#     hue="Subject",
#     palette="Set2",
#     legend=False
# )

# for i, score in enumerate(scores):
#     ax.text(i, score + 1, str(score), ha='center')

# plt.title("Subject Scores")
# plt.xlabel("Subjects")
# plt.ylabel("Scores")

# plt.grid(axis='y', linestyle='--', alpha=0.7)

# plt.show()


# 3
# import numpy as np
# import matplotlib.pyplot as plt

# np.random.seed(1024170167)

# data = np.random.randn(50)

# x = np.arange(1, 51)

# cumulative_sum = np.cumsum(data)

# noise = np.random.randn(50)

# fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# axes[0, 0].plot(x, cumulative_sum)
# axes[0, 0].set_title("Cumulative Sum")
# axes[0, 0].set_xlabel("Index")
# axes[0, 0].set_ylabel("Cumulative Sum")
# axes[0, 0].grid(True)

# axes[0, 1].scatter(x, data)
# axes[0, 1].set_title("Random Data Scatter Plot")
# axes[0, 1].set_xlabel("Index")
# axes[0, 1].set_ylabel("Random Value")
# axes[0, 1].grid(True)

# axes[1, 0].plot(x, data)
# axes[1, 0].set_title("Random Data Line Plot")
# axes[1, 0].set_xlabel("Index")
# axes[1, 0].set_ylabel("Random Value")
# axes[1, 0].grid(True)

# axes[1, 1].scatter(x, data + noise)
# axes[1, 1].set_title("Scatter Plot with Random Noise")
# axes[1, 1].set_xlabel("Index")
# axes[1, 1].set_ylabel("Value + Noise")
# axes[1, 1].grid(True)

# plt.tight_layout()

# plt.show()


# 4.1
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# df = pd.read_csv("company_sales_data.csv")

# plt.figure(figsize=(10, 6))

# sns.lineplot(
#     x="month_number",
#     y="total_profit",
#     data=df,
#     marker="o"
# )

# plt.title("Total Profit of All Months")
# plt.xlabel("Month Number")
# plt.ylabel("Total Profit")

# plt.grid(True)

# plt.show()

#4.2
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# df = pd.read_csv("company_sales_data.csv")

# plt.figure(figsize=(12, 7))

# sns.lineplot(x="month_number", y="facecream", data=df, marker="o", label="Face Cream")
# sns.lineplot(x="month_number", y="facewash", data=df, marker="o", label="Face Wash")
# sns.lineplot(x="month_number", y="toothpaste", data=df, marker="o", label="Toothpaste")
# sns.lineplot(x="month_number", y="bathingsoap", data=df, marker="o", label="Bathing Soap")
# sns.lineplot(x="month_number", y="shampoo", data=df, marker="o", label="Shampoo")
# sns.lineplot(x="month_number", y="moisturizer", data=df, marker="o", label="Moisturizer")

# plt.title("Monthly Sales of All Products")
# plt.xlabel("Month Number")
# plt.ylabel("Units Sold")

# plt.legend()
# plt.grid(True)

# plt.show()


#4.3
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# df = pd.read_csv("company_sales_data.csv")

# products = [
#     "facecream",
#     "facewash",
#     "toothpaste",
#     "bathingsoap",
#     "shampoo",
#     "moisturizer"
# ]

# total_sales = df[products].sum()

# sales_df = pd.DataFrame({
#     "Product": total_sales.index,
#     "Total Sales": total_sales.values
# })

# plt.figure(figsize=(10, 6))

# sns.barplot(
#     x="Product",
#     y="Total Sales",
#     data=sales_df,
#     hue="Product",
#     palette="Set2",
#     legend=False
# )

# plt.title("Total Sales of All Products")
# plt.xlabel("Product")
# plt.ylabel("Total Units Sold")

# plt.grid(axis="y", linestyle="--", alpha=0.7)

# plt.show()

