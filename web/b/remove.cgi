#!/usr/bin/python3
import psycopg2
import cgi
from login import credentials

form = cgi.FieldStorage()
# getvalue uses the names from the form in previous page
product_ean = form.getvalue('product_ean')

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Removing a Product and its Suppliers</title>')
print('</head>')
print('<body>')
connection = None
try:
    # Creating connection
    connection = psycopg2.connect(credentials)
    cursor = connection.cursor()

    # Making query remove primary supplier
    sql = 'DELETE FROM supplies_prim WHERE ean = (%(ean)s);'
    data = {'ean': product_ean}
    cursor.execute(sql, data)

    # Making query remove secondary supplier
    sql = 'DELETE FROM supplies_sec WHERE ean = (%(ean)s);'
    data = {'ean': product_ean}
    cursor.execute(sql, data)
    
    # Making query remove the product from the Replenishment Event
    sql = 'DELETE FROM replenishment_event WHERE ean = (%(ean)s);'
    data = {'ean': product_ean}
    cursor.execute(sql, data)
    
    # Making query remove the product from the PLanogram
    sql = 'DELETE FROM planogram WHERE ean = (%(ean)s);'
    data = {'ean': product_ean}
    cursor.execute(sql, data)
    
    # Making query remove the product
    sql = 'DELETE FROM product WHERE ean = (%(ean)s);'
    data = {'ean': product_ean}
    cursor.execute(sql, data)

    # Commit the update (without this step the database will not change)
    connection.commit()

    print('<h3>Product {} was sucessfully removed.</h3>'.format(product_ean))

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
