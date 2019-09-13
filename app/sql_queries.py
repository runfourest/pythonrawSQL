# example queries, will be different across different db platform

sqlserver_extract = ('''
  SELECT sqlserver_column_1
  FROM sqlserver_table
''')

sqlserver_insert = ('''
  INSERT INTO table (column_1)
  VALUES (?)  
''')

mysql_extract = ('''
  SELECT mysql_column_1, 
  FROM mysql_table
''')

mysql_insert = ('''
  INSERT INTO table (column_1)
  VALUES (?)  
''')

# exporting queries
class SqlQuery:
  def __init__(self, extract_query, load_query):
    self.extract_query = extract_query
    self.load_query = load_query
    
# create instances for SqlQuery class
sqlserver_query = SqlQuery(sqlserver_extract, sqlserver_insert)
mysql_query = SqlQuery(mysql_extract, mysql_insert)

# store as list for iteration
sqlserver_queries = [sqlserver_query]
mysql_queries = [mysql_query]