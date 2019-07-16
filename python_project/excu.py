import pandas as pd
import xlrd
def requirement(path_details_info):
	excel_path=input("Enter the Excel/xlsx file path\n")
	excel_file=input("Enter the File nam\n\n")
	excel_sheet_number=int(input("Enter the sheet index number \n\n"))
	column_name=input("Enter the column name\n\n")
	#dfs = pd.read_excel("C:\\Users\\thangams\\Desktop\\python_project\\file_info\\Tracebility.xlsx", sheet_name="Sheet1",index_col = 0,usecols=['Requirement'])
	path=excel_path+'\\'+excel_file
	wb=xlrd.open_workbook(path)
	sheet = wb.sheet_by_index(0) 
	id1=[]
	for i in range(sheet.ncols):
		if column_name==sheet.cell_value(0,i):
			for j in range(sheet.nrows):
				#print(sheet.cell_value(j,0))
				id1.append(sheet.cell_value(j,0))
    #without Duplicate ids[id1 is with duplicate]
	mylist = list(dict.fromkeys(id1))
	try:
		dup_ch=int(input("Enter your chooise:\n\n 1.without Duplicate\n 2.with Duplicate\n\n"))	
		if dup_ch ==1:
			return excute(mylist)
		elif dup_ch==2:
			return excute(id1)
		else:
			print("Worng input plz enter correct input")
			requirement()
	except:
			print("Worng input plz enter correct input")
			requirement()


def excute(data):
	print(data)



	
requirement()
