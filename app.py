from flask import Flask, request
import psycopg2
from psycopg2 import sql

app = Flask(__name__)

def save_code_to_db(code, table_name, column_name):
    conn = psycopg2.connect(database="travelbox_db",
                            user="doadmin",
                            password="AVNS_i-7e1eOujhl8LWLX-yu",
                            host="travelbox-do-user-14253771-0.b.db.ondigitalocean.com",
                            port="25060")
    cursor = conn.cursor()

    insert_query = sql.SQL("INSERT INTO {} ({}) VALUES (%s);").format(
        sql.Identifier(table_name),
        sql.Identifier(column_name)
    )
    cursor.execute(insert_query, [code])

    conn.commit()
    cursor.close()
    conn.close()

@app.route('/bogpay_authorization/<code>', methods=['GET'])
def handle_authorization(code):
    save_code_to_db(code, "bogpay_codes", "temp_codes")
    return "Code saved to the 'bogpay_codes' table."

@app.route('/bog_payment/<code>', methods=['GET'])
def handle_payment(code):
    save_code_to_db(code, "bog_payment", "pay_codes")
    return "Code saved to the 'payment_codes' table."

if __name__ == '__main__':
    app.run(debug=True)
