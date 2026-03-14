import axios from "axios";

export const summarizeMeeting = async (text) => {
  const res = await axios.post("http://localhost:8000/summarize", {
    text: text,
  });

  return res.data;
};
