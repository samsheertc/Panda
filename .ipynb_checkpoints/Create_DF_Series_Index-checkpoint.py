DataFrame
---------
pd.DataFrame(dictionary)
d1=[[1,2,3],[11,12,13],[21,22,23]]
d2=[(1,2,3),(11,12,13),(21,22,23)]
d3=([1,2,3],[11,12,13],[21,22,23])
d4=((1,2,3),(11,12,13),(21,22,23))
idx=[1,2,3]
col=['A', 'B', 'C']
pd.DataFrame(data=d1,index=idx,columns=col)

Series
------
idx=['a','b','c']
d1 = [1,2,3]
d2 = (1,2,3)
pd.Series(data=d1,index=idx)


MultiIndex
----------
d1=[[1,2,3],[11,12,13],[21,22,23]]
d2=[(1,2,3),(11,12,13),(21,22,23)] ****
d3=([1,2,3],[11,12,13],[21,22,23])
d4=((1,2,3),(11,12,13),(21,22,23))
pd.MultiIndex.from_arrays(d1)

eg:
MultiIndex([('mammal',   'cat'),
            ('mammal',   'dog'),
            ('mammal',  'goat'),
            ('mammal', 'human')],
           names=['Type', 'Animal'])


MultiIndex.from_product
-----------------------
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