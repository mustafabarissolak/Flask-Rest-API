from app import pdb


class Users(pdb.Model):
    __tablename__ = "Users"

    id = pdb.Column(pdb.Integer, primary_key=True)
    user_name = pdb.Column(pdb.String, nullable=False)
    password = pdb.Column(pdb.String, nullable=False)
