import os
from json import dumps
from flask import Flask, render_template, g, Response, request, flash
from .form import information

app = Flask(__name__)
app.config['SECRET_KEY'] = '1ab9de06181bac4b9570dcf327d7ce32'


def calculate(toefl, sop, lor, cgpa, gre, research, multiplier):
    admissionStats = [1, -1.105280744, 0.000781828, -0.010980987, 0.051714645, 0.124596912, 0.001658085656,
                      -0.004544239,
                      2, -1.32206708, 0.004320261, -0.01200476, 0.014918234, 0.13834353, 0.001128329046, 0.01044434,
                      3, -1.14118044, 0.000894195, -0.00616229, 0.018245858, 0.124920362, 0.001965994538, 0.02835693,
                      4, -1.29195377, 0.00582672, 0.028679426, 0.010749526, 0.085650437, 0.001503631127, 0.03807761,
                      5, -0.74113308, 0.003677915, 0.028972354, 0.003952278, 0.070261534, 0.001044124364, 0.073593]

    interceptCoeff = admissionStats[(multiplier - 1) * 8 + 1]
    toeflCoeff = admissionStats[(multiplier - 1) * 8 + 2]
    sopCoeff = admissionStats[(multiplier - 1) * 8 + 3]
    lorCoeff = admissionStats[(multiplier - 1) * 8 + 4]
    cgpaCoeff = admissionStats[(multiplier - 1) * 8 + 5]
    greCoeff = admissionStats[(multiplier - 1) * 8 + 6]
    researchCoeff = admissionStats[(multiplier - 1) * 8 + 7]

    results = (interceptCoeff + (toeflCoeff * toefl) + (sopCoeff * sop)
               + (lorCoeff * lor) + (cgpaCoeff * cgpa) + (greCoeff * gre)
               + (researchCoeff * research))

    finalResults = round(results * 100, 2)

    return finalResults

@app.route('/')
def get_ori():
    return render_template("index.html")


@app.route("/information.html", methods=['GET', 'POST'])
def admission():
    form = information()

    if form.validate_on_submit():
        toefl = form.data['toeflScore']
        sop = form.data['sopScore']
        lor = form.data['lorScore']
        cgpa = form.data['cgpaScore']
        gre = form.data['greScore']
        research = form.data['research']
        uniRating = form.data['uniRating']

        if (research.upper() == "YES"):
            research = 1.0
        elif (research.upper() == "NO"):
            research = 0.0

        results = calculate(toefl, sop, lor, cgpa, gre, research, uniRating)

        finalResults = str(results)

        if (results < 0):
            flash(f'Your chances are 0%', 'success')
        elif (results > 100):
            flash(f'Your chances are 100%', 'success')
        else:
            flash(f'Your chances are: ' + finalResults + '%', 'success')

    return render_template('information.html', form=form)

@app.route('/index.html')
def get_index():
    return render_template("index.html")

@app.route('/index/GRE.html')
def get_index_gre():
    return render_template("index/GRE.html")

@app.route('/index/TOEFL.html')
def get_index_toefl():
    return render_template("index/TOEFL.html")

@app.route('/index/CGPA.html')
def get_index_cgpa():
    return render_template("index/CGPA.html")

@app.route('/index/Research.html')
def get_index_research():
    return render_template("index/Research.html")

@app.route('/index/SOP.html')
def get_index_sop():
    return render_template("index/SOP.html")

@app.route('/index/LOR.html')
def get_index_lor():
    return render_template("index/LOR.html")

@app.route('/index_2.html')
def get_index_2():
    return render_template("index_2.html")

@app.route('/index_2/GRE.html')
def get_index_2_gre():
    return render_template("index_2/GRE.html")

@app.route('/index_2/TOEFL.html')
def get_index_2_toefl():
    return render_template("index_2/TOEFL.html")

@app.route('/index_2/CGPA.html')
def get_index_2_cgpa():
    return render_template("index_2/CGPA.html")

@app.route('/index_2/Research.html')
def get_index_2_research():
    return render_template("index_2/Research.html")

@app.route('/index_2/SOP.html')
def get_index_2_sop():
    return render_template("index_2/SOP.html")

@app.route('/index_2/LOR.html')
def get_index_2_lor():
    return render_template("index_2/LOR.html")


@app.route('/index_3.html')
def get_index_3():
    return render_template("index_3.html")

@app.route('/index_3/GRE.html')
def get_index_3_gre():
    return render_template("index_3/GRE.html")

@app.route('/index_3/TOEFL.html')
def get_index_3_toefl():
    return render_template("index_3/TOEFL.html")

@app.route('/index_3/CGPA.html')
def get_index_3_cgpa():
    return render_template("index_3/CGPA.html")

@app.route('/index_3/Research.html')
def get_index_3_research():
    return render_template("index_3/Research.html")

@app.route('/index_3/SOP.html')
def get_index_3_sop():
    return render_template("index_3/SOP.html")

@app.route('/index_3/LOR.html')
def get_index_3_lor():
    return render_template("index_3/LOR.html")


@app.route('/index_4.html')
def get_index_4():
    return render_template("index_4.html")

@app.route('/index_4/GRE.html')
def get_index_4_gre():
    return render_template("index_4/GRE.html")

@app.route('/index_4/TOEFL.html')
def get_index_4_toefl():
    return render_template("index_4/TOEFL.html")

@app.route('/index_4/CGPA.html')
def get_index_4_cgpa():
    return render_template("index_4/CGPA.html")

@app.route('/index_4/Research.html')
def get_index_4_research():
    return render_template("index_4/Research.html")

@app.route('/index_4/SOP.html')
def get_index_4_sop():
    return render_template("index_4/SOP.html")

@app.route('/index_4/LOR.html')
def get_index_4_lor():
    return render_template("index_4/LOR.html")

@app.route('/index_5.html')
def get_index_5():
    return render_template("index_5.html")

@app.route('/index_5/GRE.html')
def get_index_5_gre():
    return render_template("index_5/GRE.html")

@app.route('/index_5/TOEFL.html')
def get_index_5_toefl():
    return render_template("index_5/TOEFL.html")

@app.route('/index_5/CGPA.html')
def get_index_5_cgpa():
    return render_template("index_5/CGPA.html")

@app.route('/index_5/Research.html')
def get_index_5_research():
    return render_template("index_5/Research.html")

@app.route('/index_5/SOP.html')
def get_index_5_sop():
    return render_template("index_5/SOP.html")

@app.route('/index_5/LOR.html')
def get_index_5_lor():
    return render_template("index_5/LOR.html")
