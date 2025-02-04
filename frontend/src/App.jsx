import { Routes, Route } from "react-router-dom";
import Leaderboard from "./components/Leaderboard";
import Navbar from "./components/Navbar";
import Admin from "./components/Admin";
import Influencer from "./components/Influencer";
export default function App() {
  return (
    <div className="overflow-hidden">
      <Navbar />
      <Routes>
        <Route path="/" element={<Leaderboard />} />
        <Route path="/leaderboard" element={<Leaderboard />} />
        <Route path="/admin" element={<Admin />} />
        <Route path="/influencer" element={<Influencer />} />
        <Route path="*" element={<Leaderboard />} />
      </Routes>
    </div>
  );
}
