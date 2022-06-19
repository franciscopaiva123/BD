#!/usr/bin/python3
import psycopg2, cgi
import login

form = cgi.FieldStorage()
product_ean = form.getvalue('product')

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>List of Replenishment</title>')
print('</head>')
print('<body>')

connection = None
try:
		# Creating connection
		connection = psycopg2.connect(login.credentials)
		cursor = connection.cursor()

		# Making query
		sql = 'SELECT ean, instant, units FROM replenishment_event WHERE ean = %(ean)s;'
		data = {'ean':product_ean}
		cursor.execute(sql, data)
		result = cursor.fetchall()

		print('<h2>List of replenishments from prouct {}</h2>'.format(product_ean))
		# Displaying results
		print('<table border="5" cellspacing="5">')
		print('<tr><td>ean</td><td>date</td><td>units</td></tr>')
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