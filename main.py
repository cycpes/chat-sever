from flask import Flask
app = Flask('')

@app.route('/')
def main():
	return 'sever'
