import xlsxwriter
import imageio
import sys

# pict = imageio.imread('Gmap_1.png')
#
# workbook = xlsxwriter.Workbook('demo.xlsx')
# worksheet = workbook.add_worksheet()
#
# for i in range(0, pict.shape[0]):
#     for j in range(0, pict.shape[1]):
#         a = pict[i, j]
#         col = '#%02x%02x%02x' % (a[0], a[1], a[2])
#         format = workbook.add_format()
#         format.set_bg_color(col)
#         worksheet.write(i, j, '', format)
# workbook.close()


#!/usr/bin/python3

from openpyxl import Workbook
from openpyxl.drawing.image import Image

book = Workbook()
sheet = book.active

img = Image("Gmap_1.png")
sheet['A1'] = 'This is Sid'

sheet.add_image(img, 'B2')

book.save("demo.xlsx")