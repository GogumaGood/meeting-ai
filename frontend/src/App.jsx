import { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [meetings, setMeetings] = useState([]);
  const [file, setFile] = useState(null);
  const [summary, setSummary] = useState("");

  useEffect(() => {
    loadMeetings();
  }, []);

  const loadMeetings = async () => {
    console.log("loadMeetings");
    const res = await axios.get("http://localhost:8000/loadMeeting");

    setMeetings(res.data);
  };

  const upload = async () => {
    const formData = new FormData();
    formData.append("file", file);

    const res = await axios.post(
      "http://localhost:8000/uploadMeeting",
      formData,
      {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      },
    );

    setSummary(res.data.summary);
  };

  return (
    <div>
      <h1>Meeting AI</h1>

      <input type="file" onChange={(e) => setFile(e.target.files[0])} />

      <button onClick={upload}>회의 요약</button>

      <pre>{summary}</pre>

      <h1>Meeting History</h1>

      {meetings.map((m) => (
        <div key={m.id}>
          <h3>{m.filename}</h3>

          <p>{m.summary}</p>

          <hr />
        </div>
      ))}
    </div>
  );
}

export default App;
