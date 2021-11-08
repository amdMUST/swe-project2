import logo from './logo.svg';
import './App.css';
import { useState, useRef } from 'react';


function App() {
  // fetches JSON data passed in by flask.render_template and loaded
  // in public/index.html in the script with id "data"
  const args = JSON.parse(document.getElementById("data").text);

  // TODO: Implement your main page as a React component.
  return (
    <div>
      <div>
        <h1>Something</h1>
      </div>
      <div id="logout-link">
        <a id="signup-link" href="logout">
          Logout
        </a>
      </div>
    </div>
  );
}

export default App;
