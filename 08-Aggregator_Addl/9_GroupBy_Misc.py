index = pd.date_range("10/1/1999", periods=1100)
ts = pd.Series(np.random.normal(0.5, 2, 1100), index)
ts = ts.rolling(window=100, min_periods=100).mean().dropna()
ts.head()
ts.tail()
transformed = ts.groupby(lambda x: x.year).transform(lambda x: (x - x.mean()) / x.std())

# Original Data
grouped = ts.groupby(lambda x: x.year)
grouped.mean()
grouped.std()

# Transformed Data
grouped_trans = transformed.groupby(lambda x: x.year)
grouped_trans.mean()
grouped_trans.std()


compare = pd.DataFrame({"Original": ts, "Transformed": transformed})
compare.plot()

ts.groupby(lambda x: x.year).transform(lambda x: x.max() - x.min())



cols = ["A", "B", "C"]
values = np.random.randn(1000, 3)
values[np.random.randint(0, 1000, 100), 0] = np.nan
values[np.random.randint(0, 1000, 50), 1] = np.nan
values[np.random.randint(0, 1000, 200), 2] = np.nan
data_df = pd.DataFrame(values, columns=cols)
data_df
countries = np.array(["US", "UK", "GR", "JP"])
key = countries[np.random.randint(0, 4, 1000)]
grouped = data_df.groupby(key)
grouped.count()
transformed = grouped.transform(lambda x: x.fillna(x.mean()))

grouped_trans = transformed.groupby(key)
grouped.mean()        # original group means
grouped_trans.mean()  # transformation did not change group means
grouped.count()       # original has some missing data points
grouped_trans.count() # counts after transformation
grouped_trans.size()  # Verify non-NA count equals group size


# result = ts.groupby(lambda x: x.year).transform(
#     lambda x: (x - x.mean()) / x.std()
# )
grouped = ts.groupby(lambda x: x.year)
result = (ts - grouped.transform("mean")) / grouped.transform("std")

# result = ts.groupby(lambda x: x.year).transform(lambda x: x.max() - x.min())
grouped = ts.groupby(lambda x: x.year)
result = grouped.transform("max") - grouped.transform("min")


# grouped = data_df.groupby(key)
# result = grouped.transform(lambda x: x.fillna(x.mean()))
grouped = data_df.groupby(key)
result = data_df.fillna(grouped.transform("mean")

