from math import *

from flask import  (
    Flask,
    render_template,
    request
)
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask import jsonify
import math

app = Flask(__name__)
#db_connect = create_engine('sqlite:///dsNhanVien.db')

@app.route('/')
def  index():
    return "<h1> Ko có gì cả </h1>"

@app.route('/login', methods=['GET', 'POST'])
def  login():
    query_parameters = request.args
    vusername = query_parameters.get("username")
    vpassword = query_parameters.get("password")
    return render_template("login.html")

@app.route('/profile')
def  profile():
    return render_template("profile.html")

@app.route('/services')
def  call_services():
    return render_template("call_api.html")

@app.route('/params', methods=['GET'])
def api_filter():
    query_parameters = request.args
    return jsonify(query_parameters)

@app.route('/giaiptb2', methods=['GET'])
def giaiptb2():
    query_parameters = request.args
    a = query_parameters.get("a")
    b = query_parameters.get("b")
    c = query_parameters.get("c")

    a = float(a)
    b = float(b)
    c = float(c)
    
    delta = b*b - (4 * a * c)

    str = "chưa biết có nghiệm hay không ! "
    
    kq = { "Trạng thái" : str , "Hệ Số" : (a, b, c) }
    
    if delta < 0 :
        str = "Vo Nghiem"
        kq = { "Trang Thai" : str }
    else if delta == 0:
        x1 = -b/ (2 * a)
        x2 = -b/ (2 * a)
        str = "Co 2 nghiem"
        kq = { "Trang Thai" : str , "He So" : (x1, x2) }
    else if delta > 0 :
        x1 == -b + math.sqrt(delta) /(2 * a)
        x2 == -b - math.sqrt(delta) /(2 * a)
        str = "Co 2 nghiem"
        kq = { "Trang Thai" : str , "He So" : (x1, x2) }
    else if a + b + c == 0 :
        x1 == 1
        x2 == c/a
        str = "Co 2 nghiem"
        kq = { "Trang Thai" : str , "He So" : (x1, x2) }
    else if a - b + c == 0 :
        x1 == -1
        x2 == -c/a
        str = "Co 2 nghiem"
        kq = { "Trang Thai" : str , "He So" : (x1, x2) }
    else :
        str = "Ko co nghiem"
        kq = { "Trang Thai" : str }
        
    return jsonify(kq)

class Parameters(Resource):
    def get(self, firstParam):
        return "Day la tam so " + firstParam

api = Api(app)
api.add_resource(Parameters, '/parameters/<firstParam>') # Route_1
