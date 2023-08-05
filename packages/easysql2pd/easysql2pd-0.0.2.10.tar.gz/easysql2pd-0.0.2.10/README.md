# JT

#example

#!!!must import as  "es"!!!

import easysql2pd as es

import pandas as pd

import numpy as np



aa = pd.DataFrame(np.arange(2))

xx = pd.DataFrame(np.arange(3))

bb = eval(es.SQL('''select 'aa' as tbl ,count(*) as cnt from aa 
        union all 
        select 'xx' as tbl, count(*) as cnt from xx '''))

print(bb)
