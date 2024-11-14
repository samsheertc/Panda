Flexible apply

df = pd.DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
        "C": np.random.randn(8),
        "D": np.random.randn(8),
    }
)

df

#eg1
grouped = df.groupby("A")
grouped["C"].apply(lambda x: x.describe())

#eg2
grouped = df.groupby('A')['C']
def f(group):
    return pd.DataFrame({'original': group,'demeaned': group - group.mean()})
grouped.apply(f)


#eg3
def f(x):
    return pd.Series([x, x ** 2], index=["x", "x^2"])
s = pd.Series(np.random.rand(5))
s
s.apply(f)



Control grouped column(s) placement with group_keys

df.groupby("A", group_keys=True).apply(lambda x: x, include_groups=False)

df.groupby("A", group_keys=False).apply(lambda x: x, include_groups=False)
