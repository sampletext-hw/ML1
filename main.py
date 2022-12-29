import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file = "data_182.csv"
df = pd.read_csv(file, delimiter=',', parse_dates=['date'])
print(df.columns)

qq = df[df['letter_code'] == "NOK"]
gg = qq[qq['date'] > "1998-09-28"]

sns.lineplot(data=gg, x=gg['date'], y=gg['rate'])
plt.show()
