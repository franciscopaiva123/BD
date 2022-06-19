#!/usr/bin/python3
import psycopg2
from login import credentials
print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('</head>')
print('<body>')
print('<h3 style="text-align:center;">Insert and remove a new product and its suppliers.</h3>')
connection = None
try:

    # Creating connection
    connection = psycopg2.connect(credentials)
    cursor = connection.cursor()
    print('<td><a href="add_product.cgi">Add Product</a></td>')
    print('<p>')
    print('<td><a href="remove_product.cgi">Remove Product</a></td>')

    # Closing connection
    cursor.close()
except Exception as e:
    # Print errors on the webpage if they occur
    print('<h1>An error occurred.</h1>')
    print('<p>{}</p>'.format(e))
finally:
    if connection is not None:
        connection.close()

print('</body>')
print('</html>')

