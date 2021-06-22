'''Pass Log had 26 Pass keywords.'''
'''1. Search logs in folder.'''
'''2. Reanme the log name that add _pass when log had 26 pass keywords.'''
'''3. Need to put log file down to the new folder(PASS).'''

import os
#from os import path, listdir, renames
from easygui import diropenbox

symbols = r'''`!@#$%^&*()_+-=/*{}[]\|'";:/?,.<>'''  #特殊符號

path = diropenbox()  # 跳出對話窗 選擇 資料夾路徑

During_Sampling = []
No_Sampling = []
BIAS_SENSOR = []
REF = []
VP_SENSOR = []
BIST_status = []



#================================== DuringSampling_Data Crawler ==================================
def DataCrawler(TestItem, SOV, EOV, ):    #TestItem=> Testlog的關鍵字, SOV=> start_of_value, EOV=> enf_of_value   #示範(DuringSampling = , 17, 2)

    files = os.listdir(path)  # 得到資料夾下的所有檔名稱
    for file in files:
        if not os.path.isdir(file):
            with open(path + "\\" + file, 'r') as f:
                text = f.read()
                idFilter = '%s' %(TestItem)  # 找尋關鍵字
                idPosition = text.find(idFilter)
                start_of_value = idPosition + (SOV)
                end_of_value = start_of_value + (EOV)
                TestItem_values = text[start_of_value:end_of_value]
                print(TestItem_values, end=',')  #確認OK
    print()
'''
                if TestItem == 'DuringSampling = ':
                    During_Sampling.append(TestItem_values)
                elif TestItem == 'No Sampling = ':
                    No_Sampling.append(TestItem_values)
                elif TestItem == 'BIAS_SENSOR = ':
                    BIAS_SENSOR.append(TestItem_values)
'''
        #print(During_Sampling_list)
        #print(No_Sampling)
        #print(BIAS_SENSOR)

# ========== Measurement 1 ==========
DataCrawler('DuringSampling = ', 17, 2)
DataCrawler('No Sampling = ', 14, 2)
DataCrawler('BIAS_SENSOR = ', 14, 4)
DataCrawler('REF = ', 6, 4)
DataCrawler('VP_SENSOR = ', 12, 4)
DataCrawler('BIST status : ', 14, 3)

# ========== Measurement 2 ==========
DataCrawler('Offset Voltage(CH1) = ', 22, 5)
DataCrawler('Offset Voltage(CH2) = ', 22, 5)
DataCrawler('Offset Voltage(CH3) = ', 22, 5)
DataCrawler('Offset Voltage(CH4) = ', 22, 5)
DataCrawler('Offset Voltage(CH5) = ', 22, 5)

# ========== Measurement 3 ==========
DataCrawler('Continuously_CH1 = ', 19, 2)
DataCrawler('Continuously_CH2 = ', 19, 2)
DataCrawler('Continuously_CH3 = ', 19, 2)
DataCrawler('Continuously_CH4 = ', 19, 2)
DataCrawler('Continuously_CH5 = ', 19, 2)

# ========== Measurement 4 ==========
DataCrawler('DUV Mode(CH1) = ', 16, 6)
DataCrawler('DUV Mode(CH2) = ', 16, 6)
DataCrawler('DUV Mode(CH3) = ', 16, 6)
DataCrawler('DUV Mode(CH4) = ', 16, 6)
DataCrawler('DUV Mode(CH5) = ', 16, 6)

# ========== Result ==========
'''
for i in During_Sampling:
    print(i, end= ',')

'''
#print(During_Sampling)
#print(No_Sampling)
#print(BIAS_SENSOR)