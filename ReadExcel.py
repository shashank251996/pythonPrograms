import pandas as pd

df = pd.read_excel (r'C:\Users\shashank.gupta\Downloads\credentials.xlsx')
df2 = df[df['Ready State']=='Y']

def read_excel_and_filter():
        
    no_of_col = len(df.columns)
    no_of_rows = len(df.axes[0])
    
    no_of_filtered_rows = len(df2.axes[0])
    print("Number of Rows: ", no_of_filtered_rows)
    print(df2)
    
   
    return no_of_filtered_rows


def store_un_to_variables():
    a= read_excel_and_filter()
    mail = df2['Email/Phone no']
    
    for i in range(a):
        email= mail[i]
        
        print("User name  :",email)
        
    return email

def store_password_to_variables(i,b):
    

    passcode = df2[b]
    password = passcode[i] 
    
    return password

read_excel_and_filter()




        
    
    
      

    


    

