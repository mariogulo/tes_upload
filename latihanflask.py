from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/sensor/data/<suhu>",methods=["GET"])
def entry_data(suhu):
    with open("memorytest.txt","w") as f:
        f.write(suhu)
        f.close()
    return {"nilai suhu":suhu}

# @app.route('/login',methods=["GET"])
# def entry_point():
#     return "login dulu dong!"

# @app.route('/',methods=["GET"])
# def entry_point2():
#     return "hai ini halaman project alat bantu tambal ban"

# @app.route('/data',methods=["POST","GET"])
# def send_data():
#     if request.method == 'POST':
#         return "ini data loo"
#     if request.method == "GET":
#         return "ini data get loo"

# @app.route('/calculator/multiple/<nilai1>/<nilai2>',methods=["GET"])
# def multiple(nilai1,nilai2):
#     hasil = float(nilai1)*float(nilai2)
#     return {"hasil":hasil}

if __name__ == "__main__":
    app.run(debug=True)