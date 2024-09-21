
import './App.css'
import { ChatInterface } from './ChatInterface'

function App() {

  return (
    <>
    {/* AI therapy bot overview */}
    <div className="overall">

      {/* <p>
        The AI therapy bot is a web application that provides a conversational interface for users to talk about their feelings and emotions. The bot uses natural language processing to understand the user's input and respond with appropriate messages. The goal of the bot is to provide a safe space for users to express themselves and receive support and guidance.
      </p> */}
      {/* Chat interface to submit text */}
      <ChatInterface />
    </div>
    </>
  )
}

export default App
