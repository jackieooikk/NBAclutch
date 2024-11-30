from flask import Flask, jsonify, request
from data.data import Data
from user import User
import time
import threading


app = Flask(__name__)

def send_messages(data):

    #look out for live games with 5 minutes left in the 4th and have a point differential of 5 or less 
    user = User(5, 10)

    for game in data.live_games:

        if (game.period == 4 and game.under(user.clutch_time) and game.is_close(user.clutch_points)):
            print("WATCH THIS GAME")
            print(game)
            #send message to user 


def update(data, interval):
    while True:
        time.sleep(interval)
        # print(f"{threading.current_thread().name}")
        data.update_data()
        send_messages(data)

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
