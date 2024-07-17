import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

# Создание пустого DataFrame для one hot кодирования
one_hot = pd.DataFrame(0, index=data.index, columns=sorted(data['whoAmI'].unique()))

# Заполнение DataFrame
for i, value in enumerate(data['whoAmI']):
    one_hot.at[i, value] = 1

# Соединение исходного DataFrame с one hot кодированием
data = pd.concat([data, one_hot], axis=1)
print(data.head())

# Преобразование столбца в one hot вид с использованием get_dummies
one_hot_get_dum = pd.get_dummies(data['whoAmI'])

# Соединение исходного DataFrame с one hot кодированием
data = pd.concat([data, one_hot_get_dum], axis=1)
