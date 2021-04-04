from models.database import db
from sqlalchemy import Column, String, Integer

class Device(db.Model):
    query: db.Query
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    state = Column(String, nullable=False, default='Production')
    ip_address = Column(String, nullable=True)
    hardware_model = Column(String, nullable=True)
    network_role = Column(String, nullable=True)
    org_unit = Column(String, nullable=True)


    def __init__(self, name, state = 'Production'):
        self.name = name
        self.state = state

    def __str__(self):
        print(f'name: {self.name}')
