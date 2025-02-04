import { NavLink } from "react-router-dom";

export default function Navbar() {
  return (
    <nav className="bg-gray-800 p-3 border-b-1 border-gray-600">
      <div className="mx-40 flex justify-between items-center ">
        <div className="text-emerald-500 text-lg font-semibold">
          <NavLink to="/leaderboard">VerifyInfluencers</NavLink>
        </div>
        <div className="space-x-20">
          <NavLink to="/leaderboard" className="text-white hover:text-gray-300">
            Leaderboard
          </NavLink>
          <NavLink to="/admin" className="text-white hover:text-gray-300">
            Admin
          </NavLink>
        </div>
      </div>
    </nav>
  );
}
