from flask import render_template, request
from sqlalchemy import select
from sqlalchemy.orm import aliased

from mk8d import app
from mk8d import db
from mk8d.models import Cup, CupTrack, Track


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/cup/<cup_type>/<cup_name>")
def cup(cup_type, cup_name):
    Cup_alias = aliased(Cup, name="Cup_alias")
    table = db.session.execute(
            select(Cup, Track, CupTrack, Cup_alias)
            .join(Cup_alias, Track.original_cup == Cup_alias.id)
            .filter(Cup.id == CupTrack.cup_id,
                    CupTrack.track_id == Track.id,
                    Track.original_cup == Cup_alias.id,
                    Cup.name == cup_name)
            .order_by(CupTrack.track_order)
            ).all()

    if table:
        return render_template("cup.html",
                               title=cup_name,
                               cup_name=cup_name,
                               cup_type=cup_type,
                               table=table)
    else:
        return render_template("404.html")
