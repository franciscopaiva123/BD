#!/usr/bin/python3
import psycopg2
import cgi
from login import credentials

form = cgi.FieldStorage()
# getvalue uses the names from the form in previous page
category_name = form.getvalue('cat_name')
simple = form.getvalue('simple')
super = form.getvalue('super')

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Removing Sub-Category</title>')
print('</head>')
print('<body>')
connection = None
try:
# Creating connection
    connection = psycopg2.connect(credentials)
    cursor = connection.cursor()
    print('<h3 style="text-align:center;">Category name = {}</h3>'.format(category_name))
    if simple == "true":
     sql = 'DELETE FROM consists_of WHERE sub_cat = %(name)s;'
     data = {'name': category_name}
     cursor.execute(sql, data)

     sql = 'DELETE FROM simple_category WHERE name = %(name)s;'
     data = {'name': category_name}
     cursor.execute(sql, data)

     sql = 'DELETE FROM category WHERE name = %(name)s;'
     data = {'name': category_name}
     cursor.execute(sql, data)
    else:
     sql = 'DELETE FROM consists_of WHERE sub_cat = %(name)s;'
     data = {'name': category_name}
     cursor.execute(sql, data)

     sql = 'DELETE FROM super_category WHERE name = %(name)s;'
     data = {'name': category_name}
     cursor.execute(sql, data)

     sql = 'DELETE FROM category WHERE name = %(name)s;'
     data = {'name': category_name}
     cursor.execute(sql, data)
    connection.commit()
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


