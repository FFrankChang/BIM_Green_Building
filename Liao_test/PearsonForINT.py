import pandas as pd
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
import seaborn as sns
import chardet

# 检测文件编码
with open(r'D:\时光旅人\tongji\创新创业项目2 BIM+AI资产评估\数据\case002_基于多个回归预测算法的房价预测_数据\data_train.csv', 'rb') as f:
    result = chardet.detect(f.read())

# 使用检测到的编码读取文件
df = pd.read_csv(r'D:\时光旅人\tongji\创新创业项目2 BIM+AI资产评估\数据\case002_基于多个回归预测算法的房价预测_数据\data_train.csv', encoding=result['encoding'])

# 提取“地面平整度”和“地下室总面积”列
bedroom_area = df['卧室数']
basement_area = df['地下室总面积']

# 计算皮尔逊相关系数
correlation, p_value = pearsonr(bedroom_area, basement_area)
print(f"相关系数: {correlation}")
print(f"p值: {p_value}")

# 可视化
plt.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(10, 6))
sns.scatterplot(x=bedroom_area, y=basement_area)
plt.title('卧室数与地下室总面积的关系')
plt.xlabel('卧室数')
plt.ylabel('地下室总面积')
plt.show()