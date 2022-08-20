import fitz
import pandas as pd
import os

print(os.getcwd())
def get_path():
    final_path=[];
    path1=input("Enter the path for AI files")
    print("Path Registered Sucessfully")
    path2=input("Enter the path for WEB files")
    print("Path Registered Sucessfully")
    final_path.append(path1)
    final_path.append(path2)
    print(f'The final_path is: {final_path}')
    return(final_path)

def get_final_dataframe(path,flag):
    df=pd.DataFrame(columns=["Text",'Labels'])
    content=[]
    for file in os.listdir(path):
        print(f'The os.listdir returns {file}')
        if file.endswith('.pdf'):
            doc=fitz.open(path+'\\'+file)
            content_temp=""
            for page in range(len(doc)):
                content_temp+=doc[page].get_text()
            content.append(content_temp)
    df['Text']=content
    df['Labels']=flag
    print(df)
    return df

def get_content_of_pdf(file_path):
    for path in file_path:
        if '\\AI' in path:
            print("Here is AI files")
            df_ai=get_final_dataframe(path,1)
        else:
            df_web=get_final_dataframe(path,0)
    return df_ai.append(df_web)
def get_content(file_path):
    df=pd.DataFrame(columns=["Text",'Labels'])
    df=get_content_of_pdf(file_path)
    return df

def dataset_generate():
    file_path=get_path()
    dataset=get_content_of_pdf(file_path)
    # print(dataset)
    dataset.to_csv("dataset.csv")

if __name__=='__main__':
    dataset_generate()