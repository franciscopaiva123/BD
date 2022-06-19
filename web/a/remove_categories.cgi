#!/usr/bin/python3
import cgi

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Removing Category</title>')
print('</head>')
print('<body>')

print('<h3 style="text-align:center;">Removing Category</h3>')
# The form will send the info needed for the SQL query
print('<form action="remove_category.cgi" method="post">')
print('<p> To remove a category, it has do be empty(with no associated categories)</p>')
print('<p>Category name : <input type="text" name="cat_name"/></p>')
print('<p><input type="submit" value="Submit"/></p>')
print('</form>')

print('</body>')
print('</html>')
