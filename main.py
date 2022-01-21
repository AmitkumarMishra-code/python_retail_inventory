# Schedule Library imported
import schedule
import time
import psycopg2
import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Content

load_dotenv()

conn = psycopg2.connect(
    host=os.environ.get("host"),
    user=os.environ.get("user"),
    password=os.environ.get("password"),
    database=os.environ.get("database")
)

mycursor = conn.cursor()


def schedule_task():
    mycursor.execute("SELECT * from production.Categories")
    categories = mycursor.fetchall()
    low_inventory = []
    for x in categories:
        check_inventory(x[0], x[1], low_inventory)
    send_mail(low_inventory)


def send_mail(low_inventory):
    report = "<br>".join(low_inventory)
    message = Mail(
        from_email=os.environ.get("from_email"),
        to_emails=os.environ.get("to_email"))
    message.subject = "ALERT: Low stocks report"
    message.content = Content("text/html", report)
    try:
        sg = SendGridAPIClient(os.environ.get('sendgrid_api_key'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)


def check_inventory(category_id, category_name, low_inventory):
    mycursor.execute("SELECT count(*) from production.Products Where category_id = % s" % category_id)
    result = mycursor.fetchall()
    if result[0][0] < 35:
        low_inventory.append("Stock count of {} : {}".format(category_name, result[0][0]))


schedule.every(6).hours.do(schedule_task)
# comment out the above line, and uncomment the line below to have a quicker turnaround time for demo
# schedule.every(60).seconds.do(schedule_task)


while True:
    schedule.run_pending()
    time.sleep(1)