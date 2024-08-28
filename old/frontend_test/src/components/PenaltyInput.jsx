import React, { useState } from "react";

const PenaltyInput = () => {
  const [participantId, setParticipantId] = useState("");
  const [gateNumber, setGateNumber] = useState("");
  const [penaltyTime, setPenaltyTime] = useState("");
  const [judgeId, setJudgeId] = useState("");
  const [comment, setComment] = useState("");
  const [attemptNumber, setAttemptNumber] = useState("");
  const [raceId, setRaceId] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await fetch("http://localhost:8000/penalties", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        participant_id: participantId,
        gate_number: gateNumber,
        penalty_time: penaltyTime,
        judge_id: judgeId,
        comment: comment,
        attempt_number: attemptNumber,
        race_id: raceId,
      }),
    });
    const result = await response.json();
    console.log(result);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Participant ID"
        value={participantId}
        onChange={(e) => setParticipantId(e.target.value)}
      />
      <input
        type="text"
        placeholder="Gate Number"
        value={gateNumber}
        onChange={(e) => setGateNumber(e.target.value)}
      />
      <input
        type="text"
        placeholder="Penalty Time"
        value={penaltyTime}
        onChange={(e) => setPenaltyTime(e.target.value)}
      />
      <input
        type="text"
        placeholder="Judge ID"
        value={judgeId}
        onChange={(e) => setJudgeId(e.target.value)}
      />
      <input
        type="text"
        placeholder="Comment"
        value={comment}
        onChange={(e) => setComment(e.target.value)}
      />
      <input
        type="text"
        placeholder="Attempt Number"
        value={attemptNumber}
        onChange={(e) => setAttemptNumber(e.target.value)}
      />
      <input
        type="text"
        placeholder="Race ID"
        value={raceId}
        onChange={(e) => setRaceId(e.target.value)}
      />
      <button type="submit">Submit</button>
    </form>
  );
};

export default PenaltyInput;
