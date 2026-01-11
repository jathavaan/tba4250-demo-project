import "./App.css";
import { useGetBergenBuildings } from "./hooks/buildingHook.ts";
import { Map } from "./components/Map.tsx";

function App() {
  const { data, isLoading, error } = useGetBergenBuildings();
  if (isLoading) return <h3>Loading...</h3>;
  if (error) return <h3>Error: {error.message}</h3>;
  return (
    <div style={{ width: "100%", height: "100%" }}>
      <Map buildings={data ?? []} />
    </div>
  );
}

export default App;
