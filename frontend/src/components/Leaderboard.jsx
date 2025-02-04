import { GoPeople } from "react-icons/go";
import { IoMdCheckmarkCircleOutline } from "react-icons/io";
import { IoStatsChartSharp } from "react-icons/io5";

export default function Leaderboard() {
  return (
    <div className="h-screen bg-gray-900  pt-8 ">
      <div className="mx-30">
        <h1 className="text-3xl font-bold text-white">
          Influencer Trust Leaderboard
        </h1>
        <p className="mt-4 text-gray-300">
          Rankings of health influencers based on scientific accuracy,
          credibility, and transparecny. Updated using AI-powered analysis.
        </p>

        <div className="grid gap-x-8 grid-cols-3 mt-8">
          <div className="bg-gray-700 flex p-3 py-6 border-1 border-gray-100  rounded-md">
            <div className="content-center text-6xl pl-3 pr-5">
              <GoPeople className="text-green-700" />
            </div>
            <div className="content-center">
              <div className="font-bold text-white text-2xl">1234</div>
              <div className="text-gray-300"> Active Influencers</div>
            </div>
          </div>
          <div className="bg-gray-700 flex p-3 rounded-md py-6 border-1 border-gray-100">
            <div className="content-center text-6xl pl-3 pr-5">
              <IoMdCheckmarkCircleOutline className="text-green-700" />
            </div>
            <div>
              <div className="font-bold text-white text-2xl">25431</div>
              <div className="text-gray-300">Claims Verified</div>
            </div>
          </div>
          <div className="bg-gray-700 flex p-3 rounded-md py-6 border-1 border-gray-100">
            <div className="content-center text-6xl pl-3 pr-5">
              <IoStatsChartSharp className="text-green-700" />
            </div>
            <div>
              <div className="font-bold text-white text-2xl">85.7%</div>
              <div className="text-gray-300">Average Trust Score</div>
            </div>
          </div>
        </div>

        <div className="mt-20  bg-slate-800">
          <table className="w-full shadow-lg border-separate rounded-md border-spacing-y-3 border-1 border-gray-500">
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
              <tr>
                <td className="border-b-1 pb-3 border-gray-700">#1</td>
                <td className="border-b-1 pb-3 border-gray-700">
                  Dr. Peter Attila
                </td>
                <td className="border-b-1 pb-3 border-gray-700">Medicine</td>
                <td className="border-b-1 pb-3 border-gray-700">91%</td>
                <td className="border-b-1 pb-3 border-gray-700">203</td>
              </tr>
              <tr>
                <td>#2</td>
                <td>Dr. Who</td>
                <td>Medicine</td>
                <td>100%</td>
                <td>1</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
