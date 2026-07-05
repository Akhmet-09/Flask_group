from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return "Welcome to the Home Page!"

# Route for an about page
@app.route('/about')
def about():
    return "This is the About Page."

# Route with a dynamic parameter
@app.route('/tel')
def tel():
    return "This is the Tel Page."

# Usinday etip @app.route('/) dep aship keteberesen!
# Bilshirap atpa basqa zat jazaman dep, tek usini jaz basqa zat jazpa!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#Terminalda py main.py dep kor!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Run the app if this file is executed directly
if __name__ == '__main__':
    app.run(debug=True)