import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# 加载数据集
file_path = r"C:\Users\z_fra\Downloads\dataset_v1.1.xlsx"
data = pd.read_excel(file_path)

# 提取需要的字段
features = ['地面平整度', '住宅类型', '住宅层数', '原施工年份', '更新年份', '房价']
target = '居住面积'

# 去除缺失值
data_clean = data[features + [target]].dropna()

# 定义特征（X）和目标（y）
X = data_clean[features]
y = data_clean[target]

# 将分类数据转换为数值型数据（如果存在）
X = pd.get_dummies(X, drop_first=True)

# 将数据集划分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 初始化随机森林模型
model = RandomForestRegressor(random_state=42)

# 训练模型
model.fit(X_train, y_train)

# 预测测试集
y_pred = model.predict(X_test)

# 计算均方误差（MSE）
mse = mean_squared_error(y_test, y_pred)

# 输出MSE结果
print(f"均方误差: {mse}")

# 输出模型的重要特征
feature_importances = pd.Series(model.feature_importances_, index=X_train.columns)
print("特征重要性：")
print(feature_importances.sort_values(ascending=False))
