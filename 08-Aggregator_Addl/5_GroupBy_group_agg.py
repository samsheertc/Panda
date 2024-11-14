#######################################################################
#Selecting a group
grouped = df.groupby('A')
grouped.get_group("bar")
df.groupby(["A", "B"]).get_group(("bar", "one"))

#######################################################################
#Aggregation
animals = pd.DataFrame(
    {
        "kind": ["cat", "dog", "cat", "dog"],
        "height": [9.1, 6.0, 9.5, 34.0],
        "weight": [7.9, 7.5, 9.9, 198.0],
    }
)
animals
animals.groupby("kind").sum()
animals.groupby("kind", as_index=False).sum()

df.groupby("A")[["C", "D"]].max()
df.groupby(["A", "B"]).mean()
grouped = df.groupby(["A", "B"])
grouped.size()
grouped.describe()

ll = [['foo', 1], ['foo', 2], ['foo', 2], ['bar', 1], ['bar', 1]]
df4 = pd.DataFrame(ll, columns=["A", "B"])
df4
df4.groupby("A")["B"].nunique()
#######################################################################
#The aggregate() method
grouped = df.groupby("A")
grouped[["C", "D"]].aggregate("sum")
grouped = df.groupby(["A", "B"])
grouped.agg("sum")


grouped = df.groupby(["A", "B"], as_index=False)
grouped.agg("sum")

df.groupby("A", as_index=False)[["C", "D"]].agg("sum")
df.groupby(["A", "B"]).agg("sum").reset_index()
#######################################################################