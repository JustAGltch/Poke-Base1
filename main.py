from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='/static')  

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pokeBase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# need db to import models
import models

# root route
@app.route('/')
def root():
    return render_template('home.html', page_title='HOME')

@app.route('/all_pokes')
def all_pokes():
    pokemon = models.Pokemon.query.all()
    types = models.Types.query.all()
    #print(pokemon)
    return render_template('all_pokes.html', page_title="ALL pokes", pokemon=pokemon)


# about route - called by ABOUT in the nav bar and returning
# information about the site
@app.route('/about')  # note the leading slash, it’s important
def about():
    return render_template('about.html', page_title='ABOUT')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)