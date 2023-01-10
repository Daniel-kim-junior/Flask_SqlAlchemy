import os

from flask import Flask
import random
import user


app = Flask(__name__)
@app.route('/')
def index():
    return 'random: <strong>' + str(random.random()) + '</strong>'


@app.route('/create/')
def create():
    return 'create'



@app.route('/read/<int:post_id>/')
def read(post_id):
    return 'Read %d' % post_id

basedir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(basedir, 'db.sqlite')



app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + dbfile
# 비지니스 로직이 끝날때 Commit 실행(DB반영)
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# 수정사항에 대한 TRACK
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# SECRET_KEY
app.config['SECRET_KEY'] = 'jqiowejrojzxcovnklqnweiorjqwoijroi'


user.db.init_app(app)
user.db.app = app
with app.app_context():
    user.db.create_all()



if __name__ == "__main__":
    app.run(debug=True)
