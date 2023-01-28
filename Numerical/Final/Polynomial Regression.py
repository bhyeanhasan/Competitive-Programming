import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

data = pd.read_csv('data.csv')


x = data.iloc[:,0:1]
y = data.iloc[:,1]

print(x)

# model = LinearRegression().fit(x,y)
# print(model.predict(x))
# print(model.predict(np.array([[10]])))

poly_x = PolynomialFeatures(degree=3).fit_transform(x)

model = LinearRegression().fit(poly_x, y)

# print(model.predict(poly_x))
# print(model.intercept_)
# print(model.coef_)

plt.scatter(x, y)
plt.plot(x, model.predict(poly_x))
plt.show()

# print(model.predict(PolynomialFeatures(degree=2).fit_transform(np.array([[9]]))))
