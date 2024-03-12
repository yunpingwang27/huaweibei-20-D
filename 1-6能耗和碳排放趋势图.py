# 本代码绘制出单位GDP能耗和单位能源消费量碳排放的量及减少率折线图，以对能耗和碳排放进行趋势分析
import pandas as pd
import matplotlib.pyplot as plt
# 指定文本文件的路径
file_path = './数据表汇总/增长率.txt'

# 使用pandas读取文本文件，并生成数据框
data_frame = pd.read_csv(file_path, delimiter='	',header=0)  # 如果文本文件使用制表符分隔数据，请使用'\t'，否则根据实际情况指定分隔符
years = data_frame.iloc[:,0]
# print(data_frame.columns)
# print(data_frame.iloc[:,1])

# 设置四个子图
fig, axes = plt.subplots(2, 2, figsize=(14, 12))

# 设置全局标题
fig.suptitle('能耗和碳排放数据', fontsize=18)

# 颜色和线条样式
line_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# 标号标签
labels = ['(a)', '(b)', '(c)', '(d)']

for i in range(2):
    for j in range(2):
        ax = axes[i, j]
        ax.plot(years, data_frame.iloc[:, i * 2 + j + 1], marker='o', linestyle='-', color=line_colors[i * 2 + j], markersize=6, linewidth=3)
        ax.set_xlabel('年份', fontsize=16)
        # 获取对应指标值
        ax.set_ylabel(data_frame.columns[i * 2 + j + 1], fontsize=16)
        ax.set_title(data_frame.columns[i * 2 + j + 1], fontsize=16)
        ax.grid(True, alpha=0.5)

        # 添加标号标签
        ax.text(-0.1, 1.0, labels[i * 2 + j], transform=ax.transAxes, fontsize=18, fontweight='bold')

        ax.tick_params(axis='both', labelsize=17)

# 存储图表
plt.savefig('趋势图.png',bbox_inches='tight')
# plt.show()

