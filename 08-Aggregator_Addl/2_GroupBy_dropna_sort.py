#GroupBy sorting
#####################################################################################################################################
#Eg1
df2 = pd.DataFrame({"X": ["B", "B", "A", "A"], "Y": [1, 2, 3, 4]})
df2
	X	Y
0	B	1
1	B	2
2	A	3
3	A	4

df2.groupby(["X"]).sum()
df2.groupby(["X"], sort=False).sum()
#####################################################################################################################################
#Eg2
df3 = pd.DataFrame({"X": ["A", "B", "A", "B"], "Y": [1, 4, 3, 2]})
df3
	X	Y
0	A	1
1	B	4
2	A	3
3	B	2

df3.groupby("X").get_group("A")
df3.groupby(["X"]).get_group(("B",))
#####################################################################################################################################
#GroupBy dropna
df_list = [[1, 2, 3], [1, None, 4], [2, 1, 3], [1, 2, 2]]
df_dropna = pd.DataFrame(df_list, columns=["a", "b", "c"])
df_dropna
	a	b	  c
0	1	2.0	  3
1	1	NaN	  4
2	2	1.0	  3
3	1	2.0	  2

df_dropna.groupby(by=["b"], dropna=True).sum()
df_dropna.groupby(by=["b"], dropna=False).sum()
#####################################################################################################################################
#GroupBy object attributes
df = pd.DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
        "C": np.random.randn(8),
        "D": np.random.randn(8),
    }
)
df
	A	B	   C	         D
0	foo	one	   -0.610375	 0.239364
1	bar	one	   -0.734957	 1.004060
2	foo	two	   -0.226266	-0.438301
3	bar	three	1.354495	-0.080677
4	foo	two	    0.927002	 0.556479
5	bar	two	    0.910017	 0.678597
6	foo	one	    2.000944	 0.824918
7	foo	three	0.415942	-2.421141


df.groupby("A").groups
df.T.groupby(get_letter_type).groups
grouped = df.groupby(["A", "B"])
grouped.groups
len(grouped)
#####################################################################################################################################
n = 10
weight = np.random.normal(166, 20, size=n)
height = np.random.normal(60, 10, size=n)
time = pd.date_range("1/1/2000", periods=n)
gender = np.random.choice(["male", "female"], size=n)

df = pd.DataFrame(
    {"height": height, "weight": weight, "gender": gender},
	index=time
)
df
gb = df.groupby("gender")
#####################################################################################################################################