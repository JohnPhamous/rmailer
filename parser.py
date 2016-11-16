from openpyxl import load_workbook
import sys

wb = load_workbook(filename = sys.argv[1])
sheet = wb['Sheet1']
print(sheet['A1'].value)

