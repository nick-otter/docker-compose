from flask import Flask
from redis import redis

app = Flask(_name_)

# Redis is the hostname of the redis container on the application's network
# 6379 is the default port
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    count = redis.incr('hits')
    return 'Hello World! I have been seen {} times.\n'.format(count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
