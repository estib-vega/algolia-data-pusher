"""
    the server module is in charge of opening the 
    browser and serving the ui html

    -it communicates to the model through the user interface
    -it receives the GET and POST requests
    -it saves the file in the uploads
    -it responds to the queries with the answers given from the user_interface
"""

from flask import Flask, render_template, send_from_directory, request, jsonify
from flask_restful import Api, Resource, reqparse
import webbrowser, threading

app = Flask(__name__)
api = Api(app)

    

# # class for query processing
# class DocApi(Resource):
#      def post(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument('file')
#         args = parser.parse_args()
#         file = args['file']
#         # file.save('./data.json')
#         print(args)
#         return jsonify({'status': 'ok', 'results': ''})

# # api
# api.add_resource(DocApi, "/api/post_file")

# home
@app.route("/")
def index():
    return render_template("index.html")

# static files - css
@app.route("/css/<path:path>")
def send_css(path):
    return send_from_directory("./templates/css", path)

# posting file
@app.route("/fileupload", methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # save the file locally
        file = request.files['file']
        file.save('./data.json')
        return jsonify({'status': 'ok', 'results': ''})

# start flask server
def run(p):
    app.run(host='localhost', port=p)

# open web browser window
def open_browser(port):
    from time import sleep
    
    # wait a bit so that the server can start
    # before the browser opens
    sleep(0.25)
    # browser = webbrowser.get()
    # run in local host
    url = '127.0.0.1:' + str(port)

    webbrowser.open_new(url)

# start serving and open page
def start(p):
    PORT = p
    # open browser in a separate thread
    # so that it can wait a bit for the server to start running
    t = threading.Thread(target=open_browser, args=(PORT,), daemon=True)
    t.start()
    # run server
    run(PORT)
