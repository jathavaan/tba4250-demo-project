import {
  type BuildingFeature,
  fetchBergenBuildings,
} from "../services/buildingApi.ts";
import { useEffect, useState } from "react";

export type GetBergenBuildingsState = {
  data: BuildingFeature[] | null;
  isLoading: boolean;
  error: Error | null;
};
export const useGetBergenBuildings = (): GetBergenBuildingsState => {
  const [data, setData] = useState<BuildingFeature[] | null>(null);
  const [isLoading, setIsLoading] = useState<boolean>(true);
  const [error, setError] = useState<Error | null>(null);

  useEffect(() => {
    let isMounted = true;

    fetchBergenBuildings()
      .then((res) => {
        if (isMounted) setData(res.features);
      })
      .catch((err) => {
        if (isMounted) setError(err);
      })
      .finally(() => {
        if (isMounted) setIsLoading(false);
      });

    return () => {
      isMounted = false;
    };
  }, []);

  return { data, isLoading, error };
};
