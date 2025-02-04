import axios from "axios";
import { useEffect, useState } from "react";
import { GoPeople } from "react-icons/go";
import { IoMdCheckmarkCircleOutline } from "react-icons/io";
import { IoStatsChartSharp } from "react-icons/io5";
import { Link } from "react-router-dom";

export default function Leaderboard() {
  const backendUrl = import.meta.env.VITE_API_BASE_URL;
  const [influencersData, setInfluencerData] = useState([]);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await axios.get(`${backendUrl}/api/influencers/`);
      setInfluencerData(response.data);
    } catch (error) {}
  };

  const calculated_trust_scores = influencersData.map((user_data) => {
    if (!user_data.healthclaims || user_data.healthclaims.length === 0) {
      return { ...user_data, mean_trust_score: 0 };
    }

    const totalScore = user_data.healthclaims.reduce(
      (sum, claim) => sum + claim.trust_score,
      0
    );
    const meanScore = Math.round(totalScore / user_data.healthclaims.length);
    return { ...user_data, mean_trust_score: meanScore };
  });

  const ordered_by_trust_scores = calculated_trust_scores.sort(
    (a, b) => b.mean_trust_score - a.mean_trust_score
  );

  function get_average_trust_score_for_all_users() {
    const sum_avg_scores = calculated_trust_scores.reduce(
      (sum, influencer_data) => sum + influencer_data.mean_trust_score,
      0
    );
    const mean_trust_scores = Math.round(
      sum_avg_scores / influencersData.length
    );
    return mean_trust_scores;
  }

  return (
    <div className="h-screen bg-gray-900  pt-8 ">
      <div className="mx-30">
        {/* Title */}
        <h1 className="text-3xl font-bold text-white">
          Influencer Trust Leaderboard
        </h1>
        {/* Description */}
        <p className="mt-4 text-gray-300">
          Rankings of health influencers based on scientific accuracy,
          credibility, and transparecny. Updated using AI-powered analysis.
        </p>

        {/*  Top stats */}
        <div className="grid gap-x-8 grid-cols-3 mt-8">
          <div className="bg-gray-700 flex p-3 py-6 border-1 border-gray-100  rounded-md">
            <div className="content-center text-6xl pl-3 pr-5">
              <GoPeople className="text-green-700" />
            </div>
            <div className="content-center">
              <div className="font-bold text-white text-2xl">
                {influencersData.length}
              </div>
              <div className="text-gray-300"> Active Influencers</div>
            </div>
          </div>
          <div className="bg-gray-700 flex p-3 rounded-md py-6 border-1 border-gray-100">
            <div className="content-center text-6xl pl-3 pr-5">
              <IoMdCheckmarkCircleOutline className="text-green-700" />
            </div>
            <div>
              <div className="font-bold text-white text-2xl">
                {influencersData.reduce(
                  (sum, influencer_data) =>
                    sum + influencer_data.healthclaims.length,
                  0
                )}
              </div>
              <div className="text-gray-300">Claims Verified</div>
            </div>
          </div>
          <div className="bg-gray-700 flex p-3 rounded-md py-6 border-1 border-gray-100">
            <div className="content-center text-6xl pl-3 pr-5">
              <IoStatsChartSharp className="text-green-700" />
            </div>
            <div>
              <div className="font-bold text-white text-2xl">
                {get_average_trust_score_for_all_users()}%
              </div>
              <div className="text-gray-300">Average Trust Score</div>
            </div>
          </div>
        </div>

        {/* Leaderboard table */}
        <div className="mt-20  bg-slate-800">
          <table className="w-full shadow-lg border-separate rounded-md border-spacing-y-3 border-1 border-gray-500">
            {/*  Table head */}
            <thead className="border border-b-10 text-md text-gray-400 font-black ">
              <tr className="">
                <th className="border-b-1 pb-3 font-semibold">RANK</th>
                <th className="border-b-1 pb-3 font-semibold">INFLUENCER</th>
                <th className="border-b-1 pb-3 font-semibold">CATEGORY</th>
                <th className="border-b-1 pb-3 font-semibold">TRUST SCORE</th>
                <th className="border-b-1 pb-3 font-semibold">
                  VERIFIED CLAIMS
                </th>
              </tr>
            </thead>
            <tbody className="text-center text-sm text-gray-200 font-bold">
              {ordered_by_trust_scores.map((influencer, idx) => (
                <tr key={influencer.username}>
                  <td className="border-b-1 pb-3 border-gray-700">
                    #{idx + 1}
                  </td>
                  <td className="border-b-1 pb-3 border-gray-700">
                    <Link
                      to={{
                        pathname: `/influencer/${influencer.username}`,
                      }}
                      state={influencer} // Pass the influencer object
                    >
                      {influencer.name}
                    </Link>
                  </td>
                  <td className="border-b-1 pb-3 border-gray-700">
                    {influencer.topics[0]}
                  </td>
                  <td className="border-b-1 pb-3 border-gray-700">
                    {influencer.mean_trust_score}%
                  </td>
                  <td className="border-b-1 pb-3 border-gray-700">
                    {influencer.healthclaims.length}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
