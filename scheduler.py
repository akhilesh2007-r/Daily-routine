from apscheduler.schedulers.blocking import BlockingScheduler


def scheduled_report():
    print("Generating daily report...")  # Add your report generation logic here


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    # Schedule the `scheduled_report` function to be called once every day at a specified time.
    scheduler.add_job(scheduled_report, 'cron', hour=14, minute=18)  # Adjust the time as needed
    print("Scheduler started...")
    scheduler.start()