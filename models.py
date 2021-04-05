"""Models for Cupcake app."""

from flask_sqlalchemy import SQLAlchemy 


db = SQLAlchemy()

def connect_db(app):
    db.app = app 
    db.init_app(app)


class Cupcake(db.Model):
    __tablename__ = 'cupcakes'

    id = db.Column(db.Integer, primary_key = True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, nullable=False, default='https://tinyurl.com/demo-cupcake')

    @classmethod
    def serialize(cls, cupcake):
        return {
            'id': cupcake.id, 
            'flavor': cupcake.flavor,
            'size': cupcake.size, 
            'rating': cupcake.rating, 
            'image': cupcake.image   
        }

    @classmethod
    def add(cls, flavor, size, rating, image):
        cupcake = cls(flavor=flavor, size=size, rating=rating, image=image)
        db.session.add(cupcake)
        db.session.commit()
        return cupcake
    

