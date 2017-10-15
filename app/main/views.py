from flask import render_template

from . import main


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
