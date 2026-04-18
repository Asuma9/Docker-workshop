import sys # module that gives access to system specific functions maintained by the interpreter.
# to 

import pandas as pd


# 1. Importing/Load data to VS code
df = pd.read_csv('ObjectionsR.csv')

#checking the nature/characteristics of the data
#print(df.shape) A general feel
#print(df.columns.tolist())   printing all columns
#print(df.dtypes)   Printing the data types
#print(df.isnull().sum())    Checking if there are null values

# 2. Strip spaces from column names
df.columns = df.columns.str.strip()

# 3. Define amount columns to numeric
col_amount = ['Amount Assessed', 'Amount Objected', 'Amount Dropped', 'Agreed Amount', 'Non-Agreed Amount'] #creates a list

for col in col_amount:
    df[col] = df[col].str.strip() #remove spaces within and adjuscent to the figures
    df[col] = df[col].str.replace(',', '', regex=False)  #replace commas with 0
    df[col] = df[col].str.replace('-', '0', regex=False) #replace dashes with 0
    df[col] = pd.to_numeric(df[col], errors='coerce') #convert string to numeric


# 4. Convert date columns to datetime
col_dates = ['Objection Date', 'Objection Validation date', 'Objection Decision Date', 'If YES, date effected on iTax']

for col in col_dates:
    df[col] = pd.to_datetime(df[col], errors= 'coerce')

# 5. Convert percentage Dropped to numeric
df['Percentage Dropped'] = df['Percentage Dropped'].str.replace('%', '', regex = False)
df['Percentage Dropped'] = pd.to_numeric(df['Percentage Dropped'], errors = 'coerce')

# 6. Final Verification of all datatypes are correct
print(df.dtypes)


#print('arguments', sys.argv) # prepare the terminal/system to start taking arguments

#month = int(sys.argv[1]) # declaring an argument/variable month and instructing the system to call the script pipeline.py as the first argument

#print(f'Hello pipeline, month = {month}') # Receive input from the terminal, process it based on the script instructions, print the result of the operation back to the terminal after processing it
