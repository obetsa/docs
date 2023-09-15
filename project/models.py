from project import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, unique=True)
    name = db.Column(db.String(500))

    def __repr__(self):
        return '<Post id: {}, name: {}>'.format(self.id, self.name)