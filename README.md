# Bank-Statement-Parser
High-efficiency workflow for loading, iterating, and analysis of IBM's AML (anti money laundering) dataset. Transaction categorization, anomaly detection, and financial performance are all focal points.

```python
import kagglehub
import pandas as pd
import numpy as np
from collections import Counter

import seaborn as sns
import os

from math import sqrt
import matplotlib.pyplot as plt
import plotly.express as px
```
```python
path = '/kaggle/input/ibm-transactions-for-anti-money-laundering-aml/HI-Small_Trans.csv'
```

```python
df = pd.read_csv(os.path.join(path, "HI-Small_Trans.csv"))
df = pd.DataFrame(df)
df.head()
```

```python
# split the DataFrame into chunks of n size to optimize speed
n = 250000
chunked_list = [df[i:i + n] for i in range(0, len(df), n)]
```

```python
# accessed the first chunk
df1 = chunked_list[0]
df1
```

```python
# need to find a way to store value counts to dict
Payment_Format_Dict = copy['Payment Format'].value_counts().to_dict()

for i in Payment_Format_Dict.items():
    print(i)
```

```python
object_cols = copy.select_dtypes(include=['object']).columns
```

```python
USD = copy.select_dtypes(include='object').copy()
USD = copy[copy['Receiving Currency'] == 'USD Dollar'.copy()
```
```python
for col in USD.columns:
    print(col, USD[col].nunique())
```
