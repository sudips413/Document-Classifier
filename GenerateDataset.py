import pandas as pd
import os
import sys
import fitz

def get_path():
    path=[]
    path1=input('Enter path for AI files: ')
    print('Path registered!!')
    path2=input('Enter path for WEB files: ')
    print('Path registered!!')
    path.append(path1)
    path.append(path2)
    return path


def get_final_dataframe(path,flag):
    df=pd.DataFrame(columns=['Text','Label'])
    content=[]
    for file in os.listdir(path):
        if file.endswith('.pdf'):
            doc=fitz.open(path+'/'+file)
            content_temp=''
            for page in range(len(doc)):
                content_temp=content_temp+doc[page].get_text()
                #print(content_temp)
            content.append(content_temp)
    df['Text']=content
    df['Label']=flag
    return df

def get_content(file_path):
    df=pd.DataFrame(columns=['Text','Label'])
    print(file_path)
    for path in file_path:
        if '\\AI' in path:
            print('AI path')
            #print(path)
            df_ai=get_final_dataframe(path,1)
            print(df_ai)
        elif '\\WEB' in path:
            print('WEB path')
            #print(path)
            df_web=get_final_dataframe(path,0)
    df=df_ai.append(df_web)
    return df


def data_generate():
    file_path=get_path()
    dataset=get_content(file_path)
    dataset.to_csv('Dataset.csv',index=False)

if __name__=='__main__':
    data_generate()