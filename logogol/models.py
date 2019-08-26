from sqlalchemy import Column, Integer, String, Boolean
from logogol.database import Base


class Link(Base):
    __tablename__ = "links"
    id = Column(Integer, primary_key=True)
    url = Column(String)
    paths = Column(String)
    description = Column(String)
    tags = Column(String)

    def __init__(self, url, description=None, paths=None, tags=None):
        self.url = url
        self.paths = paths
        self.description = description
        self.tags = tags

    def __repr__(self):
        return "<Link: {}>".format(self.url)
