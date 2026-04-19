import { Routes, Route, Navigate } from "react-router-dom"
import { useState } from "react"
import Login from "./pages/Login"
import Signup from "./pages/Signup"
import Dashboard from "./pages/Dashboard"
import ForgotPassword from "./pages/ForgotPassword"
import ResetPassword from "./pages/ResetPassword"

function App() {
  const [token, setToken] = useState(localStorage.getItem("token") || null)

  const handleLogin = (receivedToken) => {
    localStorage.setItem("token", receivedToken)
    setToken(receivedToken)
  }

  const handleLogout = () => {
    localStorage.removeItem("token")
    setToken(null)
  }

  return (
    <Routes>
      <Route path="/" element={token ? <Navigate to="/dashboard" /> : <Navigate to="/login" />} />
      <Route path="/login" element={token ? <Navigate to="/dashboard" /> : <Login onLogin={handleLogin} />} />
      <Route path="/signup" element={token ? <Navigate to="/dashboard" /> : <Signup onLogin={handleLogin} />} />
      <Route path="/dashboard" element={token ? <Dashboard token={token} onLogout={handleLogout} /> : <Navigate to="/login" />} />
      <Route path="/forgot-password" element={<ForgotPassword />} />
      <Route path="/reset-password" element={<ResetPassword />} />
    </Routes>
  )
}

export default App