import os
print(os.getcwd())
from .app import app as application

if __name__ == '__package__':
	# print(app)
	application.run(host = '0.0.0.0', port = 8000)
