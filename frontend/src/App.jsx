import { useState } from "react";
import { summarizeMeeting } from "./services/api";

function App() {
  const [text, setText] = useState("");
  const [summary, setSummary] = useState("");

  const handleClick = async () => {
    const result = await summarizeMeeting(text);

    setSummary(result.summary);
  };

  return (
    <div>
      <h1>Meeting AI</h1>

      <textarea rows="10" cols="50" onChange={(e) => setText(e.target.value)} />

      <br />

      <button onClick={handleClick}>요약</button>

      <h2>{summary}</h2>
    </div>
  );
}

export default App;
