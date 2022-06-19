#!/usr/bin/python3
import psycopg2
import cgi
from login import credentials

form = cgi.FieldStorage()
# getvalue uses the names from the form in previous page
product_ean = form.getvalue('product_ean')
product_name = form.getvalue('product_name')
product_category = form.getvalue('product_category')
prim_supplier_ean = form.getvalue('prim_supplier_ean')
prim_supplier_date = form.getvalue('prim_supplier_date')
sec_supplier_ean = form.getvalue('sec_supplier_ean')
plan_side = form.getvalue('plan_side')
plan_height = form.getvalue('plan_height')
super_nif = form.getvalue('super_nif')
plan_facings = form.getvalue('plan_facings')
plan_units = form.getvalue('plan_units')
plan_loc = form.getvalue('plan_loc')
plan_nr = form.getvalue('plan_nr')
print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Inserting new Product</title>')
print('</head>')
print('<body>')
connection = None
try:
    # Creating connection
    connection = psycopg2.connect(credentials)
    cursor = connection.cursor()

    print('<h3>Product ean {}</h3>'.format(product_ean))
    print('<h3>Product name {}</h3>'.format(product_name))
    print('<h3>Product category {}</h3>'.format(product_category))
    # Making query add product
    sql = 'INSERT INTO product VALUES (%(ean)s, %(name)s, %(category)s);'
    data = {'ean': product_ean,'name': product_name,'category': product_category}
    cursor.execute(sql, data)
    
    # Making query add primary supplier
    sql = 'INSERT INTO supplies_prim VALUES (%(p_ean)s, %(s_ean)s, %(date)s);'
    data = {'p_ean': product_ean,'s_ean': prim_supplier_ean,'date': prim_supplier_date}
    cursor.execute(sql, data)

    # Making query add secundary supplier
    sql = 'INSERT INTO supplies_sec VALUES (%(p_ean)s, %(sec_ean)s);'
    data = {'p_ean': product_ean,'sec_ean': sec_supplier_ean}
    cursor.execute(sql, data)

    # Making query add the product to the Planogram
    sql = 'INSERT INTO planogram VALUES (%(p_ean)s, %(side)s, %(height)s, %(nr)s, %(super)s, %(facings)s, %(units)s, %(loc)s) ;'
    data = {'p_ean': product_ean,'side': plan_side, 'height': plan_height, 'nr': plan_nr, 'super': super_nif, 'facings': plan_facings, 'units': plan_units, 'loc': plan_loc}
    cursor.execute(sql, data)



    # Commit the update (without this step the database will not change)
    connection.commit()
    print('<h3>Product {} was sucessfully added.</h3>'.format(product_ean))

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
