from flask import Flask
from flask import request
from flask import jsonify
import mysql.connector
import json

def retrieve_projects_and_total(code_postal, statut):
    liste_villes = ["Montreuil"]
    liste_resultats = []
    total = 0
    con = mysql.connector.connect(user='testuser', password='password',host='127.0.0.1',database='projets_immobiliers')
    cursor = con.cursor()
    query = ("SELECT a.numero, a.rue, c.surface,p.creation_date, p.ca FROM adresse a, parcelle c, projet p WHERE a.adresse_id = c.adresse_id AND c.codepostal = %s AND p.status = %s AND p.parcelle_id = c.parcelle_id;")
    cursor.execute(query, (code_postal,statut))
    for(numero, rue, surface, creation_date, ca) in cursor:
        liste_resultats.append(("{} {} | {} m2 | {:%d %b %Y} | {} euros".format(numero, rue, surface, creation_date, ca)))
        temp_dict = {"numero" : numero, "rue": rue, "surface": surface, "creation_date": str(creation_date), "ca": ca}
        total = total + ca
    liste_resultats.append("Total : " + str(total))
    cursor.close
    con.close()
    return liste_resultats

def retrieve_json():
    liste_villes = ["Montreuil"]
    liste_resultats_json = []
    con = mysql.connector.connect(user='testuser', password='password',host='127.0.0.1',database='projets_immobiliers')
    cursor = con.cursor()
    query = ("SELECT a.numero, a.rue, c.surface,p.creation_date, p.ca FROM adresse a, parcelle c, projet p WHERE a.adresse_id = c.adresse_id AND c.ville = %s AND p.parcelle_id = c.parcelle_id;")
    cursor.execute(query, (liste_villes[0],))
    for(numero, rue, surface, creation_date, ca) in cursor:
        temp_dict = {"numero" : numero, "rue": rue, "surface": surface, "creation_date": str(creation_date), "ca": ca}
        liste_resultats_json.append(temp_dict)
    jsonified_list = liste_resultats_json
    cursor.close
    con.close()
    return jsonified_list

app = Flask(__name__)

@app.route('/projets/')
def list_all_projects():
    code_postal = request.args.get('code_postal')
    statut = request.args.get('statut')
    liste_resultats = retrieve_projects_and_total(code_postal, statut)
    if liste_resultats is None:
        return "<div>No project found</div>"
    result = "<div>"
    for ligne in liste_resultats:
        result += "<p>" + ligne + "</p><br>"
    result += "</div>"
    return result

@app.route('/projets/json')
def list_all_projects_json():
    return jsonify(retrieve_json())


if __name__ == "__main__":
    app.run()
