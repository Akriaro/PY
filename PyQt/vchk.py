from win32api import GetFileVersionInfo
import os
import sys
import shutil
import subprocess
import time
import psutil

expPath = [r'X:\ExperiumTrunk', r'X:\ExperiumRelease']
expFileName = ['\Experium.exe', '\exprus.dll', '\expenu.dll', '\MailEngine.dll', '\SMSEngine.dll', '\GCalDav.dll', '\Telephony.dll']
srvPath = [r'X:\winserverexe\newexe\trunkexe', r'X:\winserverexe\newexe']
srvFileName = ['\exp_srv.exe', '\wdatasrv.exe', '\wmetasrv.exe', '\wmetasrch.exe', '\wdatacnv.exe', '\sexpsrv.exe', '\sdatasrv.exe', '\smetasrv.exe', '\smetasrch.exe', '\sdatacnv.exe']
srvPath64 = [r'X:\winserverexe\newexe\trunkexe64', r'X:\winserverexe\newexe\64']
srvFileName64 = ['\exp_srv64.exe', '\wdatasrv64.exe', '\wmetasrv64.exe', '\wmetasrch64.exe', '\wdatacnv64.exe', '\sexpsrv64.exe', '\sdatasrv64.exe', '\smetasrv64.exe', '\smetasrch64.exe', '\sdatacnv64.exe']
localPath = [r'C:\Experium\rHrm', r'C:\Experium\rAgn', r'C:\Experium\webtest.PMI', r'C:\Experium\webtest.Unilever']



def chkClientLoc2(localPath, expFileName):
    ver = []
    for e in expFileName:
        if os.path.isfile(localPath + e):
            a = GetFileVersionInfo(localPath + e, '\\')
            ms = a['FileVersionMS']
            ls = a['FileVersionLS']
            v = (ms >> 16, ms & 0xFFFF, ls >> 16, ls & 0xFFFF)
        else:
            print('File not exist ' + i + e)
            os.system('pause')
        ver.append(v)
    return ver


def chkClientX():
    for i in expPath:
        ver = []
        for e in expFileName:
            if os.path.isfile(i + e):
                a = GetFileVersionInfo(i + e, '\\')
                ms = a['FileVersionMS']
                ls = a['FileVersionLS']
                v = (ms >> 16, ms & 0xFFFF, ls >> 16, ls & 0xFFFF)
            else:
                print('File not exist ' + i + e)
                os.system('pause')
            ver.append(v)
        # print(i)
        # print(ver)
        return ver

def cnv():
    a = chkClientX()
    b = chkClientLoc2()
    if a > b:
        print('EST UPDATE')
    else:
        print('FAIL')

def cnv2():
    try:
        a = chkClientX()
        # print(a)
    except:
        sys.exit()
    for i in localPath:
        b = chkClientLoc2(i, expFileName)
        print(i)
        print(expFileName)
        print(b)
        # print(i + ' cur ' + b)
        if a > b:
            print('Есть апдейт !')
            # tskill()
            # time.sleep(1)
            for e in expFileName:
                shutil.copy(expPath[0] + e, i)
            print('Обновлено ')
        # if a <= b:
        else:
            print('Нет апдейта !')


# cnv2()