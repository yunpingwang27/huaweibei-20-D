# 通过XGBoost和GBDT构建模型，进行评估后计算SHAP值，以评估各指标对碳排放量的贡献 
import shap
import matplotlib.pyplot as plt
# plt.rcParams["font.sans-serif"]=["SimHei"] #设置字体
plt.rcParams["axes.unicode_minus"]=False #该语句解决图像中的“-”负号的乱码问题

import pandas as pd

excel_file = './数据表汇总/经济与能源拆分表.xlsx'
xls = pd.ExcelFile(excel_file)
# 通过Sheet名称或者索引来选择第二个Sheet，这里使用Sheet名称作为示例
sheet_name = xls.sheet_names[4]  # 第二个Sheet的名称，索引从0开始
df = pd.read_excel(excel_file, sheet_name=sheet_name)
data = df.T

# 将第一行作为列名
new_header = data.iloc[0] # 将第一行作为新的列名
data = data[1:] # 删除第一行
data.columns = new_header # 将列名设置为新的列名

data.reset_index().columns


data=pd.DataFrame(data.reset_index().values,columns=['年份', '人口(万人)', '生产总值-GDP总量(亿元)','能源消费量（万tce）','碳排放量（万tCO2）' ])


import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor, GradientBoostingRegressor
from lightgbm import LGBMRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
from math import sqrt
# 分离X和Y
X = data[['人口(万人)', '生产总值-GDP总量(亿元)', '能源消费量（万tce）']]
Y = data['碳排放量（万tCO2）']
print(X)



for i in X.columns:
    X[i]=X[i].map(float)

Y=Y.map(float)

# 构建xgboost回归模型
xgb_model = xgb.XGBRegressor(n_estimators=100, max_depth=3, learning_rate=0.1, random_state=42)
xgb_model.fit(X, Y)
xgb_y_pred = xgb_model.predict(X)

# 输出xgboost模型评价结果
print('XGBoost模型评价结果：')
print('R2 Score:', r2_score(Y, xgb_y_pred))
print('MAE:', mean_absolute_error(Y, xgb_y_pred))
print('MSE:', mean_squared_error(Y, xgb_y_pred))
print('RMSE:', sqrt(mean_squared_error(Y, xgb_y_pred)))

# 构建GBDT回归模型
gbdt_model = GradientBoostingRegressor(n_estimators=100, max_depth=3, learning_rate=0.1, random_state=42)
gbdt_model.fit(X, Y)
gbdt_y_pred = gbdt_model.predict(X)

# 输出GBDT模型评价结果
print('GBDT模型评价结果：')
print('R2 Score:', r2_score(Y, gbdt_y_pred))
print('MAE:', mean_absolute_error(Y, gbdt_y_pred))
print('MSE:', mean_squared_error(Y, gbdt_y_pred))
print('RMSE:', sqrt(mean_squared_error(Y, gbdt_y_pred)))

# # 可视化模型预测与实际值的比较
fig, ax = plt.subplots(figsize=(10, 8))

# # 绘制散点图
ax.scatter(Y, xgb_y_pred,  c = 'darkblue', label='数据点',s = 60)

# 绘制虚线表示理想情况
ax.plot([min(Y), max(Y)], [min(Y), max(Y)], '--', alpha=0.7, color='darkred', label='理想情况',linewidth = 2.5)
ax.set_xlabel('实际碳排放（万tCO2）', fontsize=16)
ax.set_ylabel('预测碳排放（万tCO2）', fontsize=16)


# 添加图例
ax.legend(fontsize=12)

# 添加标题
plt.title('实际与预测碳排放', fontsize=16)

# 添加网格线
ax.grid(True, linestyle='--', alpha=0.6)

# 调整坐标轴刻度标签字体大小
ax.tick_params(axis='both', labelsize=17)

# 存储图
plt.savefig('shap值.png')


# 初始化SHAP模型
explainer = shap.Explainer(gbdt_model)

# 计算SHAP值
plt.xlabel("SHAP值")
plt.ylabel("特征",fontsize = 16)

shap_values = explainer(X)
plt.xticks(fontsize=20)  # 调整X轴标签字体大小
plt.yticks(fontsize=17)  # 调整Y轴标签字体大小
plt.title("SHAP摘要图", fontsize=18)  # 调整标题字体大小
plt.xlim(0, 1750)

shap.summary_plot(shap_values, X, plot_type='bar',plot_size = [11,4])
plt.savefig('shap摘要图.png')

shap_df = pd.DataFrame(shap_values.values, columns=X.columns)

shap_df.to_excel('shap_df.xlsx')

# 输出每个特征的SHAP值（绝对值）
for i, feature in enumerate(X.columns):
    abs_mean_shap_value = np.abs(shap_df.values[:, i]).mean()
    print(f"{feature}: {abs_mean_shap_value}")

plt.xlabel("SHAP值")
plt.ylabel("特征")

shap.summary_plot(shap_values, X,plot_size=[10,5])


