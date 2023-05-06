import json
from http import HTTPStatus
import time

import requests
from apscheduler.schedulers.blocking import BlockingScheduler

from config import Config


def crawl():
    token = config.CRAWLER_TOKEN
    city = config.CRAWLER_CITY
    local_time = time.strftime("%m/%d/%Y, %H:%M", time.localtime())
    weather_info = requests.get(
        f"http://api.weatherapi.com/v1/current.json?key={token}&q={city}&aqi=no"
    )
    if weather_info.status_code != HTTPStatus.OK:
        print(HTTPStatus.INTERNAL_SERVER_ERROR, weather_info.text)

    weather = {
        "time": time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime()),
        "city": json.loads(weather_info.text)["location"]["name"],
        "temp": json.loads(weather_info.text)["current"]["temp_c"],
        "humidity": json.loads(weather_info.text)["current"]["humidity"]
    }

    save_file = open(config.CRAWLER_SAVE_FILE_NAME, "w")
    json_object = json.dumps(weather)
    save_file.write(json_object)
    save_file.close()


config = Config()
crawl()
scheduler = BlockingScheduler()
scheduler.add_job(crawl, "interval", seconds=config.CRAWLER_INTERVAL)
scheduler.start()
