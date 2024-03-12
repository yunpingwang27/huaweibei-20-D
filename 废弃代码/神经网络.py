# 废弃代码：用神经网络拟合，三种指标对碳排放的关系模型
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split

excel_file = './数据表汇总/经济与能源拆分表.xlsx'
xls = pd.ExcelFile(excel_file)
sheet_name = xls.sheet_names[4]  # 第二个Sheet的名称，索引从0开始
df = pd.read_excel(excel_file, sheet_name=sheet_name,usecols=list(range(1,12)))

X = df.iloc[:3,].T  # 选择前三行，并进行转置，使每行代表一个观测值
print(X)

# 创建因变量（碳排放量）
y = df.iloc[3,]

# 选择前三行并进行转置，使每行代表一个观测值
X = df.iloc[:3, :].T

# 添加截距项（常数项）到X
X['intercept'] = 1.0  # 添加一个名为 'intercept' 的列，所有值为1

# 创建因变量（碳排放量）
y = df.iloc[3, :]

# 分割数据集为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# 假设你已经加载了数据框 df

# 选择前三行并进行转置，使每行代表一个观测值
X = df.iloc[:3, :].T

# 添加截距项（常数项）到X
X['intercept'] = 1.0  # 添加一个名为 'intercept' 的列，所有值为1

# 创建因变量（碳排放量）
y = df.iloc[3, :]

# 转换数据为PyTorch张量
X_tensor = torch.tensor(X.values, dtype=torch.float32)
y_tensor = torch.tensor(y.values, dtype=torch.float32).view(-1, 1)  # 将y转换为列向量

# 分割数据集为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X_tensor, y_tensor, test_size=0.2)

# 定义一个简单的神经网络模型
class SimpleNN(nn.Module):
    def __init__(self, input_size, hidden_size1,hidden_size2):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size1)
        self.relu1 = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size1, hidden_size2)
        self.relu2 = nn.ReLU()
        self.fc3 = nn.Linear(hidden_size2, 1)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu1(x)
        x = self.fc2(x)
        x = self.relu2(x)
        x = self.fc3(x)
        return x

# 创建模型
input_size = X_train.shape[1]
hidden_size1 = 64
hidden_size2 = 32
model = SimpleNN(input_size, hidden_size1,hidden_size2)

# 定义损失函数和优化器
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 训练模型
epochs = 1000
for epoch in range(epochs):
    optimizer.zero_grad()
    outputs = model(X_train)
    loss = criterion(outputs, y_train)
    loss.backward()
    optimizer.step()
    if epoch == epochs-1:
        print(f"Test Loss: {loss.item()}")
# 评估模型
with torch.no_grad():
    test_outputs = model(X_test)
    test_loss = criterion(test_outputs, y_test)



# 使用模型进行预测
with torch.no_grad():
    predictions = model(X_test)

# 打印预测结果
print(predictions)
torch.save(model.state_dict(), 'model_weights.pth')