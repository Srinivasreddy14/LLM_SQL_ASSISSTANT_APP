# pip install db-sqlite3
# pip install sqlite3
import sqlite3
import pandas as pd

#Connectt to SQlite
# Step 1: Connect to SQLite database (or create one if not exists)
connection=sqlite3.connect("bank_database.db")

#step 2: Reading the bank dataset
df=pd.read_csv('bank.csv',sep=';')

# step 3: Create a cursor object to insert record,create table
cursor=connection.cursor()

# Step 4: Store the DataFrame in a SQL table called "bank_accounts"
df.to_sql('bank_accounts', connection, if_exists='replace', index=False)

# Step 5: Confirm storage
print("Bank dataset stored successfully in SQLite database.")

# Step 6: Read back the data to confirm
stored_df = pd.read_sql("SELECT * FROM bank_accounts", connection)
print(stored_df)

#Disspaly ALl the records
for row in stored_df:
    print(row)

#Commit your changes int he databse
connection.commit()
connection.close()