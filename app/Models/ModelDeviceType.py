from app import pdb


class DeviceType(pdb.Model):
    __tablename__ = "DeviceType"

    id = pdb.Column(pdb.Integer, primary_key=True)
    deviceType = pdb.Column(pdb.String, nullable=False)
    protocol = pdb.Column(pdb.String, nullable=False)
    command = pdb.Column(pdb.Text, nullable=False)
