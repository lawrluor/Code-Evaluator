from app import db
from werkzeug.security import check_password_hash, generate_password_hash

# 'extend_existing' allows redefining tables and columns
class User(db.Model):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password, method='scrypt')

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Analysis(db.Model):
    __tablename__ = 'analysis'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    filename = db.Column(db.String(255), nullable=False)
    data = db.Column(db.JSON, nullable=False)  # TODO: change to JSONB?
