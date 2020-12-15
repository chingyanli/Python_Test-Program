# !/usr/bin/python3
# -*- coding: utf-8 -*-
# author: Noel Li

# import library
import pyvisa
import time
import serial

# Input
GPP_4323_COM_INPUT = input('請輸入電源供應器COM PORT(數字即可):')
COM_INPUT = input('請輸入待測物COM PORT(數字即可):')

# Setting
GPP_4323_COMPORT = 'ASRL%s::INSTR' %(GPP_4323_COM_INPUT)
GPP_4323_BAUDRATE = 115200

COM_PORT = 'COM%s' %(COM_INPUT)  # DUT COM_PORT
BAUD_RATES = 115200  # 設定傳輸速率

count = 0

def Delay(Second):
    time.sleep(Second)

Delay(5)

while True:
# pyvisa resource manager
    RM = pyvisa.ResourceManager()

# Power Supply code
    GPP_4323 = RM.open_resource(GPP_4323_COMPORT, GPP_4323_BAUDRATE, write_termination="\n", read_termination="\n")
#print(GPP_4323.query('*IDN?'))             #儀器型號辨識指令
#>>>GW INSTEK,GPP-4323,SN:GET811215,V1.04   #回覆的狀態

    GPP_4323.write(':ALLOUTOFF') #關閉所有通道輸出
    Delay(1)

    GPP_4323.write('VSET1:28.5')    #設定CH1電壓 28.5V
    GPP_4323.write('VSET2:28.5')    #設定CH1電壓 28.5V
    Delay(1)

    VSET1 = GPP_4323.query('VSET1?')#讀回CH1電壓設定值
    VSET2 = GPP_4323.query('VSET2?')#讀回CH2電壓設定值
    Delay(1)

    GPP_4323.write('ISET1:1.5')     #設定CH1電流 1.5A
    GPP_4323.write('ISET2:1.5')     #設定CH2電流 1.5A
    Delay(1)

    ISET1 = GPP_4323.query('ISET1?')#讀回CH1電流設定值
    ISET2 = GPP_4323.query('ISET2?')#讀回CH2電流設定值
    #print(type(ISET1))  #格式為字串
    #print(VSET1, ISET2)

    if (VSET1 == '28.500') and (ISET1 == '1.5000'):
        GPP_4323.write(':ALLOUTON') #打開所有通道輸出
        print('Power ON.')
        Delay(1)

        DUT = serial.Serial(COM_PORT, BAUD_RATES, timeout=0.5)  # 套用上述的設定
        #DUT.open()
        while True:
            data = DUT.readline()

            if data == b'Press ENTER to get started':
                count += 1
                print('DUT Communication succeeded!!%d times now.' %(count))
                DUT.close()
                break
    else:
        print('Setting is NG.')

# DUT code
    #Console = RM.open_resource('ASRL3::INSTR')
'''
kEY WORD : Press ENTER to get started
'''

    #main code
    #DUT.open()
