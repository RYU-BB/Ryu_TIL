import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

df = pd.DataFrame({
    'x1': np.random.chisquare(8, 1000),
    'x2': np.random.beta(8, 2, 1000) * 40,
    'x3': np.random.normal(50, 3, 1000)
})

df.plot.kde(title = "before StandardScaler")

standard_scaler = StandardScaler()
data_transform = standard_scaler.fit_transform(df)
df = pd.DataFrame(data_transform, columns=['x1','x2','x3'])

df.plot.kde(title = "after StandardScaler")