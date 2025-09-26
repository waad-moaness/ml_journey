from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

# When someone visits /ping in the browser (http://localhost:9696/ping)

# Using the HTTP GET method (default method browsers use)

# Flask will call the ping() function.
@app.route('/ping', methods= ['GET'])
def ping():
    return 'اعرعرعرعرعرعر\n'

@app.route('/user/<username>')
def show_user_profile(username):
    return f"hello {username}\n"

@app.route('/user/<int:user_id>')
def show_user_id(user_id):
    return f"user id: {user_id}\n"

@app.route('/greeting')
@app.route('/greeting/<name>')
def greet(name= None):
    return render_template('greeting.html',name=name)

@app.route('/form', methods=["GET", "POST"])
def form_test():
    if request.method == "POST":
        username = request.form['username']
        return f'''
          <div style="display: inline-block;">
    <h1 style="text-align: center; font-size:20px; color:#333; margin-bottom:10px;">
        Hello {username}
    </h1>
    <img src="../static/photo_2025-09-27_01-31-34.jpg" 
         alt="User photo" 
         style="width:400px; height:300px; border-radius:10px; border:1px solid #aaa;">
</div>


          '''
    else:
        return '''
        <form method="POST" style="border:1px solid #ccc; padding:20px; border-radius:10px; width:300px; background:#f9f9f9;">
    <label for="username" style="font-size:18px; display:block; margin-bottom:10px; color:#333;">
        Enter your name pookie:
    </label>
    <input type="text" id="username" name="username" required
           style="width:100%; padding:10px; font-size:16px; border:1px solid #aaa; border-radius:5px; margin-bottom:15px;">
    <button type="submit" 
            style="background:#4CAF50; color:white; font-size:16px; padding:10px 15px; border:none; border-radius:5px; cursor:pointer;">
        Submit
    </button>
</form>



        '''
# This makes sure the app runs only when you run this file directly
if __name__ == "__main__" :
    app.run(debug = True , host = '0.0.0.0', port= 9696)