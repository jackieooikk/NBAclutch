from flask import Flask, jsonify, request
from data.data import Data
import time
import threading


app = Flask(__name__)

def send_messages(data):
    for game in data.live_games:
        if 


def update(data, interval):
    while True:
        time.sleep(interval)
        # print(f"{threading.current_thread().name}")
        data.update_data()
        send_messages(data)
        for game in data.live_games:
            print(game)
            print(game.game_status_text)
            print(game.game_clock)
            print(game.period)

@app.route('/')
def home():
    print(str(current_data))
    return str(current_data)

if __name__ == "__main__":
    current_data = Data()
    thread1 = threading.Thread(target=update, args=(current_data,10))
    thread1.daemon = True
    thread1.start()
    app.run(debug = True, use_reloader=False)
