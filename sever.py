from flask import Flask
app = Flask(__name__)

@app.route('/ass')
def main():
	return 'sever'
if __name__=="__main__":
    app.run()
