#Applying different functions to DataFrame columns
df = pd.DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
        "C": np.random.randn(8),
        "D": np.random.randn(8),
    }
)
df
grouped = df.groupby("A")

grouped.agg({"C": "sum", "D": lambda x: np.std(x, ddof=1)})
grouped.agg({"C": "sum", "D": "std"})


#Transformation
speeds
grouped = speeds.groupby("class")["max_speed"]
grouped.cumsum()
grouped.diff()

result = speeds.copy()
result["cumsum"] = grouped.cumsum()
result["diff"] = grouped.diff()
result


#The transform() method
grouped = speeds.groupby("class")[["max_speed"]]
grouped.transform("cumsum")
grouped.transform("sum")


#Built-in transformation methods
bfill()      -> Back fill NA values within each group
cumcount()   -> Compute the cumulative count within each group
cummax()     -> Compute the cumulative max within each group
cummin()     -> Compute the cumulative min within each group
cumprod()    -> Compute the cumulative product within each group
cumsum()     -> Compute the cumulative sum within each group
diff()       -> Compute the difference between adjacent values within each group
ffill()      -> Forward fill NA values within each group
pct_change() -> Compute the percent change between adjacent values within each group
rank()       -> Compute the rank of each value within each group
shift()      -> Shift values up or down within each group
