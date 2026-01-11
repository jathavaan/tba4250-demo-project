import type { BuildingFeature } from "../services/buildingApi.ts";
import { GeoJSON, MapContainer, TileLayer } from "react-leaflet";
import type { Feature, FeatureCollection } from "geojson";
import type { Layer } from "leaflet";

const BUILDING_COLORS = {
  fkb: "#dc2626",
  osm: "#2563eb",
} as const;

export const Map = ({ buildings }: { buildings: BuildingFeature[] }) => {
  const featureCollection: FeatureCollection = {
    type: "FeatureCollection",
    features: buildings,
  };

  return (
    <MapContainer
      center={[60.39, 5.32]}
      zoom={16}
      style={{ height: "100vh", width: "100%" }}
    >
      <TileLayer
        attribution="© OpenStreetMap contributors"
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />

      <GeoJSON
        data={featureCollection}
        style={(feature) => {
          const source = (feature as Feature).properties?.data_source;

          const color =
            source === "fkb" ? BUILDING_COLORS.fkb : BUILDING_COLORS.osm;

          return {
            color,
            weight: 1,
            fillColor: color,
            fillOpacity: 0.45,
          };
        }}
        onEachFeature={(feature, layer: Layer) => {
          const props = feature.properties as {
            data_source?: string;
          };

          const id = feature.id ?? "unknown";
          const source = props?.data_source ?? "unknown";

          layer.bindTooltip(
            `
            <div>
              <strong>ID:</strong> ${id}<br/>
              <strong>Source:</strong> ${source}
            </div>
            `,
            {
              sticky: true,
              direction: "top",
              opacity: 0.75,
            },
          );
        }}
      />
    </MapContainer>
  );
};
