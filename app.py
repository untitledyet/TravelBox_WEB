import random
import sms_validation
import datetime

from flask import Flask, render_template, request
import psycopg2
import smsoffice

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    link = request.form['link']
    phone = "+995" + request.form['phone']
    expiration_day = request.form['expiration_day']
    print(expiration_day)
    code = request.form['sms_code']

    current_date = datetime.datetime.now().date()
    print(current_date)
    future_date = current_date + datetime.timedelta(days=(int(expiration_day) + 1))
    print(future_date)
    expiration_date = future_date.strftime('%Y-%m-%d')

    conn = psycopg2.connect(database="MyAuto",
                            user="doadmin",
                            password="AVNS_ccDIJkyd8h2KOE23NtN",
                            host="db-postgresql-fra1-89602-do-user-13590454-0.b.db.ondigitalocean.com",
                            port="25060")

    if phone == sms_validation.phone_number and int(code) == int(sms_validation.sms_code):
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO links_table (link, phone, expiration_date) VALUES (%s, %s, %s)",
            (
                link, phone, expiration_date))
        conn.commit()
        cur.close()
        conn.close()
        return "Your form was submitted successfully!"
    else:
        return "Verification Code is Wrong!"


@app.route('/send_sms_code', methods=['POST'])
def send_sms_code():
    phone = request.json.get('phone')
    code = random.randrange(1000, 9999)

    sms_validation.phone_number = "+995" + str(phone)
    sms_validation.sms_code = code

    smsoffice.smsoffice_send(phone, code)
    print('SMS code sent to', phone)
    return 'SMS code sent to {}'.format(phone)


if __name__ == '__main__':
    app.run(debug=True)
