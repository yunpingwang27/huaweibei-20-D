# 本文主要对碳排放总量等数据进行条形图与折线图分段绘制，以分析其总量与变化趋势。
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

def draw_5(title,years,total_values):
    # plt.figure(figsize=(10, 6))  # 设置图表大小
    plt.plot(years, total_values, marker='o', linestyle='-', color='#1f77b4', markersize=6, linewidth=3)  # 绘制折线图
    plt.title(title,fontsize = 16)  # 设置标题
    plt.xlabel('年份',fontsize = 14)  # 设置x轴标签
    plt.ylabel('总量(万tCO2)',fontsize = 14)  # 设置y轴标签
    plt.xticks(years, fontsize=16)
    plt.yticks(fontsize = 17)
    # 添加数据点标签
    for i in range(len(years)):
        plt.text(years[i], total_values[i], f'{total_values[i]:.2f}', ha='right', va='bottom')

    plt.grid(True,alpha = 0.5)  # 添加网格线

def draw_dual_plot(title,title1, years1, total_values1, title2, years2, total_values2):
    plt.figure(figsize=(16, 6))  # 设置整个图表的大小

    # 绘制第一个子图（左侧）
    ax1 = plt.subplot(1, 2, 1)
    draw_5(title1, years1, total_values1)
    labels = ['(a)','(b)']
    plt.text(-0.1, 1.05, labels[0], transform=ax1.transAxes, fontsize=18, fontweight='bold')

    # 绘制第二个子图（右侧）
    ax2 = plt.subplot(1, 2, 2)
    draw_5(title2, years2, total_values2)
    plt.text(-0.1, 1.05, labels[1], transform=ax2.transAxes, fontsize=18, fontweight='bold')

    # plt.legend([title1, title2], prop=font, loc='upper left')
    plt.tight_layout()  # 调整子图布局，防止重叠
    plt.savefig(title+'.png')  # 保存整个图表为PDF文件
    plt.close()  # 关闭图表窗口
years1 = [int(column) for column in first_row.index[1:7]]
total_values1 = list(first_row[1:7])
years2= [int(column) for column in first_row.index[7:13]]
total_values2 = list(first_row[7:13])
draw_dual_plot('十二五-十三五碳排放总量折线图','十二五期间碳排放总量折线图', years1, total_values1, '十三五期间碳排放总量折线图', years2, total_values2)

second_row = df.iloc[1]
years1 = [column for column in second_row.index[1:7]]
total_values1 = list(second_row[1:7])
years2 = [column for column in second_row.index[7:13]]
total_values2 = list(second_row[7:13])
draw_dual_plot('2010-2020农林消费部门碳排放量折线图','2010-2015年农林消费部门碳排放量折线图', years1, total_values1, '2015-2020年农林消费部门碳排放量折线图', years2, total_values2)
second_row = df.iloc[2]

years1 = [column for column in second_row.index[1:7]]
total_values1 = list(second_row[1:7])
years2 = [column for column in second_row.index[7:13]]
total_values2 = list(second_row[7:13])
draw_dual_plot('2010-2020年工业消费部门碳排放量折线图','2010-2015年工业消费部门碳排放量折线图', years1, total_values1, '2015-2020年工业消费部门碳排放量折线图', years2, total_values2)

second_row = df.iloc[3]
years1 = [column for column in second_row.index[1:7]]
total_values1 = list(second_row[1:7])
years2 = [column for column in second_row.index[7:13]]
total_values2 = list(second_row[7:13])
draw_dual_plot('2010-2020年第三产业消费部门碳排放量折线图','2010-2015年第三产业消费部门碳排放量折线图', years1, total_values1, '2015-2020年第三产业消费部门碳排放量折线图', years2, total_values2)

second_row = df.iloc[4]
years1 = [column for column in second_row.index[1:7]]
total_values1 = list(second_row[1:7])
years2 = [column for column in second_row.index[7:13]]
total_values2 = list(second_row[7:13])
draw_dual_plot('2010-2020年交通消费部门碳排放量折线图','2010-2015年交通消费部门碳排放量折线图', years1, total_values1, '2015-2020年交通消费部门碳排放量折线图', years2, total_values2)

second_row = df.iloc[5]
years1 = [column for column in second_row.index[1:7]]
total_values1 = list(second_row[1:7])
years2 = [column for column in second_row.index[7:13]]
total_values2 = list(second_row[7:13])
draw_dual_plot('2010-2020年建筑消费部门碳排放量折线图','2010-2015年建筑消费部门碳排放量折线图', years1, total_values1, '2015-2020年建筑消费部门碳排放量折线图', years2, total_values2)


second_row = df.iloc[6]
years1 = [column for column in second_row.index[1:7]]
total_values1 = list(second_row[1:7])
years2 = [column for column in second_row.index[7:13]]
total_values2 = list(second_row[7:13])
draw_dual_plot('2010-2020年居民生活消费碳排放量折线图','2010-2015年居民生活消费碳排放量折线图', years1, total_values1, '2015-2020年居民生活消费碳排放量折线图', years2, total_values2)



years = [column for column in first_row.index[1:13]]
total_values = list(first_row[1:13])

# 创建柱状图
plt.figure(figsize=(12, 6))  # 调整图表大小
plt.ylim(50000, 80000)
plt.bar(years, total_values, color='skyblue', width=0.6, edgecolor='navy', linewidth=1.5)  # 调整颜色和样式，增加宽度和边框
plt.xticks(years, years,fontsize=17)  # 调整X轴标签字体大小
plt.yticks(fontsize=17)
plt.title('2010-2020年碳排放总量柱状图', fontweight='bold',fontsize=16)  # 调整标题样式
plt.xlabel('年份', fontsize=16)  # 调整标签字体大小
plt.ylabel('总量（万tCO2）', fontsize=16)
# 添加数据点标签
for i in range(len(years)):
    plt.text(years[i], total_values[i] + 5, f'{total_values[i]:.2f}', ha='center', va='bottom', fontsize = 14, fontweight='bold')

plt.grid(axis='y', linestyle='--', alpha=0.7)  # 调整网格线样式和透明度

# 添加图例
plt.legend(['总量（万tCO2）'], loc='upper left',fontsize = 16)

plt.tight_layout()  # 调整布局以防止标签被裁剪
# plt.show()  # 显示图表
plt.savefig('2010-2020年碳排放总量柱状图.png')


