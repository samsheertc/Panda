###########################################################################################
#NA group handling
df = pd.DataFrame({"key": [1.0, 1.0, np.nan, 2.0, np.nan], "A": [1, 2, 3, 4, 5]})
df
	key	A
0	1.0	1
1	1.0	2
2	NaN	3
3	2.0	4
4	NaN	5


df.groupby("key", dropna=True).sum()
df.groupby("key", dropna=False).sum()

###########################################################################################
#Grouping with ordered factors
days = pd.Categorical(
    values=["Wed", "Mon", "Thu", "Mon", "Wed", "Sat"],
    categories=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
)

data = pd.DataFrame(
   {
       "day": days,
       "workers": [3, 4, 1, 4, 2, 2],
   }
)

data


data.groupby("day", observed=False, sort=True).sum()
data.groupby("day", observed=False, sort=False).sum()


###########################################################################################
#Grouping with a grouper specification
import datetime

df = pd.DataFrame(
    {
        "Branch": "A A A A A A A B".split(),
        "Buyer": "Carl Mark Carl Carl Joe Joe Joe Carl".split(),
        "Quantity": [1, 3, 5, 1, 8, 1, 9, 3],
        "Date": [
            datetime.datetime(2013, 1, 1, 13, 0),
            datetime.datetime(2013, 1, 1, 13, 5),
            datetime.datetime(2013, 10, 1, 20, 0),
            datetime.datetime(2013, 10, 2, 10, 0),
            datetime.datetime(2013, 10, 1, 20, 0),
            datetime.datetime(2013, 10, 2, 10, 0),
            datetime.datetime(2013, 12, 2, 12, 0),
            datetime.datetime(2013, 12, 2, 14, 0),
        ],
    }
)

df
	Branch	Buyer	Quantity	 Date
0	A	      Carl	   1	     2013-01-01 13:00:00
1	A	      Mark	   3	     2013-01-01 13:05:00
2	A	      Carl	   5	     2013-10-01 20:00:00
3	A	      Carl	   1	     2013-10-02 10:00:00
4	A	      Joe	   8	     2013-10-01 20:00:00
5	A	      Joe	   1	     2013-10-02 10:00:00
6	A	      Joe	   9	     2013-12-02 12:00:00
7	B	      Carl	   3	     2013-12-02 14:00:00

#group by Month End and Buyer
df.groupby([pd.Grouper(freq="1ME", key="Date"), "Buyer"])[["Quantity"]].sum()

df = df.set_index("Date")
df["Date"] = df.index + pd.offsets.MonthEnd(2)

#Group Based on Column
df.groupby([pd.Grouper(freq="6ME", key="Date"), "Buyer"])[["Quantity"]].sum()

#Group Based on Index
df.groupby([pd.Grouper(freq="6ME", level="Date"), "Buyer"])[["Quantity"]].sum()

###########################################################################################
#Taking the first rows of each group
df = pd.DataFrame([[1, 2], [1, 4], [5, 6]], columns=["A", "B"])
g = df.groupby("A")
g.head(1)
g.tail(1)

#Taking the nth row of each group
df = pd.DataFrame([[1, np.nan], [1, 4], [5, 6]], columns=["A", "B"])
g = df.groupby("A")
g.nth(0)
g.nth(-1)
g.nth(1)
g.nth(5) #Empty DataFrame


# nth(0) is the same as g.first()
g.nth(0, dropna="any")
g.first()

# nth(-1) is the same as g.last()
g.nth(-1, dropna="any")
g.last()

g.B.nth(0, dropna="all")
