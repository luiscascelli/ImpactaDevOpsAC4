import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)


@app.route('/')
def fibonacci():
    f = [1, 1]
    i = 0
    while len(f) < 50:
        f.append(f[i] + f[i+1])
        i += 1
    listToStr = ' '.join(map(str, p))
    return listToStr


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
