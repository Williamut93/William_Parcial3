from flask import Flask, jsonify

app = Flask(__name__)

tasks= [
    {"id":1, "frase":"Felicidades Passte william", "active":True},
    {"id":2, "frase":"Tendras 10.", "active":True},
    {"id":3, "frase":"Te veo el siguiente cuatri.", "active":True},
   

]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

if __name__=='__main__':
    app.run(debug=True)