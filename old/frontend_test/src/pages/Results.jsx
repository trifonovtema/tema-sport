import React, { useEffect, useState } from "react";
import GeneratePDFButton from "../components/GeneratePDFButton";

const Results = () => {
  const [results, setResults] = useState([]);
  const [raceId, setRaceId] = useState("");

  const fetchResults = async () => {
    const response = await fetch(`http://localhost:8003/results?race_id=${raceId}`);
    const data = await response.json();
    setResults(data);
  };

  useEffect(() => {
    if (raceId) {
      fetchResults();
    }
  }, [raceId]);

  return (
    <div>
      <h1>Results</h1>
      <input
        type="text"
        placeholder="Race ID"
        value={raceId}
        onChange={(e) => setRaceId(e.target.value)}
      />
      <button onClick={fetchResults}>Fetch Results</button>
      <table>
        <thead>
          <tr>
            <th>Participant ID</th>
            <th>Start Time</th>
            <th>Finish Time</th>
            <th>Total Time</th>
            <th>Penalties</th>
          </tr>
        </thead>
        <tbody>
          {results.map((result) => (
            <tr key={result.participant_id}>
              <td>{result.participant_id}</td>
              <td>{result.start_time}</td>
              <td>{result.finish_time}</td>
              <td>{result.total_time}</td>
              <td>{result.penalties}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <GeneratePDFButton />
    </div>
  );
};

export default Results;
