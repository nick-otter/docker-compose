from flask import Flask
from redis import Redis

app = Flask(__name__)

# Redis is the hostname of the redis container on the application's network
# 6379 is the default port
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    count = redis.incr('hits')
    return 'Hello Bind Mount Test! I have been seen {} times.\n'.format(count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
