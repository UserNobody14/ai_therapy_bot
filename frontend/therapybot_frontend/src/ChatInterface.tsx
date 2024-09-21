import React, { useState } from "react";

export interface Message {
  text: string;
  isUser: boolean;
}

const exampleMessages: Message[] = [
  { text: "Hello!", isUser: false },
  { text: "Hi there!" , isUser: true },
];

export function ChatInterface() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState<Message[]>(exampleMessages);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [mp3, setMp3] = useState<string | null>(null);

  const sendMessage = async () => {
    if (!input) {
      return;
    }

    setLoading(true);
    setError(null);

    try {
        const ddd = "http://localhost:8000/get_message";
        console.log(ddd);
      const response = await fetch(ddd, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ 
            past_messages: messages.map((message) => message.text),
            current_message: input }),
      });

      if (!response.ok) {
        throw new Error("Failed to send message");
      }

      const data = await response.json();
      setMessages((messages) => [
        ...messages,
        { text: input, isUser: true },
        { text: data.bot_message, isUser: false },
      ]);

      // If there's an mp3 file in the response, play it
      const mp3Field = data.audio_file;

      setMp3(mp3Field);

      setInput("");
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
    } catch (error: any) {
      setError(error?.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="chat-interface">
      {/* Play MP3 */}
      <h1>AI Therapy Bot</h1>
      <h2>Overview</h2>
      {/* All Messages */}
      <div className="messages">
        <div>
        The AI therapy bot is a web application that provides a conversational interface for users to talk about their feelings and emotions. The bot uses natural language processing to understand the user's input and respond with appropriate messages. The goal of the bot is to provide a safe space for users to express themselves and receive support and guidance.
        </div>
        {messages.map((message, index) => (
          <div
            key={index}
            className={`message ${message.isUser ? "user" : "bot"}`}
          >
            {message.text}
          </div>
        ))}
      </div>
      {mp3 && <audio src={mp3} controls autoPlay />}
      {/* Current Messages */}
      <div className={"input " + (loading ? 'loading' : '')}>
        <textarea
          value={input}
          onChange={(event) => setInput(event.target.value)}
          disabled={loading}
        />
        <button 
          onClick={sendMessage} 
          disabled={loading}>
          Send
        </button>
      </div>
      {error && <div className="error">{error}</div>}
    </div>
  );
}
