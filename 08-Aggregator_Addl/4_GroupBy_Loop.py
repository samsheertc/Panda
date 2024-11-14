#####################################################################################################################################
#DataFrame column selection in GroupBy
df = pd.DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
        "C": np.random.randn(8),
        "D": np.random.randn(8),
    }
)
df
	A	B	       C	       D
0	foo	one	     1.342757	-1.678967
1	bar	one	     1.144578	 0.055248
2	foo	two	     0.614844	-0.829705
3	bar	three	 1.323313	-0.263848
4	foo	two	    -0.269987	 0.735662
5	bar	two	     0.952879	-0.031635
6	foo	one	     0.836097	 1.608343
7	foo	three	-0.758255	-1.016401

grouped = df.groupby(["A"])
grouped_C = grouped["C"]
grouped_D = grouped["D"]

df["C"].groupby(df["A"])

grouped[["A", "B"]].sum()


#Iterating through groups
grouped = df.groupby('A')
for name, group in grouped:
    print(name)
    print(group)
	
	
for name, group in df.groupby(['A', 'B']):
    print(name)
    print(group)
	
#####################################################################################################################################