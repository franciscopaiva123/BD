#!/usr/bin/python3
import psycopg2, cgi
import login

form = cgi.FieldStorage()
product_ean = form.getvalue('product')
designation = form.getvalue('designation')

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Change designation of a Product</title>')
print('</head>')
print('<body>')

connection = None
try:
		# Creating connection
		connection = psycopg2.connect(login.credentials)
		cursor = connection.cursor()

		# Making query
		sql = 'UPDATE product SET descr = %(descr)s WHERE ean = %(ean)s;'
		data = {'descr':designation, 'ean':product_ean}
		print('<p>The designation of the product {} has been modified</p>'.format(data['ean']))
		cursor.execute(sql, data)

		connection.commit()

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