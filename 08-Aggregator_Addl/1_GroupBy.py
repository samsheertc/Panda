#eg1
df = pd.DataFrame(
    {'Animal': ['Falcon', 'Falcon','Parrot', 'Parrot'],
     'Max Speed': [380., 370., 24., 26.]})
df
df.groupby(['Animal']).mean()

#eg2
arrays = [['Falcon', 'Falcon', 'Parrot', 'Parrot'],['Captive', 'Wild', 'Captive', 'Wild']]
index = pd.MultiIndex.from_arrays(arrays, names=('Animal', 'Type'))
df = pd.DataFrame({'Max Speed': [390., 350., 30., 20.]},index=index)

df.groupby(level=0).mean()
df.groupby(level="Animal").mean()

df.groupby(level=1).mean()
df.groupby(level="Type").mean()


#eg3
l = [[1, 2, 3], [1, None, 4], [2, 1, 3], [1, 2, 2]]
df = pd.DataFrame(l, columns=["a", "b", "c"])
df

df.groupby(['b']).sum()
df.groupby(by=["b"]).sum()
df.groupby(['b'], dropna=False).sum()
df.groupby(by=["b"], dropna=False).sum()

#eg4
l = [["a", 12, 12], [None, 12.3, 33.], ["b", 12.3, 123], ["a", 1, 1]]
df = pd.DataFrame(l, columns=["a", "b", "c"])
df.groupby(by="a").sum()
df.groupby(['a']).sum()
df.groupby(by="a", dropna=False).sum()
df.groupby(['a'], dropna=False).sum()

#eg5
df = pd.DataFrame(
{'Animal': ['Falcon', 'Falcon','Parrot', 'Parrot'],
'Max Speed': [380., 370., 24., 26.]
}
)

df.groupby("Animal", group_keys=True)[['Max Speed']].apply(lambda x: x)
df.groupby("Animal", group_keys=False)[['Max Speed']].apply(lambda x: x)
