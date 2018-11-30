# compose_flask/app.py
import os
from flask import Flask
import redis
#from elasticsearch import Elasticsearch

#es = Elasticsearch(host=os.environ['ELASTIC_HOST'], port=os.environ['ELASTIC_PORT'])
app = Flask(__name__)
redis = redis.Redis(host=os.environ['REDIS_HOST'], port=os.environ['REDIS_PORT'], db=0)
redis2 = redis.Redis2(host=os.environ['REDIS_HOST2'], port=os.environ['REDIS_PORT2'], db=0)

@app.route('/')
def hello():
    text = """
    redis_host: %s
    redis_port: %s
    pg_pass: %s
    elastic_host: %s
    """
    return text % (os.environ['REDIS_HOST'], os.environ['REDIS_PORT'], os.environ['REDIS_HOST2'], os.environ['REDIS_PORT2'], os.environ['PG_PASS'], os.environ['ELASTIC_HOST'])


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
