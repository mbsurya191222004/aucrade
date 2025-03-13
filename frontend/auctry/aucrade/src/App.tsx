import { useState } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { Signup } from "./pages/Signup";
import { Login } from "./pages/Login";
import { Home } from "./pages/Home";

function App() {
  const [count, setCount] = useState(0);

  return (
    <>
      <Signup />
      <Login />
      <Home />
    </>
  );
}

export default App;
