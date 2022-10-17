from mk8d import db


class Cup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __repr__(self):
        return f"<id = {self.id}, cup name = {self.name}>"


class Track(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    original_cup = db.Column(db.Integer, db.ForeignKey("cup.id"),
                             nullable=False)

    def __repr__(self):
        return (f"<id = {self.id},"
                f"track name = {self.name},"
                f"original cup = {self.original_cup}>")


class CupTrack(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cup_id = db.Column(db.Integer, db.ForeignKey("cup.id"),
                             nullable=False)
    track_id = db.Column(db.Integer, db.ForeignKey("track.id"),
                             nullable=False)
    track_order = db.Column(db.Integer)


    def __repr__(self):
        return (f"<id = {self.id},"
                f"cup id = {self.cup_id},"
                f"track id = {self.track_id}>")
