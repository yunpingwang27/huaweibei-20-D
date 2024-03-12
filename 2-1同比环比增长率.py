# 本代码主要计算'常驻人口','区域生产总值','能源消耗量','碳排放量'四种指标的同比与环比的增长率并绘制折线图
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.font_manager import FontManager

mpl_fonts = set(f.name for f in FontManager().ttflist)
plt.rcParams['axes.unicode_minus'] = False # 用来正常显示负号

# 指定Excel文件路径
excel_file = './数据表汇总/经济与能源拆分表.xlsx'

# 使用pandas读取Excel文件
xls = pd.ExcelFile(excel_file)

# 通过Sheet名称或者索引来选择第二个Sheet，这里使用Sheet名称作为示例
sheet_name = xls.sheet_names[4]  # 第二个Sheet的名称，索引从0开始

# 使用pandas读取第二个Sheet的数据
df = pd.read_excel(excel_file, sheet_name=sheet_name,usecols=range(12))
print(df.iloc[:,0])
df = df.iloc[:,1:]


first_row = df.iloc[0]

# 计算同比增长率
def calculate_year_on_year_growth(data, period):
    year_on_year_growth = (data / data.shift(3)) - 1
    return year_on_year_growth

# 计算环比增长率
def calculate_quarter_on_quarter_growth(data):
    quarter_on_quarter_growth = (data / data.shift(1)) - 1
    return quarter_on_quarter_growth


# 选择数据，假设您要计算第一行的同比和环比增长率
data_to_calculate = df.T

# 计算同比增长率，周期为3
year_on_year_growth = calculate_year_on_year_growth(data_to_calculate, period=3)

# 计算环比增长率
quarter_on_quarter_growth = calculate_quarter_on_quarter_growth(data_to_calculate)

# 打印结果
print("同比增长率:")
print(year_on_year_growth.iloc[3:,1])
print("环比增长率:")
print(quarter_on_quarter_growth)

color_list = ['#1f77b4', '#ff7f0e', '#2ca02c','darkviolet','darkviolet']
plt.figure(figsize=(16, 6))
label = ['常驻人口','区域生产总值','能源消耗量','碳排放量']
# 绘制折线图，每条折线的颜色由color_list指定
for i in range(4):
    plt.subplot(1, 2, 1)
    plt.xlabel('年份',fontsize = 16)  # 设置x轴标签
    plt.ylabel('同比增长率（%）',fontsize = 16)  # 设置y轴标签
    plt.xticks(fontsize=17)
    plt.yticks(fontsize=17)
    plt.plot(year_on_year_growth.iloc[3:,i], marker='o', linestyle='-', color=color_list[i], label=label[i],linewidth = 2.5)
    plt.title('同比增长率（%）',fontsize = 16)
    plt.grid(True,alpha = 0.5)  # 添加网格线
    plt.subplot(1, 2, 2)
    plt.xticks(fontsize=17)
    plt.yticks(fontsize=17)
    plt.xlabel('年份',fontsize = 16)  # 设置x轴标签
    plt.ylabel('环比增长率',fontsize = 16)  # 设置y轴标签
    plt.plot(quarter_on_quarter_growth.iloc[1:,i], marker='o', linestyle='-', color=color_list[i], label=label[i],linewidth = 2.5)
    plt.title('环比增长率',fontsize = 16)
plt.legend()
plt.grid(True)  # 添加网格线
plt.savefig('同比环比增长率.png')
year_on_year_growth.to_csv('year_on_year.csv',float_format='%.4f')

quarter_on_quarter_growth.to_csv('quarter.csv', float_format='%.4f')
