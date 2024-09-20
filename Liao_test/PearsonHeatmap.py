import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import chardet

# 检测文件编码
with open(r'D:\时光旅人\tongji\创新创业项目2 BIM+AI资产评估\数据\case002_基于多个回归预测算法的房价预测_数据\data_train.csv', 'rb') as f:
    result = chardet.detect(f.read())

# 使用检测到的编码读取文件
df = pd.read_csv(r'D:\时光旅人\tongji\创新创业项目2 BIM+AI资产评估\数据\case002_基于多个回归预测算法的房价预测_数据\data_train.csv', encoding=result['encoding'])

# 计算皮尔逊相关性矩阵
correlation_matrix = df.corr(method='pearson')

# 绘制热力图
plt.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
'''plt.figure(figsize=(14, 12))
sns.heatmap(correlation_matrix, annot=True, fmt=".1f", cmap='coolwarm')
plt.title('Spearman Correlation Heatmap')
plt.show()'''

# 筛选出相关性绝对值大于0.5的部分
high_correlation = correlation_matrix[(correlation_matrix.abs() >= 0.5) & (correlation_matrix != 1.0)]

# 绘制热力图
plt.figure(figsize=(14, 12))
sns.heatmap(high_correlation, annot=True, fmt=".2f", cmap='coolwarm', mask=high_correlation.isnull())
plt.title('High Pearson Correlation Heatmap')
plt.show()

'''
# 将相关性结果保存为表格
correlation_table = correlation_matrix.stack().reset_index()
correlation_table.columns = ['Feature 1', 'Feature 2', 'Correlation']
correlation_table.to_csv('correlation_results.csv', index=False)
print("相关性结果已保存为correlation_results.csv")
'''