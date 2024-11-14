#Splitting an object into groups

DataFrame.groupby
(
by         =None,
axis       =<no_default>,
level      =None,
as_index   =True,
sort       =True,
group_keys =True,
observed   =<no_default>,
dropna     =True
)
#####################################################################################################################################
#Eg1
speeds = pd.DataFrame(
    [
        ("bird", "Falconiformes", 389.0),
        ("bird", "Psittaciformes", 24.0),
        ("mammal", "Carnivora", 80.2),
        ("mammal", "Primates", np.nan),
        ("mammal", "Carnivora", 58),
    ],
    index=["falcon", "parrot", "lion", "monkey", "leopard"],
    columns=("class", "order", "max_speed"),
)

speeds
	   class	order	        max_speed
falcon	bird	Falconiformes	389.0
parrot	bird	Psittaciformes	24.0
lion	mammal	Carnivora	    80.2
monkey	mammal	Primates	    NaN
leopard	mammal	Carnivora	    58.0

grouped = speeds.groupby("class")
grouped = speeds.groupby(["class", "order"])
#####################################################################################################################################
#Eg2
df = pd.DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
        "C": np.random.randn(8),
        "D": np.random.randn(8),
    }
)

df
	A	B	    C	         D
0	foo	one	    0.541539	 1.159626
1	bar	one	    0.960195	-0.641784
2	foo	two	    1.116569	 0.614636
3	bar	three  -1.773634	-1.368674
4	foo	two	    0.405849    -0.487575
5	bar	two	    0.763626     1.988514
6	foo	one	   -0.449170     0.497680
7	foo	three  -1.539388	-0.949600

grouped = df.groupby("A")
grouped = df.groupby("B")
grouped = df.groupby(["A", "B"])
#####################################################################################################################################
##Eg3
df2 = df.set_index(["A", "B"])
grouped = df2.groupby(level=df2.index.names.difference(["B"]))
grouped.sum()

def get_letter_type(letter):
    if letter.lower() in 'aeiou':
        return 'vowel'
    else:
        return 'consonant'

grouped = df.T.groupby(get_letter_type)

#Eg3
index = [1, 2, 3, 1, 2, 3]
s = pd.Series([1, 2, 3, 10, 20, 30], index=index)

s
1     1
2     2
3     3
1    10
2    20
3    30

grouped = s.groupby(level=0)
grouped.first()
grouped.last()
grouped.sum()
#####################################################################################################################################