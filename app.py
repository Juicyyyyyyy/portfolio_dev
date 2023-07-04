from app import app, db


@app.before_first_request
def setup():
	db.create_all()


if __name__ == '__main__':
	app.run(debug=False)
