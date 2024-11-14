#My Add-On
speeds.groupby('class')['order'].value_counts()
speeds.groupby('class')['max_speed'].min()
speeds.groupby('class')['max_speed'].max()
speeds.groupby('class')['max_speed'].agg(['sum','min','max','median','mean'])
speeds.groupby('class')['max_speed'].aggregate(['sum','min','max','median','mean'])
speeds.groupby('class').all()
speeds.groupby('class').any()
speeds.groupby('class')['max_speed'].apply(lambda x :x.sum())
speeds.groupby('class').count()
speeds.groupby('class').first()
speeds.groupby('class').last()
speeds.groupby('class').ndim
speeds.groupby('class').size()
speeds.groupby('class').take([0])
speeds.groupby('class').head(1)
speeds.groupby('class').tail(1)
speeds.groupby('class')['max_speed'].sum()
speeds.groupby('class')['max_speed'].std()
speeds.groupby('class')['max_speed'].var()
speeds.groupby('class')['max_speed'].nth(1)
speeds.groupby('class')['order'].nunique()
speeds.groupby('class').describe()
speeds.groupby('class').ngroups              #total groups 
speeds.groupby('class').groups               #{'group0': ['index1 positions of group0], 'group1': ['index positions of group1] ...]
speeds.groupby('class').ngroup()             #[index0 - group Nr [index1 - group Nr] [index2 - group Nr] .......
speeds.groupby('class').get_group('bird')
speeds.groupby('class')['max_speed'].idxmax()
speeds.groupby('class')['max_speed'].idxmin()
speeds.groupby('class').indices               #{'bird': array([0, 1]), 'mammal': array([2, 3, 4]), 'mammal1': array([5, 6, 7])}
speeds.groupby('class').corr()
speeds.groupby('class').prod()                #Product of each group
df.groupby('class')['max_speed'].bfill()      # Fill NaN with next value
df.groupby('class')['max_speed'].ffill()      #Fill  NaN with Prev value
speeds.groupby('class')['max_speed'].fillna(1000)


#Built-in aggregation methods
Method
any()        -> Compute whether any of the values in the groups are truthy
all()        -> Compute whether all of the values in the groups are truthy
count()      -> Compute the number of non-NA values in the groups
cov()        -> Compute the covariance of the groups
first()      -> Compute the first occurring value in each group
idxmax()     -> Compute the index of the maximum value in each group
idxmin()     -> Compute the index of the minimum value in each group
last()       -> Compute the last occurring value in each group
max()        -> Compute the maximum value in each group
mean()       -> Compute the mean of each group
median()     -> Compute the median of each group
min()        -> Compute the minimum value in each group
nunique()    -> Compute the number of unique values in each group
prod()       -> Compute the product of the values in each group
quantile()   -> Compute a given quantile of the values in each group
sem()        -> Compute the standard error of the mean of the values in each group
size()       -> Compute the number of values in each group
skew()       -> Compute the skew of the values in each group
std()        -> Compute the standard deviation of the values in each group
sum()        -> Compute the sum of the values in each group
var()        -> Compute the variance of the values in each group
agg          -> 
aggregate    -> 
apply        -> 
bfill        -> 
boxplot      -> 
corr         -> 
corrwith     -> 
cumcount     -> 
cummax       -> 
cummin       -> 
cumprod      -> 
cumsum       -> 
describe     -> 
diff         -> 
dtypes       -> 
ewm          -> 
expanding    -> 
ffill        -> 
fillna       -> 
filter       -> 
get_group    -> 
groups       -> 
head         -> 
hist         -> 
indices      -> 
ndim         -> 
ngroup       -> 
ngroups      -> 
nth          -> 
ohlc         -> 
pct_change   -> 
pipe         -> 
plot         -> 
rank         -> 
resample     -> 
rolling      -> 
sample       -> 
shift        -> 
tail         -> 
take         -> 
transform    -> 
value_counts -> 
weight       -> 
