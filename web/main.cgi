#!/usr/bin/python3
import psycopg2

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Supermarket Management WebApp</title>')
print('</head>')
print('<body>')
print('<h3>Supermarket Management WebApp</h3>')



# Displaying results
print('<table border="3" cellspacing="2">')

print('<tr><td><a href="a/main.cgi">Insert and Remove Categories</a></tr></td>')
print('<tr><td><a href="b/add_remove_producs.cgi">Insert end Remove Products</a></tr></td>')
print('<tr><td><a href="c/form_replenishments.cgi">List of Replenishments of a product</a></tr></td>')
print('<tr><td><a href="d/form_designation.cgi">Change Designation of a Product</a></tr></td>')
print('<tr><td><a href="e/form_categories.cgi">List of Sub-Categories of a product</a></tr></td>')

print('</table>')

	
print('</body>')
print('</html>')