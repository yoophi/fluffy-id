import redis
import time
from flask import Flask, jsonify

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return 'guid server.'


@app.route('/guid')
@app.route('/guid/<int:shard_id>')
def guid(shard_id=1):
    return jsonify({'shard_id': shard_id, 'guid': (gen_guid(shard_id))})


def gen_guid(shard_id=1):
    r = redis.Redis(host='localhost', port=6379, db=0)
    incr = r.incr('guid')

    guid = (int(time.time() * 1000) << (64 - 41))
    guid |= (shard_id << (64 - 41 - 13))
    guid |= incr % 1024

    return guid


if __name__ == '__main__':
    app.run()
