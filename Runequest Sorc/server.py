from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def main():
    skill = 0
    meditate = 0
    day = "Godday"
    week = "Disorder"
    season = "Sea"
    place = "None"
    item = "None"
    passion = 0
    bonus = 0

    fire = "None"
    earth = "None"
    water = "None"
    air = "None"
    moon = "None"
    dark = "None"
    harmony = "None"
    disorder = "None"
    stasis = "None"
    move = "None"
    truth = "None"
    illusion = "None"
    fertility = "None"
    death = "None"
    man = "None"
    beast = "None"
    otras = "None"

    resultado = 0

    if request.method == 'POST':
        fire = request.form.getlist('fire')
        earth = request.form.getlist('earth')
        water = request.form.getlist('water')
        air = request.form.getlist('air')
        moon = request.form.getlist('moon')
        dark = request.form.getlist('dark')
        harmony = request.form.getlist('harmony')
        disorder = request.form.getlist('disorder')
        stasis = request.form.getlist('stasis')
        move = request.form.getlist('move')
        truth = request.form.getlist('truth')
        illusion = request.form.getlist('illusion')
        fertility = request.form.getlist('fertility')
        death = request.form.getlist('death')
        man = request.form.getlist('man')
        beast = request.form.getlist('beast')
        otras = request.form.getlist('otras')
        skill = request.form['skill']
        meditate = request.form['meditate']
        day = request.form['day']
        week = request.form['week']
        season = request.form['season']
        place = request.form['place']
        item = request.form['item']
        passion = request.form['passion']
        bonus = request.form['bonus']

    meditatebonus = int(meditate) * 5

    daybonus = 0
    if day == "Freezeday":
        if dark:
            daybonus += 10
        if earth:
            daybonus += -10
    if day == "Waterday":
        if water:
            daybonus += 10
        if fire:
            daybonus += -10
    if day == "Clayday":
        if earth:
            daybonus += 10
        if air:
            daybonus += -10
    if day == "Windday":
        if air:
            daybonus += 10
        if water:
            daybonus += -10
    if day == "Fireday":
        if fire:
            daybonus += 10
        if dark:
            daybonus += -10
    if day == "Wildday":
        if not (air or fire or water or earth or dark or moon):
            daybonus += 10

    weekbonus = 0
    if week == "Disorder":
        if disorder:
            weekbonus += 10
        if harmony:
            weekbonus += -10
    if week == "Harmony":
        if harmony:
            weekbonus += 10
        if disorder:
            weekbonus += -10
    if week == "Death":
        if death:
            weekbonus += 10
        if fertility:
            weekbonus += -10
    if week == "Fertility":
        if fertility:
            weekbonus += 10
        if death:
            weekbonus += -10
    if week == "Stasis":
        if stasis:
            weekbonus += 10
        if move:
            weekbonus += -10
    if week == "Movement":
        if move:
            weekbonus += 10
        if stasis:
            weekbonus += -10
    if week == "Illusion":
        if illusion:
            weekbonus += 10
        if truth:
            weekbonus += -10
    if week == "Truth":
        if truth:
            weekbonus += 10
        if illusion:
            weekbonus += -10

    seasonbonus = 0
    if season == "Sea":
        if water:
            seasonbonus += 5
        if fire:
            seasonbonus += -15
    if season == "Fire":
        if fire:
            seasonbonus += 5
        if dark:
            seasonbonus += -15
    if season == "Earth":
        if earth:
            seasonbonus += 5
        if air:
            seasonbonus += -15
    if season == "Darkness":
        if dark:
            seasonbonus += 5
        if earth:
            seasonbonus += -15
    if season == "Storm":
        if air:
            seasonbonus += 5
        if water:
            seasonbonus += -15

    placebonus = 0
    if place == "Minor":
        placebonus += 10
    if place == "Mayor":
        placebonus += 20
    if place == "Great":
        placebonus += 30

    itembonus = 0
    if place == "Comun":
        itembonus += 10
    if place == "Magic":
        itembonus += 20

    resultado = int(skill) + int(meditatebonus) + int(daybonus) + int(weekbonus) + int(
        seasonbonus) + int(placebonus) + int(itembonus) + int(passion) + int(bonus)

    return render_template('main.html', resultado=resultado, skill=skill, passion=passion, bonus=bonus)


if __name__ == '__main__':
    app.run()
