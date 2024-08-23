from flask import Flask, request, jsonify

import sqlite3

conn = sqlite3.connect('machine.db') 
c = conn.cursor()

app = Flask(__name__)

@app.route("/info", methods=["GET"])
def get_info():
    c.execute('select * from register')
    info = c.fetchall()
    machines = []
    for machine in info:
        machines.append({'machine_id':machine[1], 'machine_name':machine[2]})
    return {'result':machines}

@app.route("/register", methods=["POST"])
def set_machine():
    request_data = request.get_json()
    try:
        c.execute("insert into register (machine_id, machine_name) values ('"+ request_data['machine_id']+"', '"+request_data['machine_name']+"')")
        conn.commit()
        return {'result':'success'}
    except:
        return {'result':'failed'}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)