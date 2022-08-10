import pandas as pd
import numpy as np
import os




def create_all_dataset(file_name):
    
    
    print(os.getcwd())
    print(os.listdir())
    xls = pd.ExcelFile("./"+file_name)
    df1 = pd.read_excel(xls, 'Analysis',skiprows=6,header=1)

    col_list = list(df1.columns.values)

    final_column_list_sem1 = list(col_list[3:30:6])

    for i in col_list[33:45:4]:
        final_column_list_sem1.append(i)



    final_column_list_sem1.append(col_list[45])


    temp_df = df1.to_numpy()
    final_l_sem1 = []

    for j in range(2,len(df1)):
        templist = []
        r = temp_df[j][2:30:3]
        for i in range(len(r)):
            if i%2!=0:
                templist.append(r[i])
        k = temp_df[j][36:46:4]
        for value in k:
            templist.append(value)
        
        templist.append(temp_df[j][47])
        final_l_sem1.append(templist)




    for i in range(final_l_sem1.count([np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan])):
        final_l_sem1.remove([np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan])


    df_sem1 = pd.DataFrame(final_l_sem1, columns = final_column_list_sem1)
    df_sem1.to_csv('./datasets/sem1.csv')


    col_list = list(df1.columns.values)


    final_column_list_sem2 = list(col_list[48:len(col_list)-24:6])


    for i in col_list[len(col_list)-23:len(col_list)-8:4]:
        final_column_list_sem2.append(i)


    final_l_sem2 = []

    for j in range(2,len(df1)):
        templist = []
        r = temp_df[j][50::3]
        for i in range(10):
            if i%2==0:
                templist.append(r[i])
        
        k = temp_df[j][81:93:4]
        for value in k:
            templist.append(value)
        
        templist.append(temp_df[j][92])
        # final_l_sem1.append(templist)
        final_l_sem2.append(templist)


    for i in range(final_l_sem2.count([np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan])):
        final_l_sem2.remove([np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan])



    df_sem2 = pd.DataFrame(final_l_sem2, columns = final_column_list_sem2)
    df_sem2.to_csv('./datasets/sem2.csv')


    col_list = list(df1.columns.values)
    aggregate_col_list = col_list[len(col_list)-8::]
    print(aggregate_col_list)

    aggregate_val_list = []

    for j in range(2,len(df1)):
        
        r = list(temp_df[j][93:])
        
        
        
        aggregate_val_list.append(r)

    temp_index_list = []
    for i in range(len(aggregate_val_list)):
        if np.nan in  aggregate_val_list[i]:
            temp_index_list.append(i)
        

    for _ in temp_index_list:
        aggregate_val_list.pop()

    print(len(aggregate_val_list))

    df_aggr  = pd.DataFrame(aggregate_val_list,columns=aggregate_col_list)
    df_aggr.to_csv('./datasets/final.csv')


    temp_details_col_list = col_list[:3]

    temp_arr = []

    for j in range(2,77):
        
        r = temp_df[j][:3:]
        if np.nan not in r:

            temp_arr.append(r)

    df_details = pd.DataFrame(data=temp_arr,columns=temp_details_col_list)
    
    df_details.to_csv('./datasets/details.csv')

    return True
