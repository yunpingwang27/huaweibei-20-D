# 本文主要分析人口，GDP、能源消耗量这三种指标与碳排放量的相关性，
# 1.绘制散点图与拟合直线；
# 2.求出三种相关系数
# 3.进行OLS最小二乘法拟合

import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import pearsonr,spearmanr,kendalltau
import statsmodels.api as sm

# 指定Excel文件路径
excel_file = './数据表汇总/经济与能源拆分表.xlsx'
xls = pd.ExcelFile(excel_file)
sheet_name = xls.sheet_names[4]  # 第二个Sheet的名称，索引从0开始
df = pd.read_excel(excel_file, sheet_name=sheet_name,usecols=list(range(1,12)))
first_row = df.iloc[0]
second_row =  df.iloc[1]
# print(df)

third_row =  df.iloc[2]
y_row = df.iloc[3]

X = df.iloc[:3].T  # 选择前三行，并进行转置，使每行代表一个观测值



# 绘制散点图
line_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

slope_1, intercept_1, r_value_1, p_value_1, std_err_1 = stats.linregress(first_row, y_row)
slope_2, intercept_2, r_value_2, p_value_2, std_err_2 = stats.linregress(second_row, y_row)
slope_3, intercept_3, r_value_3, p_value_3, std_err_3 = stats.linregress(third_row, y_row)
plt.figure(figsize=(8, 6))
plt.title('相关指标与碳排放散点图',fontsize = 16)
plt.scatter(first_row, y_row, label='常驻人口', alpha=0.8,s = 40,c = line_colors[0])
plt.scatter(second_row, y_row, label='地区生产总值',alpha=0.8,s = 40,c = line_colors[1])
plt.scatter(third_row, y_row, label='能源消费量',alpha=0.8,s = 40,c = line_colors[2])
plt.plot(first_row, slope_1 * first_row + intercept_1, color='darkred', label='拟合直线(常驻人口)',linewidth=2.5)
plt.plot(second_row, slope_2 * second_row + intercept_2, color='green', label='拟合直线 (地区生产总值)',linewidth=2.5)
plt.plot(third_row, slope_3 * third_row + intercept_3, color='blue', label='拟合直线 (能源消费量)',linewidth=2.5)
# 添加标签和图例
plt.xlabel('相关指标',fontsize = 16)
plt.ylabel('碳排放量(万tCO2)',fontsize = 16)
plt.xticks(fontsize = 16)
plt.yticks(fontsize = 16)
plt.legend(fontsize = 14)

# 显示图形
plt.savefig('相关性散点图.png')


# 计算三种相关系数情况
df.loc[4] = df.iloc[2]/df.iloc[1]
df.loc[5] = df.iloc[1]/df.iloc[0]
for i in [0,1,2,4,5]:
    correlation_coefficient, p_value = pearsonr(df.iloc[i],y_row)
    correlation_coefficient2,p_value2 = spearmanr(df.iloc[i], y_row)
    tau, p_value3 = kendalltau(df.iloc[i], y_row)
    print(f"{tau:.4f}",f"{p_value3:.6f}")
    print(f"{correlation_coefficient:.4f}", f"{p_value:.6f}") 
    print(f"{correlation_coefficient2:.4f}", f"{p_value2:.6f}")


# 使用OLS法进行线性拟合
# 添加截距项（常数项）到X
X = sm.add_constant(X)

# 创建因变量（碳排放量）
y = df.iloc[3]

# 使用最小二乘法进行多元线性回归
model = sm.OLS(y, X).fit()

# 输出回归结果摘要
print(model.summary())
