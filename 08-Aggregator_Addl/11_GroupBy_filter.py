sf = pd.Series([1, 1, 2, 3, 3, 3])

sf
0    1
1    1
2    2
3    3
4    3
5    3

sf.groupby(sf).filter(lambda x: x.sum() > 2)
3    3
4    3
5    3

dff = pd.DataFrame({"A": np.arange(8), "B": list("aabbbbcc")})
dff
	A	B
0	0	a
1	1	a
2	2	b
3	3	b
4	4	b
5	5	b
6	6	c
7	7	c

dff.groupby("B").filter(lambda x: len(x) > 2)

dff.groupby("B").filter(lambda x: len(x) > 2, dropna=False)

dff["C"] = np.arange(8)
	A	B	C
0	0	a	0
1	1	a	1
2	2	b	2
3	3	b	3
4	4	b	4
5	5	b	5
6	6	c	6
7	7	c	7

dff.groupby("B").filter(lambda x: len(x["C"]) > 2)
