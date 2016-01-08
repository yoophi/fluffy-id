import redis
import time
from flask import Flask, jsonify

__version__ = '0.0.1'


def gen_guid(shard_id=1):
    r = redis.Redis(host='localhost', port=6379, db=0)
    incr = r.incr('guid')

    guid = (int(time.time() * 1000) << (64 - 41))
    guid |= (shard_id << (64 - 41 - 13))
    guid |= incr % 1024

    return guid


app = Flask(__name__)


@app.route('/')
def index():
    return 'guid server.'


@app.route('/guid')
@app.route('/guid/<int:shard_id>')
def guid(shard_id=1):
    return jsonify({'shard_id': shard_id, 'guid': gen_guid(shard_id)})
