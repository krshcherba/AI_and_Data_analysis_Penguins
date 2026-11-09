import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px	# для 3d диаграммы
# from scipy.stats import levene

df = pd.read_csv('penguins.csv')

df.head()	# первые строки
df.shape	# количество строк и столбцов
df.info()	# тип данных и количество непустых значений
df.describe()	# статистика по числовым столбцам

print(df.isnull().sum())	# проверка пропущенных значений

print(df['species'].value_counts())	# количество пингвинов каждого вида
print(df.groupby('species').mean(numeric_only=True))	# средние значения числовых признаков для каждого вида

print(df.duplicated().sum())	# дубликаты

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

print(df.groupby('species')[
	['bill_length_mm',
	 'bill_depth_mm',
	 'flipper_length_mm',
	 'body_mass_g']
].agg(['mean', 'std', 'median', 'min', 'max']))	# среднее, стандартное отклонение, медиана, минимум и максимум по указан
# ным параметрам каждого из видов


# диаграммы
features = [
    "bill_length_mm",
    "bill_depth_mm",
    "flipper_length_mm",
    "body_mass_g"
]

for feature in features:
    plt.figure(figsize=(8, 4))
    sns.boxplot(data=df, x="species", y=feature)
    plt.title(feature)
    plt.show()


# 3d диаграмма облаков
df_plot = df.dropna(subset=[
    'bill_length_mm',
    'bill_depth_mm',
    'flipper_length_mm',
    'species'
])

fig = px.scatter_3d(
    df_plot,
    x='bill_length_mm',
    y='bill_depth_mm',
    z='flipper_length_mm',
    color='species',
    hover_data=['island', 'body_mass_g'],
    title='Penguin species: 3D scatter plot'
)

fig.show()