#rm = ResourceManager


import visa                             #載入VISA函式庫
import time                             #載入時間函式庫

rm = visa.ResourceManager()             #將rm定義為ResourceManager

rm.list_resources()                     #將已連接儀器列出清單
# start of Untitled

v34970A = rm.open_resource('GPIB0::9::INSTR')          #連接GPIB::9::(Agilent_34970A)

print(v34970A.query('*IDN?'))           #印出儀器資訊

readings = v34970A.query(':MEASure:VOLTage:DC? %s,%s,(%s)' % ('AUTO', 'DEF', '@201'))

v34970A.write(':ROUTe:CHANnel:DELay:AUTO %d,(%s)' % (1, '@201'))
v34970A.write(':ROUTe:CHANnel:DELay:AUTO %d,(%s)' % (0, '@201'))
v34970A.write(':ROUTe:OPEN (%s)' % ('@301'))
v34970A.write(':ROUTe:CLOSe (%s)' % ('@301'))

v34970A.close()
rm.close()

# end of Untitled




