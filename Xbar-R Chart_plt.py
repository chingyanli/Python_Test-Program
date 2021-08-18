''' Control - Chart 管制圖'''
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np
import random

# ================= 規格參數(格式需求: list) =================
Serial_Number = ['210100001', '210100002', '210100003', '210100004', '210100005', '210100006', '210100007',
                 '210100008', '210100009', '210100010']

Higher_Specs = [5.2, 5.2, 5.2, 5.2, 5.2, 5.2, 5.2, 5.2, 5.2, 5.2]   #從CSV的上限規格套入
Target = [4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8]     #從CSV的規格(下限+上限) / 2 套入中心值, 要注意是否落在中心值
Lower_Specs = [4.4, 4.4, 4.4, 4.4, 4.4, 4.4, 4.4, 4.4, 4.4, 4.4]    #從CSV的下限規格套入

# ================= 假量測數據(格式需求: list) =================
Means = []
for i in range(0, 10):
    j = random.uniform(4.65, 4.95)
    Means.append(j)
#print('數據: ',Means)

# ================= 圖面設定 =================
fig, ax = plt.subplots() # Create a figure and an axes.

# ================= Y 軸刻度設定 =================
ax.yaxis.set_minor_locator(MultipleLocator(0.05))  #間隔0.05

# ================= 運算(規格: Target + 1sigma, Target - 1sigma) =================
count = len(Target) # 判斷樣品數量

std = np.std(Means) # 標準差
'''標準差 尚未 除以 標準係數差'''

mean = np.mean(Means)   # 平均值

add_3sigma = (mean + (3 * std))    # 運算 平均值 + 3Sigma
sub_3sigma = (mean - (3 * std))    # 運算 平均值 - 3Sigma

Line_add_3sigma_Specs = []
Line_sub_3sigma_Specs = []

for k in range(count):
    Line_add_3sigma_Specs.append(add_3sigma)
    Line_sub_3sigma_Specs.append(sub_3sigma)

# ================= 畫圖(規格: 上限值, 下限值, 目標值) =================
Line_Higher_Specs = plt.plot(Higher_Specs, label="UCL", linestyle='-', color='r')

Line_add_3sigma_Specs = plt.plot(Line_add_3sigma_Specs, label="u +3σ", linestyle='--', color='orange')

Line_Target = plt.plot(Target, label="Target", linestyle='--', color="g")

Line_sub_3sigma_Specs = plt.plot(Line_sub_3sigma_Specs, label="u -3σ", linestyle='--', color='orange')

Line_Lower_Specs = plt.plot(Lower_Specs, label="LCL", linestyle='-', color='r')

# ================= 畫圖(量測數據) =================
#Line_Means = plt.plot(Means, label="Means", linestyle='-', color='b') #可以使用
Line_Means = plt.plot(Serial_Number, Means, 'bo-')

# ================= 圖面 Tile, Legend 設定 =================
ax.set_title('Xbar-R Chart')
ax.legend()

plt.xlabel('Serial Number')
plt.ylabel('5V Power Voltage')

plt.xticks(fontsize=8, rotation=35)
plt.yticks(fontsize=8)

plt.grid(True)
plt.show()