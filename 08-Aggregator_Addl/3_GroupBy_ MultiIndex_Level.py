#GroupBy with MultiIndex
#####################################################################################################################################
#eg1
arrays = [
    ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
    ["one", "two", "one", "two", "one", "two", "one", "two"],
]
index = pd.MultiIndex.from_arrays(arrays, names=["first", "second"])
s = pd.Series(np.random.randn(8), index=index)
s

first  second
bar    one       0.076221
bar    two      -0.757531
baz    one       1.952837
baz    two      -0.392886
foo    one      -0.996285
foo    two      -0.051184
qux    one       0.216164
qux    two      -2.873620
	   
grouped = s.groupby(level=0)
grouped.sum()
s.groupby(level="second").sum()

#####################################################################################################################################
#eg2
arrays = [
    ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
    ["doo", "doo", "bee", "bee", "bop", "bop", "bop", "bop"],
    ["one", "two", "one", "two", "one", "two", "one", "two"],
]
index = pd.MultiIndex.from_arrays(arrays, names=["first", "second", "third"])
s = pd.Series(np.random.randn(8), index=index)

s
first  second  third
bar    doo     one      0.570101
bar    doo     two     -0.243474
baz    bee     one      1.927505
baz    bee     two     -1.534175
foo    bop     one      0.600583
foo    bop     two      1.129668
qux    bop     one      0.866207
qux    bop     two     -0.716745
			   
s.groupby(level=["first", "second"]).sum()
s.groupby(["first", "second"]).sum()

#####################################################################################################################################
#Grouping DataFrame with Index levels and columns
arrays = [
    ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
    ["one", "two", "one", "two", "one", "two", "one", "two"],
]
index = pd.MultiIndex.from_arrays(arrays, names=["first", "second"])
df = pd.DataFrame({"A": [1, 1, 1, 1, 2, 2, 3, 3], "B": np.arange(8)}, index=index)
df

		           A	B
first	second		
bar	    one	       1	0
bar	    two	       1	1
baz	    one	       1	2
baz	    two	       1	3
foo	    one	       2	4
foo	    two	       2	5
qux	    one	       3	6
qux	    two	       3	7


df.groupby([pd.Grouper(level=1), "A"]).sum()
df.groupby([pd.Grouper(level="second"), "A"]).sum()
df.groupby(["second", "A"]).sum()
#####################################################################################################################################

	