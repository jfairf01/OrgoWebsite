from flask import render_template

from . import SnEMechs


@SnEMechs.route('/')
def index():
    return render_template('SnEMechs/index.html')

@SnEMechs.route('/Sn_2')
def Sn2():
    return render_template('SnEMechs/Sn2.html')

@SnEMechs.route('/Sn_2/Learning')
def Sn2Learning():
    return render_template('SnEMechs/Sn2/Learning.html')

@SnEMechs.route('/Sn_2/Learning/Mechanisms/1')
def Sn2Mech1():
    return render_template('SnEMechs/Sn2/Mechanisms/Slide1.html')

@SnEMechs.route('/Sn_2/Learning/Mechanisms/2')
def Sn2Mech2():
    return render_template('SnEMechs/Sn2/Mechanisms/Slide2.html')

@SnEMechs.route('/Sn_2/Learning/Reaction_Conditions')
def Sn2RxnConds():
    return render_template('SnEMechs/Sn2/Reactions/index.html')

@SnEMechs.route('/Sn_2/Problems')
def Problems():
    return render_template('SnEMechs/Sn2/problems.html')