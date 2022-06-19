#!/usr/bin/python3
import psycopg2, cgi
import login

form = cgi.FieldStorage()
categorie = form.getvalue('categorie')

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>List of Sub-Categories</title>')
print('</head>')
print('<body>')

connection = None
try:
		# Creating connection
		connection = psycopg2.connect(login.credentials)
		cursor = connection.cursor()

		# Making query
		sql = 	'WITH RECURSIVE all_categories AS (' \
				'SELECT super_cat, sub_cat FROM consists_of WHERE super_cat = %(categorie)s ' \
				'UNION ' \
				'SELECT c.super_cat, c.sub_cat ' \
				'FROM consists_of c INNER JOIN all_categories a ON c.super_cat = a.sub_cat)' \
				'SELECT sub_cat FROM all_categories;'

		data = {'categorie':categorie}
		cursor.execute(sql, data)
		result = cursor.fetchall()

		print('<h2>List of all Sub-Categories From categorie {}</h2>'.format(categorie))
		# Displaying results
		print('<table border="5" cellspacing="5">')
		for row in result:
			print('<tr>')
			for value in row:
			# The string has the {}, the variables inside format() will replace the{}
				print('<td>{}</td>'.format(value))
			print('</tr>')
		print('</table>')

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
