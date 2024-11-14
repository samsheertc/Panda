#Enumerate groups

dfg = pd.DataFrame(list("aaabba"), columns=["A"])
dfg
	A
0	a
1	a
2	a
3	b
4	b
5	a



dfg.groupby("A").ngroup()
0    0
1    0
2    0
3    1
4    1
5    0

Here Index for group 'a' = 0 
Here Index for group 'b' = 1


dfg.groupby("A").ngroup(ascending=False)
0    1
1    1
2    1
3    0
4    0
5    1

Here Index for group 'a' = 1 
Here Index for group 'b' = 0