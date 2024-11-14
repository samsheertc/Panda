# filtrations

speeds
speeds.groupby("class").nth(1)

speeds.groupby("class")[["order", "max_speed"]].nth(1)

head() -> Select the top row(s) of each group
nth()  -> Select the nth row(s) of each group
tail() -> Select the bottom row(s) of each group


product_volumes = pd.DataFrame(
    {
        "group": list("xxxxyyy"),
        "product": list("abcdefg"),
        "volume": [10, 30, 20, 15, 40, 10, 20],
    }
)

product_volumes
	group	product	volume
0	x	       a	10
1	x	       b	30
2	x	       c	20
3	x	       d	15
4	y	       e	40
5	y	       f	10
6	y	       g	20

product_volumes = product_volumes.sort_values("volume", ascending=False)

grouped = product_volumes.groupby("group")["volume"]

cumpct = grouped.cumsum() / grouped.transform("sum")

cumpct

significant_products = product_volumes[cumpct <= 0.9]


significant_products.sort_values(["group", "product"])

