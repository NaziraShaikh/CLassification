import falcon

from prediction import Resource

api = application = falcon.API()
prediction = Resource()
api.add_route('/predict', prediction)
