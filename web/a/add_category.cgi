#!/usr/bin/python3
import psycopg2
import cgi
from login import credentials

form = cgi.FieldStorage()
# getvalue uses the names from the form in previous page
category_name = form.getvalue('cat_name')
simple = form.getvalue('simple')
super = form.getvalue('super')
simple_cat_name = form.getvalue('simple_cat_name')

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Adding new Category</title>')
print('</head>')
print('<body>')
connection = None
print('<h3 style="text-align:center;">Category name = {}</h3>'.format(category_name))
try:
    # Creating connection
    connection = psycopg2.connect(credentials)
    cursor = connection.cursor()
    if simple == "true":
     sql = 'INSERT INTO category VALUES (%(name)s);' 
     data = {'name': category_name}
     cursor.execute(sql, data)
     sql = 'INSERT INTO simple_category VALUES (%(name)s);'
     data = {'name': category_name}
     cursor.execute(sql, data)
    else:
     sql = 'INSERT INTO category VALUES (%(name)s);'
     data = {'name': category_name}
     cursor.execute(sql, data)
     sql = 'INSERT INTO super_category VALUES (%(name)s);'
     data = {'name': category_name}
     cursor.execute(sql, data)
     sql = 'INSERT INTO consists_of VALUES (%(name)s,%(sub)s);'
     data = {'name': category_name,'sub': simple_cat_name}
     cursor.execute(sql, data)

    connection.commit()

    # Closing connection
    cursor.close()
except Exception as e:
    # Print errors on the webpage if they occur
    print('<h3>An error occurred.</h3>')
    print('<p>{}</p>'.format(e))
    connection.rollback()
finally:
    if connection is not None:
        connection.close()
print('</body>')

print('</html>')
