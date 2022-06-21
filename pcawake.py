import pyautogui as pd
import sys
import os
try:
    if len(sys.argv)>1:
        if sys.argv[1]=='create':
            try:
                fin = open("keepawake.bat", "rt")
                data = fin.read()
                data = data.replace('<file_path>', os.path.abspath(__file__).replace('\\','/'))
                fin.close()
                fin = open("keepawake.bat", "wt")
                fin.write(data)
                fin.close()
            except:
                import traceback
                print(traceback.format_exc())
    else:
        while(True):
            pd.moveTo(100,100)
            pd.press('shift')
            pd.moveTo(1000,100)
            # if(KeyboardInterrupt):
            #     break
except (KeyboardInterrupt, SystemExit):
        raise