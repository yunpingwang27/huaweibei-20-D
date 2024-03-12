# 本代码对碳排放总量的变化进行季节性分析
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['axes.unicode_minus'] = False # 用来正常显示负号

# 指定Excel文件路径
excel_file = './数据表汇总/碳排放拆分表.xlsx'

# 使用pandas读取Excel文件
xls = pd.ExcelFile(excel_file)

# 通过Sheet名称或者索引来选择第二个Sheet，这里使用Sheet名称作为示例
sheet_name = xls.sheet_names[0]  # 第二个Sheet的名称，索引从0开始

columns = list(range(12))
# 使用pandas读取第二个Sheet的数据
df = pd.read_excel(excel_file, sheet_name=sheet_name,usecols=columns)

# 现在，变量df包含了第二个Sheet的数据
# print(df)


# 获取总量
first_row = df.iloc[0]
# df_value = df[1:13]
# print(df_value)
data_1 = df.iloc[:, 1:]
row_means = data_1.mean(axis=1)
print(row_means)


# 进行季节性分析

years = [column for column in first_row.index[1:13]]
total_values = list(first_row[1:13])

import statsmodels.api as sm

# 执行STL分解
stl_result = sm.tsa.seasonal_decompose(total_values, model='additive', period=5)

# 获取分解后的结果
trend = stl_result.trend
seasonal = stl_result.seasonal
residual = stl_result.resid
print(trend)
print(seasonal)
print(residual)
import matplotlib.pyplot as plt

years = [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]
# 获取分解后的结果
trend = stl_result.trend
seasonal = stl_result.seasonal
residual = stl_result.resid

# 创建一个子图来可视化分解结果
plt.figure(figsize=(6, 6))

# 可视化趋势成分
plt.subplot(311)
plt.plot(years,trend)
plt.title('趋势成分')

# 可视化季节性成分
plt.subplot(312)
plt.plot(years,seasonal)
plt.title('季节性成分')

# 可视化残差成分
plt.subplot(313)
plt.plot(years,residual)
plt.title('残差成分')

# 调整子图之间的间距
plt.tight_layout()

# 显示图形
plt.savefig('碳排放季节性分析.png')
# plt.show()

