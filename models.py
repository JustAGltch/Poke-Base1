from main import db

class Pokemon(db.Model):
    __tablename__ = 'Pokemon'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable = False)
    picture = db.Column(db.String(80))
    types = db.relationship('Link')

class Types(db.Model):
    __tablename__ = 'Types'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable = False)
    description = db.Column(db.String(255))
    picture = db.Column(db.String(80))

class Link(db.Model):
    
    __tablename__ = 'Link'

    id = db.Column(db.Integer, primary_key=True)
    poke_ID = db.Column(db.Integer, db.ForeignKey('Pokemon.id'), nullable = False)
    types_ID = db.Column(db.Integer, db.ForeignKey('Types.id'), nullable = False)
    types = db.relationship('Types')
    pokemon = db.relationship('Pokemon')
    
    def __repr__(self):
      return(self.types.description[::])