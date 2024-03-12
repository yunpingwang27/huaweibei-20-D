
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['axes.unicode_minus'] = False # 用来正常显示负号

# 指定Excel文件路径
excel_file = './数据表汇总/碳排放拆分表.xlsx'

# 使用pandas读取Excel文件
xls = pd.ExcelFile(excel_file)

# 通过Sheet名称或者索引来选择第二个Sheet，这里使用Sheet名称作为示例
sheet_name = xls.sheet_names[0]  # 第二个Sheet的名称，索引从0开始

df = pd.read_excel(excel_file, sheet_name=sheet_name,usecols=range(12))
print(df.iloc[:,0])
label = df.iloc[:,0]
df = df.iloc[:,1:]

sf = pd.DataFrame()
for i in range(1,len(label)):
    sf[label[i]] = df.iloc[i,:]/df.iloc[0,:]
sf = sf.T
sf.to_csv('./proportion/部门碳排占比.csv',float_format='%.6f')