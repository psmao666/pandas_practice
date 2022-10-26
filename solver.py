import pandas as pd
import numpy as np

# this is to read the data 
data = pd.read_csv('data.csv')
# convert the csv data into dataframe
df = pd.DataFrame(data)

# q1: simple output
def q1():
    print(df)

# q2: extract the coloumn that has 'python'
def q2():
    result = df[df['programmer'].str.contains("python")]
    return result

# q3: print all the column names

def q3():
    for col in df.columns:
        print(col)

    # alternatively, to print the obj
    # return df.columns

# q4: change the name of the second column to popularity

def q4():
    print(df.rename(columns={'programmer': 'popularity'}))
    # to chagne it permanently, 
    # df.rename(columns={'programer': 'popularity'}, inplace = True)
    print(df)

# q5: count the number of appearance in the column of programmer

def q5():
    print(df.value_counts('programmer'))

# q6: fill nan with the average of upper value and lower value

def q6():
    df['score'] = df['score'].fillna(df['score'].interpolate())
    print(df)

# q7: get the rows that has a > 3 score

def q7():
    df['score'] = df['score'].apply(pd.to_numeric)
    print(df[df['score'] > 3])

if __name__ == "__main__":
    q7()
    # print(q3())