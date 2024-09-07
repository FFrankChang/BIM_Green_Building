import pandas as pd
from scipy.stats import spearmanr

# 加载数据集
file_path = r"C:\Users\z_fra\Downloads\dataset_v1.1.xlsx"
data = pd.read_excel(file_path)

# 提取相关列并去除缺失值
data_clean = data[['房价', '居住面积']].dropna()

# 计算斯皮尔曼秩相关系数和 P 值
corr, p_value = spearmanr(data_clean['房价'], data_clean['居住面积'])

# 输出结果
print(f"斯皮尔曼秩相关系数: {corr}")
print(f"P 值: {p_value}")
