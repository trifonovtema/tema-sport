import React, { useState } from "react";

const GeneratePDFButton = () => {
  const [pdfUrl, setPdfUrl] = useState("");
  const [raceId, setRaceId] = useState("");
  const [competitionName, setCompetitionName] = useState("");
  const [competitionDate, setCompetitionDate] = useState("");

  const handleGeneratePDF = async () => {
    const response = await fetch(`http://localhost:8003/results/pdf?race_id=${raceId}&competition_name=${competitionName}&competition_date=${competitionDate}`);
    const data = await response.json();
    setPdfUrl(data.pdf_url);
  };

  return (
    <div>
      <input
        type="text"
        placeholder="Race ID"
        value={raceId}
        onChange={(e) => setRaceId(e.target.value)}
      />
      <input
        type="text"
        placeholder="Competition Name"
        value={competitionName}
        onChange={(e) => setCompetitionName(e.target.value)}
      />
      <input
        type="text"
        placeholder="Competition Date"
        value={competitionDate}
        onChange={(e) => setCompetitionDate(e.target.value)}
      />
      <button onClick={handleGeneratePDF}>Generate PDF</button>
      {pdfUrl && (
        <div>
          <a href={pdfUrl} download="results.pdf">Download PDF</a>
        </div>
      )}
    </div>
  );
};

export default GeneratePDFButton;
