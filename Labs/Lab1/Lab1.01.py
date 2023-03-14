import xlsxwriter

N = 50

class interval:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

workbook = xlsxwriter.Workbook('Labs\Lab1\\results.xlsx')
worksheet = workbook.add_worksheet()


allNumbers = [5.34, 4.85, 4.90, 5.15, 5.11, 4.99, 4.76, 5.21, 4.95, 4.94,5.06, 5.21, 5.05, 5.07, 4.78, 5.01, 4.99, 5.13, 4.78, 4.93, 4.92, 5.09, 5.02, 5.37, 4.96, 4.89, 5.08, 5.05, 4.82, 5.32, 4.87, 5.09, 5.14, 4.80, 5.30, 5.06, 4.79, 4.84, 5.01, 5.03, 4.84, 5.09, 4.80, 5.22, 5.17, 4.99, 4.84, 5.07, 5.07, 5.15]

allNumbers.sort()

for i in range(N):
    line1 = 'A' + str(i)
    worksheet.write(line1, i)
    line2 = 'B' + str(i)
    worksheet.write(line2, allNumbers[i])

workbook.close()