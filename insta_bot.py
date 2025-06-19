from instapy import InstaPy
from instapy import smart_run
import random as r
import schedule
import time

username = "zed_central"
password = "Entermyaccount147$"

def bot():
    session = InstaPy(username, password)
    session.login()

    with smart_run(session):
        session.like_by_tags(["tag_placeholder"], amount=50)
        session.set_do_follow(True, percentage=r.randint(40, 60))
        session.set_do_comment(True, percentage=r.randint(10, 30))
        session.set_comments("Great", "This is cool", "Solid!")

schedule.every().day.at("07:15").do(bot)
schedule.every().day.at("16:37").do(bot)

while True:
    schedule.run_pending()
    time.sleep(15)