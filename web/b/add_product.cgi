#!/usr/bin/python3
import cgi

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Inserting Product</title>')
print('</head>')
print('<body>')

# The string has the {}, the variables inside format() will replace the {}
print('<h3 style="text-align:center;">Add new Product</h3>')
# The form will send the info needed for the SQL query
print('<form action="insert.cgi" method="post">')
print('<p>New Product ean: <input type="text" name="product_ean"/></p>')
print('<p>New Product name: <input type="text" name="product_name"/></p>')
print('<p>New Product Category: <input type="text" name="product_category"/></p>')
print('<p>Product Primary Supplier nif : <input type="text" name="prim_supplier_ean"/></p>')
print('<p>Product Primary Supplier date : <input type="text" name="prim_supplier_date"/></p>')
print('<p>Product Secondary Supplier nif : <input type="text" name="sec_supplier_ean"/></p>')
print('<p>Planogram Side(L or R): <input type="text" name="plan_side"/></p>')
print('<p>Planogram Height(Upper, middle or floor): <input type="text" name="plan_height"/></p>')
print('<p>Corridor nr: <input type="text" name="plan_nr"/></p>')
print('<p>Supermarket Nif: <input type="text" name="super_nif"/></p>')
print('<p>Planogram Facings: <input type="text" name="plan_facings"/></p>')
print('<p>Planogram Units: <input type="text" name="plan_units"/></p>')
print('<p>Planogram Location: <input type="text" name="plan_loc"/></p>')
print('<p><input type="submit" value="Submit"/></p>')
print('</form>')

print('</body>')
print('</html>')

