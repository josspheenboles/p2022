#from win32com.client import Dispatch
import pandas as pd
from openpyxl import load_workbook
import os
import time

def run_macro(workbook_name, vba_sub, com_instance):
    wb = load_workbook(workbook_name)
    wb.RefreshAll()
    xl_module = wb.VBProject.VBComponents.Add(1)
    xl_module.CodeModule.AddFromString(vba_sub.strip())
    com_instance.Application.Run('UpdateLinkValues')
    wb.Save()
    wb.Close()
    return True

def main():
    dir_root  = ("C:\\Model_Spreadsheets")

    vba_sub = \
        '''
        sub UpdateLinkValues()
            Application.AskToUpdateLinks = False
            ActiveWorkbook.UpdateLink Name:=ActiveWorkbook.LinkSources
        end sub
        '''

    xl_app = Dispatch("Excel.Application")
    xl_app.Visible = False
    xl_app.DisplayAlerts = False

    for root, dirs, files in os.walk(dir_root):
        for fn in files:
            if fn.endswith(".xlsx") and fn[0] is not "~":
                run_macro(os.path.join(root, fn), vba_sub, xl_app)
    xl_app.Quit()


if __name__ == "__main__":
    main()