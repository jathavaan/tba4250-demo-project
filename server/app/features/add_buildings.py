import sys

import duckdb
from fastapi import APIRouter, Depends
from geoalchemy2.shape import from_shape
from shapely import from_wkb
from sqlmodel import Session
import geopandas as gpd

from app.common.deps import get_session
from app.core.entites import Building

router = APIRouter()


@router.post("/")
def add_buildings(session: Session = Depends(get_session)):
    buildings = get_buildings_from_blob_storage()
    session.add_all(buildings)
    session.commit()

    return {"inserted": len(buildings)}


def get_buildings_from_blob_storage() -> list[Building]:
    con = duckdb.connect()
    con.execute("INSTALL spatial;")
    con.execute("LOAD spatial;")
    con.execute("INSTALL azure;")
    con.execute("LOAD azure;")

    if sys.platform == "linux":
        con.execute("SET azure_transport_option_type = curl")

    con.execute(
        """
        CREATE SECRET secret (
            TYPE azure,
            PROVIDER config,
            ACCOUNT_NAME 'doppablobstorage'
        )
        """
    )

    path = "az://data/release/2025-11-21.41/theme=buildings/region=46/*.parquet"

    df = con.execute(
        f'''
        SELECT external_id  AS id, ST_AsWKB(geometry) AS geometry, source AS data_source FROM read_parquet('{path}')
        '''
    ).fetchdf()

    df["geometry"] = df["geometry"].apply(lambda g: bytes(g) if isinstance(g, (memoryview, bytearray)) else g)
    buildings: list[Building] = []

    for row in df.itertuples(index=False):
        shapely_geom = from_wkb(row.geometry)

        buildings.append(
            Building(
                id=row.id,
                geom=from_shape(shapely_geom, srid=4326),
                data_source=row.data_source,
            )
        )

    return buildings
