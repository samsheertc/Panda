DataFrame
---------
idx=[1,2,3]
col=['Col1', 'Col2', 'Col3']

d1 = { 
    'Col1' : ['key1_v1', 'key1_v2','key1_v3'],
    'Col2' : ['key2_v1', 'key2_v2','key2_v3'],
    'Col3' : ['key3_v1', 'key3_v2','key3_v3'],
}

d2=[[1,2,3],[11,12,13],[21,22,23]]
d3=[(1,2,3),(11,12,13),(21,22,23)]
d4=([1,2,3],[11,12,13],[21,22,23])
d5=((1,2,3),(11,12,13),(21,22,23))

pd.DataFrame(data=d1,index=idx,columns=col)


Series
------
idx=['a','b','c']
d1 = [1,2,3]
d2 = (1,2,3)
pd.Series(data=d1,index=idx,name='Items',dtype='float64')
pd.Series(data=d1,index=idx,name='Items',dtype='int64')


MultiIndex
----------
d1=[[1,2,3],[11,12,13],[21,22,23]]
d2=[(1,2,3),(11,12,13),(21,22,23)] ****
d3=([1,2,3],[11,12,13],[21,22,23])
d4=((1,2,3),(11,12,13),(21,22,23))
pd.MultiIndex.from_arrays(d1,names=['level1', 'level2','level3'])

MultiIndex([(1, 11, 21),
            (2, 12, 22),
            (3, 13, 23)],
           names=['level1', 'level2', 'level3'])

eg:
MultiIndex([('mammal',   'cat'),
            ('mammal',   'dog'),
            ('mammal',  'goat'),
            ('mammal', 'human')],
           names=['Type', 'Animal'])


MultiIndex.from_product
----------------------
data = [[0, 1, 2], ['green', 'purple']]
data = [(0, 1, 2), ('green', 'purple')]**
data = ([0, 1, 2], ['green', 'purple'])
data = ((0, 1, 2), ('green', 'purple'))
pd.MultiIndex.from_product( data ,names=['number', 'color'])

MultiIndex([(0,  'green'),
            (0, 'purple'),
            (1,  'green'),
            (1, 'purple'),
            (2,  'green'),
            (2, 'purple')],
           names=['number', 'color'])