from flask import Flask,jsonify
#from attendance import getAttendance
import pandas as pd
app=Flask(__name__)

@app.route("/")
def welcome():
    info={
        "test":"test sucess",
        "attendance":"/attendance/roll_no/div"
        }
    return jsonify(info)

@app.route("/attendance/<roll_no>/<div>")
def attendance(roll_no,div):
    roll_no=int(roll_no)
    if div=="A":
       df=pd.read_csv("data/A.csv")
        
    if div=="B":
       df=pd.read_csv("data/B.csv")
        
    data=df.loc[df["roll_no"]==roll_no]
    
    if data["310244 ISEE"].values[0] > 50:
        message="power attendace"
    elif data["310244 ISEE"].values[0] < 50 and data["310244 ISEE"].values[0] > 75:
        message="you must have 75 % to grant your semester"
    elif data["310244 ISEE"].values[0] < 75 and data["310244 ISEE"].values[0] > 80:
        message="good attendance"
    elif data["310244 ISEE"].values[0] < 80:
        message="exelent attendace"
        
    result={
    "message":message,
    "Name":str(data["Name "].values[0]),
    "RollNo":str(int(data["Roll"].values[0])),
    "TOC":str(data["310241 TOC"].values[0]),
    "DBMS":str(data["310242 DBMS"].values[0]),
    "SEPM":str(data["310243 SEPM"].values[0]),
    "ISEE":str(data["310244 ISEE"].values[0]),
    "Attendance":str(data["Theory Attendance %"].values[0])
    }
    print(result)
    
    info={
        "test":"test sucess"
        }
    
    return  jsonify(result)
    

app.run(debug=True)