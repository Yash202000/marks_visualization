from secrets import choice
from cv2 import COLORMAP_TWILIGHT_SHIFTED
import pandas as pd
import numpy as np
import math


def get_tables(val):
    df_sem1 = pd.read_csv('./datasets/sem1.csv')
    df_sem2 = pd.read_csv('./datasets/sem2.csv')
    df_details = pd.read_csv('./datasets/details.csv')
    df_final = pd.read_csv('./datasets/final.csv')

    
    if val=='1':
        df = pd.concat([df_details,df_sem1],axis=1)
        val_list = tuple(df.values.tolist())
        col_list = tuple(df.columns.values)

        return {"keys": col_list,"values": val_list}
    elif val=='2':
        df = pd.concat([df_details,df_sem2],axis=1)
        val_list = tuple(df.values.tolist())
        col_list = tuple(df.columns.values)

        return {"keys": col_list,"values": val_list}
    else:
        df = df_final
        val_list = tuple(df.values.tolist())
        col_list = tuple(df.columns.values)

        return {"keys": col_list,"values": val_list}


def give_me_sgpa():
    df_aggr = pd.read_csv('./datasets/final.csv')


    count_10= 0
    count_9= 0
    count_8= 0
    count_7= 0
    count_6= 0
    count_5= 0
    count_4= 0
    count_3= 0
    count_2= 0
    count_1= 0
    count_0 = 0

    temp = list(df_aggr['SGPA'])
    print(temp)
    import math
    for i in range(len(temp)):
        if temp[i]=='-':
            count_0+=1
        elif math.floor(float(temp[i]))==0:
            count_0+=1
        elif math.floor(float(temp[i]))==1:
            count_1+=1
        elif math.floor(float(temp[i]))==2:
            count_2+=1
        elif math.floor(float(temp[i]))==3:
            count_3+=1
        elif math.floor(float(temp[i]))==4:
            count_4+=1
        elif math.floor(float(temp[i]))==5:
            count_5+=1
        elif math.floor(float(temp[i]))==6:
            count_6+=1
        elif math.floor(float(temp[i]))==7:
            count_7+=1
        elif math.floor(float(temp[i]))==8:
            count_8+=1
        elif math.floor(float(temp[i]))==9:
            count_9+=1
        elif math.floor(float(temp[i]))==10:
            count_10+=1



    per_count = [count_0,count_1,count_2,count_3,count_4,count_5,count_6,count_7,count_8,count_9,count_10]

    return tuple(per_count)

    
    
    
    
    
    
    
     


def give_me_ranks():
    df = pd.read_csv('./datasets/final.csv')
    df['Rank'].replace('-',0,inplace=True)
    temp =list(df['Rank'])
    temp = [int(x) for x in temp]
    return tuple(temp)


def give_class():
    df = pd.read_csv('./datasets/final.csv')
    store = list(df['Class'].value_counts().values)
    store = [int(x) for x in store]
    return {"keys": tuple(df['Class'].value_counts().keys()), "values": store}

def get_backlog_details_th():
    df = pd.read_csv('./datasets/final.csv')
    store= list(df['No. of Backlogs(TH)'].value_counts().values)

    store = [ int(x) for x in store]

    return { "keys" :tuple(df['No. of Backlogs(TH)'].value_counts().keys()) ,"values": store}

def get_backlog_details_pr():
    df = pd.read_csv('./datasets/final.csv')
    store= list(df['No. of Backlogs(PR)'].value_counts().values)

    store = [ int(x) for x in store]

    return { "keys" :tuple(df['No. of Backlogs(PR)'].value_counts().keys()) ,"values": store}



def get_backlog_details():
    df = pd.read_csv('./datasets/final.csv')
    store= list(df['Total No. of Backlogs '].value_counts().values)

    store = [ int(x) for x in store]

    return { "keys" :tuple(df['Total No. of Backlogs '].value_counts().keys()) ,"values": store}
    


def get_columns(choice):
    if choice==1:
        df_sem1 = pd.read_csv('./datasets/sem1.csv')
        col_tuple = tuple(df_sem1.columns.values)
    else:
        df_sem2 = pd.read_csv('./datasets/sem2.csv')
        col_tuple = tuple(df_sem2.columns.values)
    return col_tuple

def get_single_column_values(choice):
    
    df_sem1 = pd.read_csv('./datasets/sem1.csv')
    col_list = list(df_sem1.columns.values)
    print(col_list)
    return { "col_name": col_list[choice], "data": tuple(df_sem1[col_list[choice]])}

def get_single_column_values_sem2(choice):
    df_sem2 = pd.read_csv('./datasets/sem2.csv')
    col_list = list(df_sem2.columns.values)
    print(col_list)
    return { "col_name": col_list[choice], "data": tuple(df_sem2[col_list[choice]])}


def give_result_sheet(choice):
    df_details = pd.read_csv('./datasets/details.csv')
    if choice==1:
        df_sem1 = pd.read_csv('./datasets/sem1.csv')
        return pd.concat([df_details,df_sem1],axis=1).to_html()

    elif choice==2:
        df_sem2 = pd.read_csv('./datasets/sem2.csv')
        return pd.concat([df_details,df_sem2],axis=1).to_html()

    elif choice==3:
        df_final = pd.read_csv('./datasets/final.csv')
        return df_final.to_html()
    
