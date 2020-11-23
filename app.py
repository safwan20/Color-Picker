from flask import Flask, jsonify, request
import logging
from colorPicker import *

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)


@app.route('/pick_color', methods=['POST', 'GET'])
def home() :
	try : 
		if request.method == 'POST' :
			image = request.files['image']
			print(image)
			image.save("savedImages/" + image.filename)
			filename = "savedImages/" + image.filename
			print(filename)
			cp = pickColor(filename)
			print(cp)
			logging.debug(cp)
			return app.make_response((jsonify(cp), 200))
	except :
		return app.make_response((jsonify({"message": "Bad Request"}),400))

	return app.make_response((jsonify({"message": "Send Images"}),200))


app.run(debug=True)
