from flask import render_template
from ..models import EditableHTML

from . import main


@main.route('/')
def index():
    return render_template('main/index.html')

@main.route('/SecondPage')
def secondPage():
    return render_template('main/SecondPage.html')

@main.route('/ThirdPage')
def thirdPage():
    return render_template('main/ThirdPage.html')

@main.route('/FourthPage')
def fourthPage():
    return render_template('main/FourthPage.html')

@main.route('/FifthPage')
def fifthPage():
    return render_template('main/FifthPage.html')

@main.route('/about')
def about():
    editable_html_obj = EditableHTML.get_editable_html('about')
    return render_template('main/about.html',
                           editable_html_obj=editable_html_obj)
