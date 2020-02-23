import requests
import numpy as np


if __name__ == "__main__":
	features = [0.53003534,0.49338521,0.,1.,0.,0.]
	print(features)
	data = {'features': features}
	response = requests.post('http://127.0.0.1:5000/predict', json=data)
	print(response.text)