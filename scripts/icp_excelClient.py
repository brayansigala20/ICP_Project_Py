import pandas as pd
from openpyxl import Workbook
import datetime as dt

OG_EXCEL = pd.read_excel("C:\\Users\\braya\\Downloads\\ICP\\MASTER ROBOT ICP 2024.xlsx")
excel = OG_EXCEL
# excel = OG_EXCEL[
#     OG_EXCEL["OC CLIENTE"].notna()
#     & (OG_EXCEL["OC CLIENTE"].str.strip() != "N/A")
#     & (OG_EXCEL["OC CLIENTE"].str.strip() != "N-A")
#     & (OG_EXCEL["OC CLIENTE"].str.strip() != "n-a")
#     & (OG_EXCEL["OC CLIENTE"].str.strip() != "na")
#     & (OG_EXCEL["OC CLIENTE"].str.strip() != "")
# ]

header_datetime = dt.datetime(2024, 5, 1, 0, 0)

columnData = {}
if header_datetime in excel.columns:
    columnData = excel[header_datetime]


clientName = excel["CLIENTE"].to_dict()
orderPurchase = excel["OC CLIENTE"].to_dict()
print(orderPurchase)
wb = Workbook()

ws = wb.active
ws.title = "Lista de Nombres"

ws["A1"] = "Nombre"
ws["B1"] = "Folio"
ws["C1"] = "Oc"

for idx, item in enumerate(clientName.values(), start=2):
    text = item
    ws.cell(row=idx, column=1, value=text)

for idx, item in enumerate(columnData, start=2):
    text = item
    ws.cell(row=idx, column=2, value=text)

for idx, item in enumerate(orderPurchase.values(), start=2):
    text = item
    ws.cell(row=idx, column=3, value=text)

wb.save("C:\\Users\\braya\\Downloads\\ICP\\Lista_Nombres.xlsx")
