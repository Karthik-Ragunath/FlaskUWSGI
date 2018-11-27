from flask import Flask
import json
from .fib import getfib

app = Flask(__name__)
@app.route("/<int:number>", methods=['GET'])
def get_fib(number):
    return json.dumps(getfib(int(number))), 200
    # return "<h1 style='color:blue'>Hello There!</h1>"

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8000)

#uwsgi.ini
# - Listen on all ips for connection to port 80
# - chdir - change current directory to /root/fib
# wsgi-file - Application executable to be called
# Flask has an internal application object to start the process. In our case, it is app object
