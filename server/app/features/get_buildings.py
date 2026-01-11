from typing import Any

from fastapi import APIRouter, Depends
from shapely import wkb
from shapely.geometry import mapping
from sqlmodel import Session, select

from app.common.deps import get_session
from app.core.entites import Building

router = APIRouter()


@router.get("/")
def get_buildings(session: Session = Depends(get_session)):
    buildings = get_all_buildings(session)
    response = convert_buildings_to_geojson(buildings)
    return response


def get_all_buildings(session: Session) -> list[Building]:
    minx, miny, maxx, maxy = 5.2, 60.3, 5.5, 60.5
    from sqlalchemy import func
    envelope = func.ST_MakeEnvelope(minx, miny, maxx, maxy, 4326)
    stmt = select(Building).where(func.ST_Intersects(Building.geom, envelope))
    result = session.exec(stmt).all()
    return list(result)


def convert_buildings_to_geojson(buildings: list[Building]) -> dict[str, Any]:
    features: list[dict[str, Any]] = []

    for building in buildings:
        data = building.geom.data
        shapely_geom = wkb.loads(bytes(data))
        geometry = mapping(shapely_geom)

        feature = {
            "type": "Feature",
            "id": building.id,
            "properties": {
                "data_source": building.data_source,
            },
            "geometry": geometry,
        }

        features.append(feature)

    return {
        "type": "FeatureCollection",
        "features": features,
    }
