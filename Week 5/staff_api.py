from flask import Flask, jsonify, request, abort
import mysql.connector

VERSION='v1'
BASE_URI='/api/' + VERSION
STAFFS="/staffs"
STAFF="/staff"
uri_all_staffs=BASE_URI+STAFFS

app = Flask(__name__)

#Get requests
@app.route(uri_all_staffs, methods=['GET'])
def get_staffs():
    cnx = mysql.connector.connect(user="B00XXXX",
                                  password="XXXXX",
                                  host="scm.ulster.ac.uk",
                                  database="B00XXXXX")

    cursor = cnx.cursor()
    query = ("SELECT * FROM staff")
    cursor.execute(query)
    rows = cursor.fetchall()
    items = []
    for row in rows:
        dict={}
        for (key,value) in zip(cursor.description, row):
            dict[key[0]] = value
        items.append(dict)
    cnx.close()

    return jsonify({'staffs':items}), 200

#returns single record of staff
@app.route(uri_all_staffs+'/<int:id>', methods=['GET'])
def get_staff(id):
    cnx = mysql.connector.connect(user="B00XXXX",
                                  password="XXXXX",
                                  host="scm.ulster.ac.uk",
                                  database="B00XXXXX")

    cursor = cnx.cursor()
    query = ("SELECT * FROM staff WHERE Staff_Id="+ str(id))
    cursor.execute(query)
    row = cursor.fetchone()
    staff = []
    for (key, value) in zip(cursor.description,row):
        staff[key[0]]=value
    cnx.close()

    return jsonify({'staffs':items}), 200

#Post requests
@app.route(uri_all_staffs, methods=['POST'])
def add_staffs():
    if not request.json :
        abort(400)
    cnx = mysql.connector.connect(user="B00XXXX",
                                  password="XXXXX",
                                  host="scm.ulster.ac.uk",
                                  database="B00XXXXX")

    cursor = cnx.cursor()
    sql="INSERT INTO staff ( FirstName, LastName, Campus) " \
         "values ( %s, %s, %s)"
    cursor.execute(sql, ( request.json['FirstName'],
                          request.json['LastName'],
                          request.json['Campus']))
    id = cursor.lastrowid
    cnx.commit()
    sql = "select * from staff where Staff_Id="+str(id)
    cursor.execute(sql)
    row=cursor.fetchone()
    staff={}
    for (key, value) in zip(cursor.description,row):
        staff[key[0]]=value
    cnx.close()

    return jsonify(staff), 201

if __name__ == "__main__":
    app.run(debug=True)
        
