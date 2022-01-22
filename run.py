import schedule
import time
import malaysia
import world
import app
import sendmail

def job1():
    print("Its start")
    malaysia.get_data()
    world.get_data()

def job2():
    app.generate_res()

def job3():
    sendmail.send()
    


# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
schedule.every().day.at("23:57:00").do(job1)
schedule.every().day.at("23:57:30").do(job2)
schedule.every().day.at("23:58:30").do(job3)

while 1:
    schedule.run_pending()
    time.sleep(1)