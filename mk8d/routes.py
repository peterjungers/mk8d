from flask import render_template, request, url_for
from sqlalchemy import select
from sqlalchemy.orm import aliased

from mk8d import app
from mk8d import db
from mk8d.models import Cup, CupTrack, Track


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/cup/<cup_name>')
def cup(cup_name):
    cup_type = request.args.get("cup_type")

    cup_alias = aliased(Cup)
    table = (db.session.execute(
             select(Cup, Track, CupTrack, cup_alias)
             .join(cup_alias, Track.original_cup == cup_alias.id)
             .filter(Cup.id == CupTrack.cup_id,
                     CupTrack.track_id == Track.id,
                     Track.original_cup == cup_alias.id,
                     Cup.name == cup_name)
             .order_by(CupTrack.track_order)
             ).all()
             )

    return render_template("cup.html",
                           cup_name=cup_name,
                           table=table,
                           cup_type=cup_type)
