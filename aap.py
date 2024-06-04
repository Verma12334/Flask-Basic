from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET"])
def welcome():
   return "<h1>Welcome to Saurabh Python Web Application</h1>"

@app.route("/index", methods=["GET"])
def index():
   return "<h2>Welcome to the Saurabh Index Page</h2>"

@app.route('/success/<float:score>')
def success(score):
   return "The person has passed, and the score is: {}".format(score)

@app.route('/fail/<float:score>')
def fail(score):
   return "The person has failed, and the score is: {}".format(score)

@app.route('/form', methods=["GET","POST"])
def form():
   if request.method == "GET":
       return render_template('form.html')
   else:
       try:
           maths = float(request.form['maths'])
           science = float(request.form['science'])
           history = float(request.form['history'])

           average_marks = (maths + science + history) / 3

           result = "success" if average_marks >= 50 else "fail"

           return redirect(url_for(result, score=average_marks))

       except Exception as e:
           error_message = "An error occurred: {}".format(str(e))
           return render_template('error.html', error=error_message)

@app.route('/api', methods=["POST"])
def calculate_sum():
   data = request.get_json()
   a_value = float(data['a'])
   b_value = float(data['b'])
   result = a_value + b_value
   return jsonify(result=result)

if __name__ == "__main__":
   app.run(debug=True)
