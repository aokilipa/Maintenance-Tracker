from flask_restful import Resource

#creating dtrequest list with dictionary to simulate data store
#using datastructure to simulate data store
dtrequest = [
    {
        "id": 1,
        "requestor":"Alicia Keys",
        "type": "maintenance",
        "status":"Approved",
        "desc": "Description goes here"
    },
    {
        "id": 2,
        "requestor":"John Doe",
        "type": "repair",
        "status":"Pending",
        "desc": "Description goes here"
    },
    {
        "id": 3,
        "requestor":"Susan Doe",
        "type": "maintenance",
        "status":"Approved",
        "desc": "Description goes here"
    },
    {
        "id": 4,
        "requestor":"John Doe",
        "type": "maintenance",
        "status":"Approved",
        "desc": "Description goes here"
    }
]

class RequestResource(Resource):
    def get(self):
        return dtrequest
