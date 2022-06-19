#!/usr/bin/python3
import psycopg2
import cgi
from login import credentials

form = cgi.FieldStorage()
# getvalue uses the names from the form in previous page
category_name = form.getvalue('cat_name')
super_cat_name = form.getvalue('super_cat_name')
super = form.getvalue('super')
simple = form.getvalue('simple')

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Adding new Sub-Category</title>')
print('</head>')
print('<body>')
connection = None
try:
    # Creating connection
    connection = psycopg2.connect(credentials)
    cursor = connection.cursor()
    print('<h3 style="text-align:center;">Sub-Category name = {}</h3>'.format(category_name))
    if simple == "true":    
     sql = 'INSERT INTO category VALUES (%(name)s);' 
     data = {'name': category_name}
     cursor.execute(sql, data)
    
     sql = 'INSERT INTO simple_category VALUES (%(name)s);'
     data = {'name': category_name}
     cursor.execute(sql, data)

     sql = 'INSERT INTO consists_of VALUES (%(sup)s,%(name)s);'
     data = {'name': category_name,'sup': super_cat_name}
     cursor.execute(sql, data)

    else:
     sql = 'INSERT INTO category VALUES (%(name)s);' 
     data = {'name': category_name}
     cursor.execute(sql, data)
    
     sql = 'INSERT INTO super_category VALUES (%(name)s);'
     data = {'name': category_name}
     cursor.execute(sql, data)

     sql = 'INSERT INTO consists_of VALUES (%(sup)s,%(name)s);'
     data = {'name': category_name,'sup': super_cat_name}
     cursor.execute(sql, data)
    connection.commit()

    # Closing connection
    cursor.close()
except Exception as e:
    # Print errors on the webpage if they occur
    print('<h1>An error occurred.</h1>')
    print('<p>{}</p>'.format(e))
    connection.rollback()
finally:
    if connection is not None:
        connection.close()
print('</body>')
print('</html>')
