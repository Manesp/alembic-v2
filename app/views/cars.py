from flask import Blueprint, jsonify,request
from ..models.cars import Cars
app = Blueprint("cars", __name__)



@app.route('/cars',methods=['GET'])
def get_car():
    query_params = request.args.to_dict()
    car = Cars.list_by(query_params)
    return jsonify([r.serialize() for r in car])


@app.route("/cars", methods=["POST"])
def create():
    car = Cars.create(**request.json)
    return jsonify(car.serialize())

@app.route("/cars", methods=["DELETE"])
def delete():
    car = Cars.find(**request.json)
    car.delete_all()

@app.route("/cars", methods=["PUT"])
def update():
    car = Cars.bulk_update(**request.json)