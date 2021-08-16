'''撈取資料夾內所有特定欄列的資料'''

import os   # 模組 - 負責讀取資料夾跟檔案
import csv  # 模組 - 處理 CSV

from easygui import diropenbox  # 模組 - 直接導入選擇資料夾的UI畫面

path = diropenbox()  # 跳出對話窗 選擇 資料夾路徑

#=================================================================================================
#=================================== SerialNumber_Data Crawler ===================================
#=================================================================================================
def SNDataCrawler(row_, column_):
    files = os.listdir(path)  # 得到資料夾下的所有檔名稱
    for file in files:
        #SerialNumber = file.split('.')
        #print(SerialNumber[0])  # 序號 -> 新增至sheetname

        # =================================================================================================
        # =================================== Open CSV to recode data ====================================
        # =================================================================================================
        with open(r'%s\%s'%(path, file), encoding='utf-8', newline='') as csvfile:
            Text = csv.reader(csvfile, delimiter=',', quotechar='|')
            Meas = []
            for row in Text:
                Meas.append(row[row_]) #指到 CSV的 Meas欄位(第14欄)
            print(Meas[column_]) #指到Meas(第14欄)的第三列

#SNDataCrawler(13, 2)