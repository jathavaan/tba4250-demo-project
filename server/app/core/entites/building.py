from geoalchemy2 import Geometry
from sqlalchemy import Column
from sqlmodel import SQLModel, Field


class Building(SQLModel, table=True):
    __tablename__ = "buildings"

    id: str = Field(default=None, primary_key=True)
    geom: str = Field(sa_column=Column(Geometry(geometry_type="MULTIPOLYGON", srid=4326), nullable=False))
    data_source: str = Field(default=None)
