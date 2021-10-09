from flask import Flask
app = Flask('')

@app.route('/')
def main():
	return 'sever'
if __name__="__main__":
	app.run()
