# 通过灰度自记忆模型与SVR算法根据人口与经济情况预测能源消耗,配合arima算法进行预测
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
# from scipy.stats import pearsonr,spearmanr,kendalltau
# 假设你有三个或更多组数据
import statsmodels.api as sm
# import numpy as np

import pandas as pd
excel_file = './数据表汇总/经济与能源拆分表.xlsx'
xls = pd.ExcelFile(excel_file)
# 通过Sheet名称或者索引来选择第二个Sheet，这里使用Sheet名称作为示例
sheet_name = xls.sheet_names[4]  # 第二个Sheet的名称，索引从0开始
df = pd.read_excel(excel_file, sheet_name=sheet_name)
# print(df)
label = df.iloc[:,0]
# print(label)
df = df.iloc[:,1:]
sf = pd.DataFrame()
sf['常驻人口'] = df.iloc[0,:]
sf['地区生产总值'] = df.iloc[1,:]
sf['能源消费量'] = df.iloc[2,:]
sf['碳排放量'] = df.iloc[3,:]

# 假设你已经有了包含数据的DataFrame df

# 提取时间序列数据
energy_consumption = sf['能源消费量']
population = sf['常驻人口']
gdp = sf['地区生产总值']

# 计算累加生成序列
cumulative_energy = energy_consumption.cumsum()
cumulative_population = population.cumsum()
cumulative_gdp = gdp.cumsum()
t = 1
a = 1
b = 1
c = 1
def get_cumulative(a,b,c,t):
    F_yt = -a*list(cumulative_energy)[t] + b*list(cumulative_population)[t]+ c*list(cumulative_gdp)[t]
        # 
    return F_yt
f_yt = get_cumulative(a,b,c,t)
z = pd.DataFrame()
energy = list(energy_consumption)
z_minus = []
z_plus = []
cumulative_gr = []
for i in range(1,11):
    value = energy[t]
    value_plus = energy[t+1]
    value_minus = energy[t-1]
    value_plus_1 = list(cumulative_energy)[t+1]
    value_1 = list(cumulative_energy)[t]
    z_plus.append((value_plus+value)/2)
    z_minus.append((value-value_minus)/2)
    cumulative_gr.append(value_plus_1 - value_1)
from sklearn.svm import SVR
# columns = ["energy", "gdp", "population"]
columns = list(range(2010,2021))
r = pd.DataFrame(columns=columns)
# print(list(cumulative_energy))
r.loc[0] = list(cumulative_energy)
r.loc[1] = list(cumulative_gdp)
r.loc[2] = list(cumulative_population)
# import numpy as np
# print(r)
import statsmodels.api as sm
X = r.iloc[:,1:].T
y = cumulative_gr
# 使用最小二乘法进行多元线性回归
# 输出回归结果摘要
model = sm.OLS(y, X).fit()
# print(model.summary())
# print(model.params)
param = model.params
# print(param[0])
def z_01(y):
    z_0 = []
    z_1 = []
    for t in range(11):
        if t == 0:
            z_0.append(0)
        else:
            z_0.append((y[t-1]+y[t])/2)
        if t == 10:
            z_1.append(0)
        else:
            z_1.append((y[t+1]+y[t])/2)
    return z_0,z_1
y = energy
z_0,z_1 = z_01(y)
# 进行预测
f_yt = []
for i in range(11):
    f_yt.append(get_cumulative(param[0],param[1],param[2],t=i))

f_yt_1 = []
for i in range(1,11):
    f_yt_1.append(f_yt[i-1])
f_yt_1.append(0)
columns = list(range(2010,2021))
rs = pd.DataFrame(columns=columns)

rs.loc[0] = list(z_0)
rs.loc[1] = list(z_1)
rs.loc[2] = f_yt
rs.loc[3] = f_yt_1
X = rs.T
model = sm.OLS(y, X).fit()
predictions = model.predict(X)
y = energy
from statsmodels.tsa.arima.model import ARIMA


# 创建ARIMA模型
model = ARIMA(sf['地区生产总值'],order=(1,1,1))

# 拟合模型
model_fit = model.fit()

# 进行预测
forecast_steps = 6  # 你可以根据需要选择预测的时间步长
gdp_forecast = model_fit.forecast(steps=forecast_steps)
svr = pd.DataFrame(columns=columns)
svr.loc[0] = sf['地区生产总值']
svr.loc[1] = sf['常驻人口']
svr.loc[2] = list(predictions)
model = ARIMA(sf['常驻人口'],order=(1,1,1))
model_fit = model.fit()
pop_forecast = model_fit.forecast(steps = forecast_steps)

model = ARIMA(list(predictions),order=(1,1,1))
model_fit = model.fit()
predict_fore = model_fit.forecast(steps = forecast_steps)
print(list(predictions))
model = ARIMA(sf['能源消费量'],order=(1,1,1))
model_fit = model.fit()
predict_en = model_fit.forecast(steps = forecast_steps)

X = svr.T

svr_rbf = SVR(kernel='rbf', C=1000, gamma=0.1, epsilon=.5)
svr_rbf.fit(X,y)

y_pred = svr_rbf.predict(X)
list1 = list(svr.iloc[0])+list(gdp_forecast)
list2 = list(svr.iloc[1])+list(pop_forecast)
list3 = list(svr.iloc[2])+list(predict_fore)

predict_x = pd.DataFrame(columns=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
predict_x.loc[0] = list1
predict_x.loc[1] = list2
predict_x.loc[2] = list3
X = predict_x.T
y = energy+list(predict_en)
svr_rbf.fit(X,y)
result = svr_rbf.predict(predict_x.T.values.tolist())


s = pd.DataFrame(columns=[0,1,2,3])
s[0] = energy
s[1] = list(predictions)
s[2] = result
