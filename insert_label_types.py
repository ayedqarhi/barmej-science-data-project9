import psycopg2 as ps
conn = ps.connect(user='postgres', password='123pass', host='ip-172-31-33-3', port='5432', database='postgres')
cursor = conn.cursor()
SQL = "INSERT INTO label_types(label_id,label_name,comments)"
SQL += " VALUES(1,'positive','Positive feeling'),"
SQL += "(0,'negative','Negative feeling'),"
SQL += "(2,'neutral','Neutral feeling')"
cursor.execute(SQL)
conn.commit()
cursor.close()
conn.close()
