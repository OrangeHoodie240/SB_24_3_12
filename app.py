"""Flask app for Cupcakes"""
from flask import Flask, jsonify, request, render_template
from models import db, connect_db, Cupcake


app = Flask(__name__) 

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SQLALCHEMY_ECHO'] = True
connect_db(app)



@app.route('/api/cupcakes', methods=['GET'])
def get_all_cupcakes():
    cupcakes = Cupcake.query.all() 
    cupcakes = [Cupcake.serialize(cupcake) for cupcake in cupcakes]
    return  jsonify(cupcakes=cupcakes)

@app.route('/api/cupcakes/<int:id>', methods=['GET'])
def get_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=Cupcake.serialize(cupcake))

@app.route('/api/cupcakes', methods=['POST'])
def add_cupcake():
    data = request.get_json()
    flavor = data.get('flavor', None)
    size = data.get('size', None)
    rating = data.get('rating', None)
    image = data.get('image', None)
    
    if(None in [flavor, size, rating]):
        raise ValueError(str([flavor, size, rating]))

    cupcake = Cupcake.add(flavor, size, rating, image)
    return jsonify(cupcake=Cupcake.serialize(cupcake)), 201

@app.route('/api/cupcakes/<int:id>', methods=['PATCH'])
def update_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id) 

    data = request.get_json() 
    cupcake.flavor = data.get('flavor', cupcake.flavor)
    cupcake.size = data.get('size', cupcake.size)
    cupcake.rating = data.get('rating', cupcake.rating)
    cupcake.image = data.get('image', cupcake.image)
    db.session.commit() 

    return jsonify(cupcake=Cupcake.serialize(cupcake))



@app.route('/api/cupcakes/<int:id>', methods=['DELETE'])
def delete_cupcake(id):
    Cupcake.query.get_or_404(id)
    Cupcake.query.filter(Cupcake.id==id).delete()
    db.session.commit() 

    return jsonify({"message": "Deleted"})

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
