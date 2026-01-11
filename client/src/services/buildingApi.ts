import axios from "axios";

type Geometry =
  | {
      type: "Point";
      coordinates: number[];
    }
  | {
      type: "LineString";
      coordinates: number[][];
    }
  | {
      type: "Polygon";
      coordinates: number[][][];
    }
  | {
      type: "MultiPolygon";
      coordinates: number[][][][];
    };

type BuildingProperties = {
  data_source: string;
};

export type BuildingFeature = {
  type: "Feature";
  id: number | string;
  properties: BuildingProperties;
  geometry: Geometry;
};

export type BuildingsResponse = {
  type: string;
  features: BuildingFeature[];
};

export const fetchBergenBuildings = async (): Promise<BuildingsResponse> => {
  const { data } = await axios.get<BuildingsResponse>(
    `${import.meta.env.VITE_BACKEND_BASE_URL}/buildings`,
    {
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
    },
  );
  return data;
};
