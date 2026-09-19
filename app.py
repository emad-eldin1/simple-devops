import os
import redis
from flask import Flask, jsonify

app = Flask(__name__)
r = redis.Redis(host=os.getenv("REDIS_HOST", "localhost"), port=6379, decode_responses=True)


@app.get("/")
def home():
    try:
        count = r.incr("visits")
    except redis.RedisError:
        count = "redis offline"
    return f"<h1>Simple DevOps App</h1><p>Visits: {count}</p>"


@app.get("/health")
def health():
    return jsonify(status="ok")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
