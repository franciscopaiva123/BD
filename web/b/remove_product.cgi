#!/usr/bin/python3
import cgi

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Removing a Product and its Suppliers</title>')
print('</head>')
print('<body>')

# The string has the {}, the variables inside format() will replace the {}
print('<h3 style="text-align:center;">Removing a Product and its Suppliers.</h3>')

# The form will send the info needed for the SQL query
print('<form action="remove.cgi" method="post">')
print('<p>Product ean: <input type="text" name="product_ean"/></p>')
print('<p><input type="submit" value="Submit"/></p>')
print('</form>')

print('</body>')
print('</html>')


