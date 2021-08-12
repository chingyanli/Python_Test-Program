'''Data Converter for TISADC'''
'''1. Search logs in folder.'''
'''2. Testlog Data Crawler.'''

import os
from easygui import diropenbox

path = diropenbox()  # 跳出對話窗 選擇 資料夾路徑

During_Sampling = []
No_Sampling = []
BIAS_SENSOR = []
REF = []
VP_SENSOR = []
BIST_status = []

#=================================== SerialNumber_Data Crawler ===================================
def SNDataCrawler():
    files = os.listdir(path)  # 得到資料夾下的所有檔名稱
    for file in files:
        SerialNumber = file.split('_')
        print(SerialNumber[1], end=',')
    print()

#================================== Data Crawler ==================================
def DataCrawler(TestItem, EOV):    #TestItem=> Testlog的關鍵字, EOV=> enf_of_value(你所需要的資料長度)   #示範(DuringSampling = , 2)

    files = os.listdir(path)  # 得到資料夾下的所有檔名稱
    for file in files:
        if not os.path.isdir(file):
            with open(path + "\\" + file, 'r') as f:
                text = f.read()
                idFilter = '%s' %(TestItem)  # 找尋關鍵字
                idPosition = text.find(idFilter)
                start_of_value = idPosition + (len(TestItem))
                end_of_value = start_of_value + (EOV)
                TestItem_values = text[start_of_value:end_of_value]
                print(TestItem_values, end=',')  #確認OK
    print()

# ========== SerialNumber ==========
SNDataCrawler()

# ========== Measurement 1 ==========
DataCrawler('DuringSampling = ', 2)
DataCrawler('No Sampling = ', 2)
DataCrawler('BIAS_SENSOR = ', 4)
DataCrawler('REF = ', 4)
DataCrawler('VP_SENSOR = ', 4)
DataCrawler('BIST status : ', 3)

# ========== Measurement 2 ==========
DataCrawler('Offset Voltage(CH1) = ', 5)
DataCrawler('Offset Voltage(CH2) = ', 5)
DataCrawler('Offset Voltage(CH3) = ', 5)
DataCrawler('Offset Voltage(CH4) = ', 5)
DataCrawler('Offset Voltage(CH5) = ', 5)

# ========== Measurement 3 ==========
DataCrawler('Continuously_CH1 = ', 2)
DataCrawler('Continuously_CH2 = ', 2)
DataCrawler('Continuously_CH3 = ', 2)
DataCrawler('Continuously_CH4 = ', 2)
DataCrawler('Continuously_CH5 = ', 2)

# ========== Measurement 4 ==========
DataCrawler('DUV Mode(CH1) = ', 6)
DataCrawler('DUV Mode(CH2) = ', 6)
DataCrawler('DUV Mode(CH3) = ', 6)
DataCrawler('DUV Mode(CH4) = ', 6)
DataCrawler('DUV Mode(CH5) = ', 6)