# 本篇绘制出2010-2020年的各部门碳排放折线图，与各部门平均碳排放占比扇形图
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['axes.unicode_minus'] = False # 用来正常显示负号

# 指定Excel文件路径
excel_file = './数据表汇总/碳排放拆分表.xlsx'

# 使用pandas读取Excel文件
xls = pd.ExcelFile(excel_file)

# 通过Sheet名称或者索引来选择第二个Sheet，这里使用Sheet名称作为示例
sheet_name = xls.sheet_names[0]  # 第二个Sheet的名称，索引从0开始

# 使用pandas读取第二个Sheet的数据
columns = list(range(12))
df = pd.read_excel(excel_file, sheet_name=sheet_name,usecols=columns)

# 现在，变量df包含了第二个Sheet的数据


# 获取总量
first_row = df.iloc[0]

def draw_5(title,data):
    # 获取分部门碳排放数据
    first_row = data.iloc[1]
    years2 = [column for column in first_row.index[1:]]
    total_values2 = list(first_row)[1:]
    first_row = data.iloc[2]
    first_row = data.iloc[4]
    years4 = [column for column in first_row.index[1:]]
    total_values4 = list(first_row)[1:]
    first_row = data.iloc[5]
    years5 = [column for column in first_row.index[1:]]
    total_values5 = list(first_row)[1:]
    first_row = data.iloc[6]
    years6 = [column for column in first_row.index[1:]]
    total_values6 = list(first_row)[1:]
    
    color = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
    # 绘制各部门碳排放折线图
    plt.plot(years2, total_values2, marker='o', linestyle='-', color=color[0],label = '农林消费部门',markersize=6, linewidth=4)  # 绘制折线图
    plt.plot(years4, total_values4, marker='o', linestyle='-', color=color[1],label='交通消费部门',markersize=6, linewidth=3)  # 绘制折线图
    plt.plot(years5, total_values5, marker='o', linestyle='-', color=color[2],label='建筑消费部门',markersize=6, linewidth=3)  # 绘制折线图
    plt.plot(years6, total_values6, marker='o', linestyle='-', color=color[3],label='居民生活消费部门',markersize=6, linewidth=3)  # 绘制折线图
     
    plt.title(title,fontsize = 18)  # 设置标题
    plt.xlabel('年份',fontsize = 16)  # 设置x轴标签
    plt.ylabel('总量(万tCO2)',fontsize = 16)  # 设置y轴标签
    # 设立x轴刻度大小
    plt.xticks(years2,fontsize = 17)
    plt.yticks(fontsize = 17)

    # print(total_values2)
    # print(years2)
    plt.grid(True,alpha = 0.5)  # 添加网格线
def draw_dual_plot(title):
    plt.figure(figsize=(17,9))  # 设置整个图表的大小
    # 绘制图形
    draw_5(title, df)
    plt.legend(fontsize = 14,loc='best')
    plt.savefig(title+'.png',bbox_inches='tight')  # 保存整个图表
    plt.close()  # 关闭图表窗口

# 绘制图表
draw_dual_plot('2010-2020年各部门碳排放折线图')

# 绘制各部门碳排放占比扇形图

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

# 获取总量
first_row = df.iloc[0]
data_1 = df.iloc[:, 1:]
row_means = data_1.mean(axis=1)
print(row_means)
import matplotlib.pyplot as plt

# 数据
labels = ['农林消费部门', '工业消费部门', '交通消费部门', '建筑消费部门', '居民生活消费']
sizes = [1141.095166, 51983.922217, 4338.789657, 4226.376124, 5940.981325]

# 颜色
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# 扇形图
fig1, ax1 = plt.subplots(figsize = (8,8))

# 设置百分比标签的字体大小和样式
font_props = {'fontsize': 16, 'fontweight': 'bold', }


# 绘制扇形图
ax1.pie(sizes, colors=colors, autopct='%1.1f%%', textprops=font_props, startangle=90)
ax1.axis('equal')  # 保持纵横比一致


# 添加图例
plt.legend(labels, loc="lower right",fontsize = 16)

# 图表标题
plt.title('碳排放总量分布',fontsize = 16)

plt.savefig('各部门碳排放分布.png')