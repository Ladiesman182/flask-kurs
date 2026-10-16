from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        "index.html",
        navn="Amir",
        klasse="2imi",
        fag="IM"
    )

@app.route('/om')
def om():
    return render_template(
        "om.html",
        navn="Leo",
        alder=17,
        språk="ARABISK",
        skole="kuben"
    )

@app.route("/fag")
def fag():
    fagliste = ["Python", "Flask", "HTML", "CSS" ]
    return render_template("Fag.html" , fag=fagliste)



@app.route("/registrering", methods=["GET", "POST"])
def registrering():
    if request.method == "POST":
        navn = request.form["navn"]
        epost = request.form["epost"]
        alder = request.form["alder"]
        kommentar = request.form["kommentar"]

        return render_template(
            "resultat.html",
            navn=navn,
            epost=epost,
            alder=alder,
            kommentar=kommentar
        )     

    return render_template("registrering.html")



if __name__ == "__main__":
    app.run(debug=True)
