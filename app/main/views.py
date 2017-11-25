from flask import render_template, jsonify
from sqlalchemy import func

from . import main
from .. import db
from ..models import User, HighScore

@main.route('/highScore')
def highScore():
    highScore = HighScore.query.order_by(HighScore.username).first()
    if highScore is None:
        return jsonify(username="None", score=0)
    return jsonify(username=highScore.username, score=highScore.highScore)

@main.route('/newhighScore/<userName>/<newScore>')
def newhighScore(userName, newScore):
    HighScore.query.delete()
    newHighScore = HighScore(username=userName, highScore=newScore)
    db.session.add(newHighScore)
    db.session.commit()
    return jsonify(username=newHighScore.username, score=newHighScore.highScore)

@main.route('/')
def index():
    return render_template('main/index.html')

@main.route('/Categories')
def Categories():
    return render_template('main/Categories.html')

@main.route('/FourthPage')
def fourthPage():
    return render_template('main/FourthPage.html')

@main.route('/FifthPage')
def fifthPage():
    return render_template('main/FifthPage.html')
