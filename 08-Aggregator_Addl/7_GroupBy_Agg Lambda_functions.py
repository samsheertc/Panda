#Aggregation with User-Defined Functions
animals = pd.DataFrame(
    {
        "kind": ["cat", "dog", "cat", "dog"],
        "height": [9.1, 6.0, 9.5, 34.0],
        "weight": [7.9, 7.5, 9.9, 198.0],
    }
)
animals

	kind	height	weight
0	cat	    9.1	    7.9
1	dog	    6.0	    7.5
2	cat	    9.5	    9.9
3	dog	    34.0	198.0

animals.groupby("kind")[["height"]].agg(lambda x: set(x))
animals.groupby("kind")[["height"]].agg(lambda x: x.astype(int).sum())
################################################################################################
#Applying multiple functions at once
grouped = df.groupby("A")

grouped["C"].agg(["sum", "mean", "std"])

grouped[["C", "D"]].agg(["sum", "mean", "std"])


(
    grouped["C"]
    .agg(["sum", "mean", "std"])
    .rename(columns={"sum": "foo", "mean": "bar", "std": "baz"})
)

(
    grouped[["C", "D"]].agg(["sum", "mean", "std"]).rename(
        columns={"sum": "foo", "mean": "bar", "std": "baz"}
    )
)

grouped["C"].agg(["sum", "sum"])
grouped["C"].agg([lambda x: x.max() - x.min(), lambda x: x.median() - x.mean()])

################################################################################################
#Named aggregation
animals = pd.DataFrame(
    {
        "kind": ["cat", "dog", "cat", "dog"],
        "height": [9.1, 6.0, 9.5, 34.0],
        "weight": [7.9, 7.5, 9.9, 198.0],
    }
)

animals

	kind	height	weight
0	cat	     9.1	7.9
1	dog	     6.0	7.5
2	cat	     9.5	9.9
3	dog	     34.0	198.0


animals.groupby("kind").agg(
    min_height=pd.NamedAgg(column="height", aggfunc="min"),
    max_height=pd.NamedAgg(column="height", aggfunc="max"),
    average_weight=pd.NamedAgg(column="weight", aggfunc="mean"),
)

animals.groupby("kind").agg(
    min_height=("height", "min"),
    max_height=("height", "max"),
    average_weight=("weight", "mean"),
)

animals.groupby("kind").agg(
    **{
        "total weight": pd.NamedAgg(column="weight", aggfunc="sum")
    }
)

animals.groupby("kind").height.agg(
    min_height="min",
    max_height="max",
)
################################################################################################