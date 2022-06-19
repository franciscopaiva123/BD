#!/usr/bin/python3
import cgi

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Removing Category</title>')
print('</head>')
print('<body>')
print('<h3 style="text-align:center;">Removing Sub-Category</h3>')

# The form will send the info needed for the SQL query
print('<form action="remove_sub_category.cgi" method="post">')
print('<p>Category name : <input type="text" name="cat_name"/></p>')
print('<p>Choose Category type</p>')
print('<p>Simple Category: <input type="radio" name="simple" value="true"/></p>')
print('<p>Super Category: <input type="radio" name="super" value="false"/></p>')
print('<p><input type="submit" value="Submit"/></p>')
print('</form>')

print('</body>')
print('</html>')




