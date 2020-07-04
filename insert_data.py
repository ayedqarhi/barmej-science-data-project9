import psycopg2 as ps
import pandas as pd
import datetime

data = pd.read_csv('imdb_dataset.csv')
review = data['review']
sentiment = data['sentiment']

conn = ps.connect(user='postgres', password='123pass', host='ip-172-31-33-3', port='5432', database='postgres')
cursor = conn.cursor()

# data_input table
for i, row in enumerate(review):
	d = datetime.datetime.now()
	SQL = "INSERT INTO data_input(inpt_id,input_text,input_date) VALUES(%s,%s,%s)"
	VAL = (i+1, row, d)
	cursor.execute(SQL, VAL)

conn.commit()

# label_types
SQL = "SELECT label_id,label_name FROM label_types"
cursor.execute(SQL)
rows = cursor.fetchall()
conn.commit()

label_types_dict = {}
for r in rows:
	label_types_dict[r[1]] = r[0]

# data_labeling
for i, row in enumerate(sentiment):
	d = datetime.datetime.now()
	SQL = "INSERT INTO data_labeling(id_text,id_label,label_date) VALUES(%s,%s,%s)"
	VAL = (i+1, label_types_dict[row], d)
        cursor.execute(SQL, VAL)

conn.commit()

cursor.close()
conn.close()
