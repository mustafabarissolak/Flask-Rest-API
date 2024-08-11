from app import pdb


class CustomerDevice(pdb.Model):
    __tablename__ = "CustomerDevice"

    id = pdb.Column(pdb.Integer, primary_key=True)
    customerId = pdb.Column(pdb.Integer, pdb.ForeignKey("Customer.id"), nullable=False)
    deviceTypeId = pdb.Column(pdb.Integer, pdb.ForeignKey("DeviceType.id"), nullable=False)
    port = pdb.Column(pdb.String, nullable=False)
    ipHost = pdb.Column(pdb.String, nullable=False)
