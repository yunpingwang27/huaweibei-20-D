# 本文利用OLS估计建立模型,初步拟合三种指标对碳排放量的关系 
import pandas as pd
from sklearn.linear_model import LinearRegression
# 假设你有三个或更多组数据
import statsmodels.api as sm
excel_file = './数据表汇总/经济与能源拆分表.xlsx'
xls = pd.ExcelFile(excel_file)
# 通过Sheet名称或者索引来选择第二个Sheet，这里使用Sheet名称作为示例
sheet_name = xls.sheet_names[4]  # 第二个Sheet的名称，索引从0开始
df = pd.read_excel(excel_file, sheet_name=sheet_name,usecols=list(range(1,12)))

df.loc[4] = df.iloc[2]/df.iloc[1]
df.loc[5] = df.iloc[1]/df.iloc[0]
X= df.iloc[[0, 4, 5]].T

# 添加截距项（常数项）到X

# 创建因变量（碳排放量）
y = df.iloc[3,]

# 创建因变量（碳排放量）

model = LinearRegression()

# 拟合模型
model.fit(X, y)

# 查看回归系数和截距
coefficients = model.coef_
intercept = model.intercept_
print(coefficients)
print(intercept)
s = coefficients[0]/df.iloc[0,].var()
print(s)

X = sm.add_constant(X)


# 使用最小二乘法进行多元线性回归
model = sm.OLS(y, X).fit()

# 输出回归结果摘要
print(model.summary())
