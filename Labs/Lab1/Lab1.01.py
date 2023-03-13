import xlsxwriter
import random

workbook = xlsxwriter.Workbook('Labs\Lab1\\results.xlsx')
worksheet = workbook.add_worksheet()

n = [4.8] * 100

for i in range(100):
    n[i] = round(n[i] + random.random(), 2)

for i in range(100):
    line1 = 'A' + str(i)
    worksheet.write(line1, i)
    line2 = 'B' + str(i)
    worksheet.write(line2, n[i])

workbook.close()
print(n)