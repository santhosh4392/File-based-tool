import os
import pandas as pd
import xlrd
import re
import csv
def requirement(path_details_info):
    excel_path="C:\\Users\\thangams\\Desktop\\python_project\\file_info" #input("Enter the Excel/xlsx file path\n") -->
    excel_file="Tracebility.xlsx"#input("Enter the File name\n\n")-->
    excel_sheet_number=0 #int(input("Enter the sheet index number \n\n"))--->
    column_name='Requirement'#input("Enter the column name\n\n") --->
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
            excute(path_details_info,mylist)
        elif dup_ch==2:
            return excute(path_details_info,id1)
        else:
            print("Worng input plz enter correct input")
            path_conformation()
    except:
            print("Worng input plz enter correct input")
            path_conformation()


def excute(path_data,req_data):
    output={} 
   # print(req_data)
    #print(path_data)
    data=[]
    file_details=[]  

    file_list=[]

    for r_data in req_data:
        if r_data not in 'Requirement':
            for data_ph in path_data:
                arr= os.listdir(data_ph)
                for j in arr:
                     res=data_ph+"\\"+j             
                     if re.search(r'\.py',res):
                        with open(res,'r') as f:
                             file_data=f.readlines()
                             #print(r_data)
                             #print(file_data)
                             for f_data in file_data:
                                 if re.search(r_data,f_data):
                                    file_details.append(r_data)
                                    #print(r_data,'-->',res)
                                    data_tuple=r_data,j
                                    #print(data_tuple)
                                    data.append(data_tuple)
                                    break
   
    #print(file_details)
    #print(data)
    for i in file_details:
        for j in range(len(data)):
            if i == data[j][0]:
                file_list.append(data[j][1])
        output[i]=file_list
        file_list=[]
    with open('result.csv', 'w') as f:
        for key in output.keys():
            f.write("%s,%s\n"%(key,output[key]))
    



     
def add_path():
    path=input("Enter the path\n\n")    
    path_details.append(path)
    os.system('cls')
    path_info()

def edit_path():
    print("1. Rename the path\n\n2. Delete the path\n")
    p_ch=int(input("Enter the chooise\n\n"))
    if p_ch==1:
        print("\n\nCheck the path Details\n\n")
        s_no=0        
        for j in path_details:
            print(s_no,'\t',j)
            s_no=s_no+1
        
        file_ch=int(input("Enter the File number\n\n"))
        
        new_path=input("Enter the New path\n\n")
        
        path_details[file_ch]=new_path
        os.system('cls')
        path_info()
    elif p_ch==2:
        print("\n\nCheck the path Details\n\n")
        d_no=0        
        for k in path_details:
            print(d_no,'\t',k)
            d_no=d_no+1
        d_ch=int(input("Enter the File number\n\n"))
        del path_details[d_ch]
        os.system('cls')
        path_info() 
        
def verify_path_info():
        print("\n\nVerify the path Details\n\n")
        s_no=0
        path_empty=[]
        if path_empty == path_details:            
            print("PATH not available\n\n")
        for j in path_details:
            print(s_no,'\t',j)
            s_no=s_no+1
        back=input("Do you go back (Y/N)\n\n")
        if back ==('y'or'Y'):
            path_info()
            
def path_conformation():    
    fix_ch=input("Do you Fix the Path (Y/N)\t")
    if fix_ch==('y'or'Y'):
        requirement(path_details)
    elif fix_ch==('n'or 'N'):
        home()
    else:
        print("input is mismatch Enter correct input\n\n")
        path_conformation()
        
def path_info():
        print("\t\t\t      *******PATH INFO******   \n\n")
        print("\n\n1. Add Path from Folder \n\n2. Edit path form Folder\n\n3. Verify path Folder\n\n4. back\n\n")
        path_ch=int(input("Enter the choice\n"))
        if path_ch==1:
            add_path()            
        elif path_ch==2:
            edit_path()
        elif path_ch==3:
            verify_path_info()
        elif (path_ch==4) or (str(path_ch)=='b'):
            os.system('cls')
            home()
        else:
            print("incorrect command\n try agin \n\n")
            # path_ch=int(input("Enter the choice\n"))
    
def home():
    print("\n\n\t\t\t      *******MAIN INFO******   \n\n")
    print("\n\n1. Path\n\n2. RESULT\n\n3. cancel\n\n")
    ch=int(input("Enter the choice\n"))
    try:
        if ch ==1:
            os.system('cls')
            path_info()        
        elif ch==2:
            path_conformation()
        elif ch==3:
            exit()
        else:
            print("invalied ")
            os.system("cls")
            home()
    except:
        print("invalied")


if __name__=='__main__':
    path_details=[]
    home()
    
    #print(path_details)