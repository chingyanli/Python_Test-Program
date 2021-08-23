'''撈取資料夾內所有特定欄列的資料'''

def SNDataCrawler(col_, row_):
    import os   # 模組 - 負責讀取資料夾跟檔案
    import csv  # 模組 - 處理 CSV

    from easygui import diropenbox  # 模組 - 直接導入選擇資料夾的UI畫面

    path = diropenbox()  # 跳出對話窗 選擇 資料夾路徑
    #=================================================================================================
    #=================================== SerialNumber_Data Crawler ===================================
    #=================================================================================================
    Means = []

    files = os.listdir(path)  # 得到資料夾下的所有檔名稱
    for file in files:
        #SerialNumber = file.split('.')
        #print(SerialNumber[0])  # 序號 -> 新增至sheetname
        count = 0
        # =================================================================================================
        # =================================== Open CSV to recode data ====================================
        # =================================================================================================
        with open(r'%s\%s'%(path, file), encoding='utf-8', newline='') as csvfile:
            Text = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in Text:
                Meas = row[col_] #指到 CSV的 Meas欄位
                count += 1
                if count == row_:   #指到 所需要的 資料, append到 Data的list欄位
                    Means.append(float(Meas))
    return Means #回傳Meas(第X欄所有內容)


#SNDataCrawler(13 , 22)
print('SNDataCrawler(col, row)= ',SNDataCrawler(13, 22))