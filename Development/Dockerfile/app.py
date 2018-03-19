from flask import Flask
from redis import Redis, RedisError
import os
import socket

redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def hello():
  html = "<h3>Hello {name}!</h3>" \
         "You successfully run a <strong>python website :)</strong>"
  return html.format(name=os.getenv("NAME"))

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80)
