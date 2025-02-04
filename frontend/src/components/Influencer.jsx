import { FaExternalLinkAlt } from "react-icons/fa";
import { useLocation, useParams } from "react-router-dom";
import { Link } from "react-router-dom";

export default function Influencer() {
  const { username } = useParams(); // Get the username from the URL
  const location = useLocation();

  const influencerData = location.state || {}; // Fallback to empty object

  if (!influencerData) {
    // You can make an API request here based on the username
    return (
      <div className=" bg-gray-900  pt-8 ">
        <div className="text-center bg-gray-900 mt-20 text-4xl font-bold text-gray-400">
          Loading...
        </div>
      </div>
    );
  }

  if ("error" in influencerData) {
    if (influencerData.error == "Too many requests.") {
      return (
        <div className="min-h-screen bg-gray-900  pt-8">
          <div className=" text-white text-center my-20 text-xl font-semibold">
            Too many requests made for the free tier Twitter API. Please check
            later or add your personal Twitter API key.
          </div>
        </div>
      );
    }
    if (influencerData.error == "No user found.") {
      return (
        <div className="min-h-screen bg-gray-900  pt-8">
          <div className=" text-white text-center my-20 text-xl font-semibold">
            No user found with that name.
          </div>
        </div>
      );
    }
    return (
      <div className="min-h-screen bg-gray-900  pt-8">
        <div className=" text-white text-center my-20 text-xl font-semibold">
          {influencerData}
        </div>
      </div>
    );
  }

  return (
    <div className=" min-h-screen bg-gray-900  pt-8 ">
      <Link
        to="/leaderboard"
        className="text-green-500 text-lg px-15  rounded mb-4"
      >
        ← Back to Leaderboard
      </Link>

      <div className="mx-10 ">
        {/* Influencer name */}
        <h1 className="text-4xl font-bold text-white ml-5">
          {influencerData.name}
        </h1>
        {/* Topics */}
        <div className="flex text-white ml-5 gap-3 mt-5">
          {influencerData.topics.map((topic, idx) => (
            <div
              key={`${username}${idx}`}
              className="p-1 px-3 bg-gray-700  rounded-full"
            >
              {topic}
            </div>
          ))}
        </div>
        {/* Description */}
        <div className="text-gray-300 mr-100 ml-5 mt-4 text-lg font-normal">
          Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe, illo
          eius illum mollitia corporis dolorem accusamus accusantium. Veritatis
          libero hic fuga fugiat repellat optio debitis itaque. Aperiam odio
          libero sint? Lorem ipsum dolor sit, amet consectetur adipisicing elit.
          Quaerat animi quam quidem, labore pariatur, maxime libero beatae sit
          fuga nobis dolore itaque, quae odit id sint. Optio laudantium quis
          possimus.
        </div>

        <div>
          {/* Claims, Recommended products and Monetization picker */}
          <div className="flex text-gray-400 mt-10 ml-5 gap-5 text-lg border-b-1 border-collapse">
            <div className="border-b-5 border-green-500 text-green-500 hover:text-green-400">
              Claims Analysis
            </div>
            <div className="hover:text-gray-300">Recommended Products</div>
            <div className="hover:text-gray-300">Monetization</div>
          </div>

          {influencerData.healthclaims.map((healthClaimData) => (
            <>
              {/* Single claim with details*/}
              <div className="text-white pt-4 px-5 mx-5 mt-3 bg-gray-800 rounded-lg">
                {/* Claim text, status and trust score */}
                <div className="border-b-1 border-gray-700 mx-10">
                  <div className="flex  pb-4">
                    {/* Claim status */}
                    <div
                      className={`text-green-200 rounded-full text-center my-auto px-2 ${
                        healthClaimData.verification_status == "Verified"
                          ? "bg-green-700"
                          : healthClaimData.verification_status ==
                            "Questionable"
                          ? "bg-yellow-700"
                          : "bg-red-700"
                      } `}
                    >
                      {healthClaimData.verification_status}
                    </div>
                    {/* Claim text */}
                    <div className="text-lg ml-5">{healthClaimData.claim}</div>
                  </div>
                  <div className="mb-4 text-right">
                    <div className="text-lg">Trust score: </div>
                    <div
                      className={`text-xl font-bold ml-5 ${
                        healthClaimData.trust_score >= 90
                          ? "text-green-600"
                          : healthClaimData.trust_score >= 70
                          ? "text-yellow-600"
                          : "text-red-600"
                      }`}
                    >
                      {healthClaimData.trust_score} %
                    </div>
                  </div>
                </div>
                {healthClaimData.sources.length === 0 ? (
                  <>
                    {/* Researches */}
                    <div className="ml-10">
                      <div className=" ml-4 pt-3 text-lg pb-2">
                        No researches found to clarify or debunk the
                        affirmation.
                      </div>
                      {/* Researches lsit */}
                    </div>
                  </>
                ) : (
                  <>
                    {/* Researches */}
                    <div className="ml-10">
                      <div className=" ml-4 pt-3 text-lg pb-2">Researches</div>
                      {/* Researches lsit */}

                      {healthClaimData.sources.map((source) => (
                        <>
                          <div className="pl-4 text-lg pb-2">
                            <a
                              href={source.study_link}
                              target="_blank"
                              rel="noopener noreferrer"
                              className="flex items-center text-blue-500 hover:underline"
                            >
                              {source.study_name}
                              <FaExternalLinkAlt className="ml-2" />
                            </a>
                          </div>
                        </>
                      ))}
                    </div>
                  </>
                )}
              </div>
            </>
          ))}
        </div>
      </div>
    </div>
  );
}
