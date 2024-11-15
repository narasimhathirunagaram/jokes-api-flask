from flask import Flask, jsonify
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import requests

app = Flask(_name_)
DATABASE_URI = 'sqlite:///jokes.db'
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Joke(Base):
    _tablename_ = 'jokes'
    id = Column(Integer, primary_key=True)
    category = Column(String)
    type = Column(String)
    joke = Column(String, nullable=True)
    setup = Column(String, nullable=True)
    delivery = Column(String, nullable=True)
    nsfw = Column(Boolean)
    political = Column(Boolean)
    sexist = Column(Boolean)
    safe = Column(Boolean)
    lang = Column(String)

Base.metadata.create_all(engine)

@app.route('/fetch_jokes', methods=['GET'])
def fetch_jokes():
    url = "https://v2.jokeapi.dev/joke/Any?amount=10"
    response = requests.get(url)
    
    if response.status_code == 200:
        jokes_data = response.json().get('jokes', [])

        for joke_data in jokes_data:
            joke = Joke(
                category=joke_data.get('category'),
                type=joke_data.get('type'),
                joke=joke_data.get('joke') if joke_data.get('type') == 'single' else None,
                setup=joke_data.get('setup') if joke_data.get('type') == 'twopart' else None,
                delivery=joke_data.get('delivery') if joke_data.get('type') == 'twopart' else None,
                nsfw=joke_data.get('flags', {}).get('nsfw', False),
                political=joke_data.get('flags', {}).get('political', False),
                sexist=joke_data.get('flags', {}).get('sexist', False),
                safe=joke_data.get('safe', True),
                lang=joke_data.get('lang')
            )
            session.add(joke)
        
        session.commit()
        return jsonify({"message": "Jokes fetched and stored successfully!"}), 201
    else:
        return jsonify({"error": "Failed to fetch jokes from JokeAPI"}), 500

@app.route('/validate_jokes', methods=['GET'])
def validate_jokes():
    try:
        # Count the rows in the jokes table
        count = session.query(Joke).count()
        return jsonify({"message": f"Number of jokes in the database: {count}"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000, debug=True)