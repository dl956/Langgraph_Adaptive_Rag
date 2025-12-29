import React, { useState } from "react";

function App() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const handleAsk = async () => {
    if (!question.trim()) return;
    setLoading(true);
    setAnswer("");
    try {
      const response = await fetch("/api/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question }),
      });
      if (!response.ok) throw new Error("Request failed");
      const data = await response.json();
      setAnswer(data.answer || "No answer received");
    } catch (error) {
      setAnswer("Request error: " + error.message);
    }
    setLoading(false);
  };

  return (
    <div style={{ maxWidth: 480, margin: "50px auto", padding: 20, border: "1px solid #ddd", borderRadius: 8 }}>
      <h2>Q&A Assistant</h2>
      <textarea
        rows={3}
        value={question}
        onChange={e => setQuestion(e.target.value)}
        placeholder="Please enter your question"
        style={{ width: "100%", marginBottom: 12, resize: "vertical" }}
      />
      <button onClick={handleAsk} disabled={loading} style={{ width: "100%", padding: 8 }}>
        {loading ? "Asking..." : "Ask"}
      </button>
      <div style={{ marginTop: 24, minHeight: 32 }}>
        {answer && (
          <div style={{ background: "#f8f8f8", padding: 12, borderRadius: 6 }}>
            <b>Answer: </b>{answer}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;