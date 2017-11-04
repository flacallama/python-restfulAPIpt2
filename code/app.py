from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)



# # the api works with resources, and each resource must be a class
# # ex class Student inherits from Resource
# class Student(Resource):
#     #this is the old way - @app.route('/student...')
#     def get(self, name):
#         return {'student': name}
#
# api.add_resource(Student, '/student/<string:name>')

items = []

class Item(Resource):
    def get(self, name):
        # for item in items:
        #     if item['name'] == name:
        #         return item
        item = filter(lambda x: x['name'])
        return {"item": None}, 404

    def post(self, name):
        data = request.get_json() #this will give an error without params if header is wrong
        # data = request.get_json(force=True)  #here we don't look at header
        # data = request.get_json(silent=True) #doesnt give error
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201 # 201 is for "created"   202 is accepted/delaying created

class ItemList(Resource):
    def get(self):
        return {"items": items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)  #creates a html page for troubleshooting
