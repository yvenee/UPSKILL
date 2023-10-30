from flask import Flask
import redis

app = Flask(__name__)
redis_client = redis.Redis(host='localhost', port=6379)  # Replace with your Redis server details

@app.route('/counter', methods=['GET'])
def get_counter():
    counter_value = redis_client.get('counter')
    return f'Counter value: {counter_value}'

@app.route('/counter', methods=['POST'])
def increment_counter():
    current_value = redis_client.incr('counter')
    return f'Counter incremented. Current value: {current_value}'