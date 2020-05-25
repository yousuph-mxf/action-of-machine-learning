import pandas as pd
import matplotlib.pyplot as plt
unrate=pd.read_csv('UNRATE.csv')
print(unrate.head(12))
first_twelve=unrate[0:12]
plt.plot(first_twelve['DATE'],first_twelve['VALUE'])
plt.xticks(rotation=45)
plt.xlabel('month')
plt.ylabel('unemployment rate')
plt.title('失业率')
plt.show()
