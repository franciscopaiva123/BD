#!/usr/bin/python3
import psycopg2

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Change designation</title>')
print('</head>')
print('<body>')

# The form will send the info needed for the SQL query
print('<form action="change_designation.cgi" method="post">')
print('<p>Product EAN: <input type="text" name="product"/></p>')
print('<p>New Designation: <input type="text" name="designation"/></p>')
print('<p><input type="submit" value="Submit"/></p>')

print('</form>')



print('</body>')
print('</html>')