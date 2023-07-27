// A custom react hook for making HTTP requests using the Axios library

import { useState, useEffect } from "react";

const useFetch = () => {
  /**
   * A custom React hook for making HTTP requests using the Axios library.
   *
   * @returns An object containing the response data, error message, loading state,
   *          and an `axiosFetch` function to trigger the request.
   */

  const [response, setResponse] = useState([]);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const [controller, setController] = useState();

  const axiosFetch = async (configObj) => {
  // axiosInstance is a custom axios instance 
    const { axiosInstance, method, url, requestConfig = {} } = configObj;

    try {
      setLoading(true);
      const ctrl = new AbortController();
      setController(ctrl);
      const res = await axiosInstance[method.toLowerCase()](url, {
        ...requestConfig,
        signal: ctrl.signal,
      });
      setResponse(res.data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    // useEffect cleanup function
    return () => controller && controller.abort();
  }, [controller]);

  return { response, error, loading, axiosFetch };
};

export default useFetch;
