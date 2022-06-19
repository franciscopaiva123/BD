#!/usr/bin/python3
import psycopg2
import cgi
from login import credentials

form = cgi.FieldStorage()
# getvalue uses the names from the form in previous page
category_name = form.getvalue('cat_name')

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Removing Category</title>')
print('</head>')
print('<body>')
connection = None
try:
    # Creating connection
    connection = psycopg2.connect(credentials)
    cursor = connection.cursor()

    print('<h3 style="text-align:center;">Category {} removed</h3>'.format(category_name))

    sql = 'DELETE FROM consists_of WHERE super_cat = %(name)s;'
    data = {'name': category_name}
    cursor.execute(sql, data)

    sql = 'DELETE FROM super_category WHERE name = %(name)s;'
    data = {'name': category_name}
    cursor.execute(sql, data)

    sql = 'DELETE FROM category WHERE name = %(name)s;'
    data = {'name': category_name}
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
