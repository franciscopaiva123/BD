import psycopg2
import cgi

ist_id = 'ist196737'
host = 'db.tecnico.ulisboa.pt'
port = 5432
password = 'nknv1556'
db_name = ist_id

dsn = f'host={host} port={port} user={ist_id} password={password} dbname={db_name}'
connection = None

form = cgi.FieldStorage()
acct_num = form.getvalue('account')


#Page header code


try:
    connection = psycopg2.connect(dsn)
    print(f'<p>Connected to Postgres with: {dsn}.</p>')

    cursor = connection.cursor()
    sql = 'SELECT * FROM account WHERE account_number = %s;'
    cursor.execute(sql,[acct_num])

    result = cursor.fetchall()

    row_count = len(result)
    print('<p>How many rows: {}</p>'.format(row_count))
    col_count = len(cursor.description)
    print('<p>How many columns: {}</p>'.format(col_count))

    print('<table border=“5”>');
    for row in result:
        print('<tr>')
        for value in row:
            print(f'<td>{value}</td>')
        print('</tr>')
    print('</table>');

    cursor.close()
    print('<p>Test completed successfully.</p>')
    connection.close()

except Exception as error:
    print('<h1>An error occurred.</h1>')
    print(f'<p>{error}</p>')
finally:
    if connection is not None:
        connection.close()
