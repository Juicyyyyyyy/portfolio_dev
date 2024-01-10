from app import app, db
from flask_ckeditor import CKEditor


with app.app_context():
	db.create_all()

CKEditor(app)

if __name__ == '__main__':
	app.run(debug=True)