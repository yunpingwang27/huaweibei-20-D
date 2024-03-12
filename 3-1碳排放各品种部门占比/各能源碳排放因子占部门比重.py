
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"STSONG.TTF", size=14)
from matplotlib.font_manager import FontManager

mpl_fonts = set(f.name for f in FontManager().ttflist)

plt.rcParams['axes.unicode_minus'] = False # 用来正常显示负号
# sns.set(font='SimHei')                        

# 指定Excel文件路径
excel_file = '碳排放拆分表.xlsx'

# 使用pandas读取Excel文件
xls = pd.ExcelFile(excel_file)

# 通过Sheet名称或者索引来选择第二个Sheet，这里使用Sheet名称作为示例
sheet_name = xls.sheet_names[1]  # 第二个Sheet的名称，索引从0开始

# columns = list(range(12))
# 使用pandas读取第二个Sheet的数据
# columns = list(range(12))
df = pd.read_excel(excel_file, sheet_name=sheet_name)
# print(df.iloc[:,0])
label = df.iloc[:,0]
# label = ['农林消费部门','交通消费部门','建筑消费部门','居民生活消费']
# df = df.iloc[:,1:]

label_enegry = df.iloc[:,0]
print(label_enegry)
df = df.iloc[:,1:]
# print(label_enegry)

excel_file = '经济与能源拆分表.xlsx'

# 使用pandas读取Excel文件
xls = pd.ExcelFile(excel_file)

# 通过Sheet名称或者索引来选择第二个Sheet，这里使用Sheet名称作为示例
sheet_name = xls.sheet_names[2]  # 第二个Sheet的名称，索引从0开始
# 能耗
# columns = list(range(12))
# 使用pandas读取第二个Sheet的数据
# columns = list(range(12))
ef = pd.read_excel(excel_file, sheet_name=sheet_name)
# print(ef.iloc[:,0])
# label = ef.iloc[:,0]
label = ['农林消费部门','工业消费部门','交通消费部门','建筑消费部门','居民生活消费']
# ef = ef.iloc[:,1:]

# label_enegry_1 = ef.iloc[:,0]
# print(len(list(label_enegry_1)))
ef = ef.iloc[:,1:]
# print(label_enegry_1)

indexes_to_remove =list(range(6,18))+list(range(24,30))  # 在这里指定要删除的行的索引
print(indexes_to_remove)
# 使用 drop 方法删除指定的行
ef = ef.drop(indexes_to_remove)
excel_file = './数据表汇总/碳排放拆分表.xlsx'
label_enegry_1 = ef.iloc[:,0]
print(len(label_enegry_1))
print(ef)
# 使用pandas读取Excel文件
xls = pd.ExcelFile(excel_file)

# 通过Sheet名称或者索引来选择第二个Sheet，这里使用Sheet名称作为示例
sheet_name = xls.sheet_names[0]  # 第二个Sheet的名称，索引从0开始

columns = list(range(12))
# 使用pandas读取第二个Sheet的数据
sdf = pd.read_excel(excel_file, sheet_name=sheet_name)
label_pro = sdf.iloc[:,0]
sdf = sdf.iloc[:,1:]
# print(sdf)
# print(label_pro)
energy_propo = pd.DataFrame()
# print()
s = [1,2,4,5,6]

# print(ef)
# sf = pd.DataFrame()
# sf_list = sdf.iloc[2]
sf_list = []
# print(sf_list)
for i in range(len(label)):
    sf = pd.DataFrame()
    for j in range(6):
        # sf = pd.DataFrame()
        # if df.iloc[i*6+j,0] != '-':
        sf[label_enegry[j]] = df.iloc[i*6+j,:] * ef.iloc[i*6+j,:]
        # print(sf[label_enegry[j]])
        # print(sdf.iloc[s[i],:])
        sf[label_enegry[j]] = sf[label_enegry[j]]/sdf.iloc[s[i],:]
        # else:
            # sf[label_enegry[j]] = None
    sf_list.append(sf)
    sf = sf.T
    sf.to_csv('./proportion/'+label[i]+'各品种碳排放比重.csv')
# print(len(sf_list))
# print(len(sf))
# print(sf_list[0])
# for i in range(5):
    # energy_propo[label[i]] = 

# print(sf[label[0]][label_enegry[0]])
# sf = pd.DataFrame
# sf = pd.DataFrame()
# for i in range(1,len(label)):
#     sf[label[i]] = df.iloc[i,:]/df.iloc[0,:]
#     # print(sf['农林消费部门'])
#     # sf['发电'] = df.iloc[1,:]/df.iloc[0,:]
#     # print(sf['农林消费部门'])
# sf = sf.T
# # year_on_year_growth.to_csv('year_on_year.csv',float_format='%.6f')
# sf.to_csv('./proportion/部门能耗占比.csv',float_format='%.6f')
# # print(sf['居民生活消费'])