import pandas as pd
from scipy.stats import spearmanr
import chardet

# 检测文件编码
with open(r'D:\时光旅人\tongji\创新创业项目2 BIM+AI资产评估\数据\case002_基于多个回归预测算法的房价预测_数据\data_train.csv', 'rb') as f:
    result = chardet.detect(f.read())

# 使用检测到的编码读取文件
df = pd.read_csv(r'D:\时光旅人\tongji\创新创业项目2 BIM+AI资产评估\数据\case002_基于多个回归预测算法的房价预测_数据\data_train.csv', encoding=result['encoding'])

# 提取“地面平整度”和“地下室总面积”列
ground_flatness = df['地面平整度']
basement_area = df['地下室总面积']

# 计算斯皮尔曼秩相关系数和 P 值
corr, p_value = spearmanr(ground_flatness , basement_area)

# 输出结果
print(f"斯皮尔曼秩相关系数: {corr}")
print(f"P 值: {p_value}")