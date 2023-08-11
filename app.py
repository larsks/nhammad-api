from flask import Flask, request, jsonify

app = Flask(__name__)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = [0] * (n+1)
        fib[1] = 1
        for i in range(2, n+1):
            fib[i] = fib[i-1] + fib[i-2]
        return fib[n]


@app.route('/', methods=['GET'])  # New route for the root URL
def index():
    return "Welcome to the Fibonacci API"
    
@app.route('/<int:n>', methods=['GET'])
def get_fibonacci(n):
    result = fibonacci(n)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)  # Change the port to 5001 or any other available port

