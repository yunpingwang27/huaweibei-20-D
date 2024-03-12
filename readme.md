## 代码解释
- 1-1碳排放可视化：主要对碳排放总量等数据进行条形图与折线图分段绘制，以分析其总量与变化趋势
- 1-2各部门碳排放可视化：绘制出2010-2020年的各部门碳排放折线图，与各部门平均碳排放占比扇形图
- 1-3季节性STL分析：碳排放总量的变化进行季节性分析
- 1-4 相关性分析：本文主要分析人口，GDP、能源消耗量这三种指标与碳排放量的相关性：
    - 绘制散点图与拟合直线；
    - 求出三种相关系数
    - 进行OLS最小二乘法拟合
- 1-5各指标对碳排放的贡献分析：通过XGBoost和GBDT构建模型，进行评估后计算SHAP值，以评估各指标对碳排放量的贡献
- 1-6能耗和碳排放趋势图：绘制出单位GDP能耗和单位能源消费量碳排放的量及减少率折线图，以对能耗和碳排放进行趋势分析
- 2-1同比环比增长率：主要计算'常驻人口','区域生产总值','能源消耗量','碳排放量'四种指标的同比与环比的增长率并绘制折线图
- 3-1碳排放各品种部门占比：求出各部门能耗占比，各部门碳排放、对应各能源品类的碳排放占比并输出对应表格。