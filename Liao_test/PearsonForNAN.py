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
ground_flatness = df['地面平整度']
basement_area = df['地下室总面积']

#字符映射
flatness_class = {'Gtl': 1, 
               'Mod': 2, 
               'Sev': 3}
ground_flatness = ground_flatness.map(flatness_class)

# 计算皮尔逊相关系数
correlation, p_value = pearsonr(ground_flatness, basement_area)
print(f"相关系数: {correlation}")
print(f"p值: {p_value}")

# 可视化
plt.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(10, 6))
sns.scatterplot(x=ground_flatness, y=basement_area)
plt.title('地面平整度与地下室总面积的关系')
plt.xlabel('地面平整度')
plt.ylabel('地下室总面积')
plt.show()
