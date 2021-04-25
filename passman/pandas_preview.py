#!/usr/bin/env python3

import pandas as pd
# with open('file') as file:

col_head = ['url','username','password','extra','name','grouping','fav']
data_set = ['s1','s2','s3','s4','s5','s6','s7']
df = pd.DataFrame(columns=col_head,dtype=str)
df.data = data_set
print(df)    
input('Press ENTER to exit')
