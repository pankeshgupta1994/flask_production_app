import os
from app import create_app
from gevent.pywsgi import WSGIServer


app = create_app(os.getenv('APP_ENV') or 'default')
debug = app.config["DEBUG"]
port = int(app.config["PORT"])

if __name__ == '__main__':
	if os.getenv('APP_ENV') == 'production':
		http_server = WSGIServer(('0.0.0.0', port), app, None, 'default')
		http_server.serve_forever()
	else:
		app.run(host='0.0.0.0',port=port,debug=True)

