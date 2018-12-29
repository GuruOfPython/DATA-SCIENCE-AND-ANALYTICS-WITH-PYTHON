import openpyxl
from openpyxl import load_workbook
from openpyxl import Workbook
from PIL import Image

width = 100
height = 100

img = Image.open('images/P_6.png')
# img = img.resize((width,height))
img.save('images/P_5.png')

wb = openpyxl.Workbook()
ws = wb.worksheets[0]
img = openpyxl.drawing.image.Image('images/P_5.png')
ws.add_image(img,'F10')
wb.save('out.xlsx')
print('ready')