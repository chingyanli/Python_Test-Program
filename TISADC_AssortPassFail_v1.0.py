'''Pass Log had 26 Pass keywords.'''
'''1. Search logs in folder.'''
'''2. Reanme the log name that add _pass when log had 26 pass keywords.'''
'''3. Need to put log file down to the new folder(PASS).'''

import os
#from os import path, listdir, renames
from easygui import diropenbox

symbols = r'''`!@#$%^&*()_+-=/*{}[]\|'";:/?,.<>'''  #特殊符號

path = diropenbox()     #跳出對話窗 選擇 資料夾路徑
files = os.listdir(path)    #得到資料夾下的所有檔名稱
s = []
for file in files:
    if not os.path.isdir(file):
        count = 0
        with open(path+"\\"+file, 'r') as f:
            texts = f.readlines()
            for text in texts:
                if 'PASS:' in text:
                    count += 1
                else:
                    count += 0
        #print(count) #確認26個PASS, 代表該測試項目PASS數量正確. <class 'int'>
        if count == 26:
            print(file+' PASS')
            os.renames(path+"\\"+file, path + "\\" + "PASS" + "\\" + file.replace('.log', '_PASS.log'))
            print('匯整PASS完成.')
        else:
            print('%s_FAIL' %(file))
            os.renames(path + "\\" + file, path + "\\" + "FAIL" + "\\" + file.replace('.log', '_FAIL.log'))
            print('匯整FAIL完成.')