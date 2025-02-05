import { CiSettings } from "react-icons/ci";
import { FaSearch } from "react-icons/fa";
import { FaPlus } from "react-icons/fa6";
import { FaTwitter } from "react-icons/fa";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

export default function Admin() {
  const [twitterKey, setTwitterKey] = useState("");
  const [username, setUsername] = useState("");
  // const [tweets, setTweets] = useState([]);
  const [error, setError] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const navigate = useNavigate();
  const apiUrl = "/choreo-apis/verifyinfluencersdjangore/backend/v1";
  const backendUrl = import.meta.env.VITE_API_BASE_URL
    ? import.meta.env.VITE_API_BASE_URL
    : apiUrl;

  const handleSubmit = async (e) => {
    e.preventDefault(); // Prevent page reload
    setIsLoading(true);

    if (!username) {
      setError("Username field is required.");
      setIsLoading(false);
      return;
    }

    try {
      let response;
      if (twitterKey != "") {
        response = await axios.get(
          `${backendUrl}/api/influencers/${username}/tweets/`,
          {
            headers: {
              Authorization: twitterKey,
              "Content-Type": "application/json",
            },
          }
        );
      } else {
        response = await axios.get(
          `${backendUrl}/api/influencers/${username}/tweets/`
        );
      }

      if (response.status != 200) {
        if (response.status == 404) {
          throw new Error("No user found.");
        }
        if (response.status == 429) {
          throw new Error("Too many requests.");
        }
        if (response.status == 401) {
          throw new Error("You are not authorized to perform this action.");
        }
        throw new Error("Failed to fetch tweets.");
      }

      try {
        const allInfluencers = await axios.get(
          `${backendUrl}/api/influencers/`
        );
        const influencer = allInfluencers.data.filter(
          (influencer) =>
            influencer.username === response.data[0].twitter_username
        );
        navigate(`/influencer/${influencer[0].username}`, {
          state: { ...influencer[0] },
        });
      } catch (error) {
        setError("Too many requests.");
        throw new Error("Too many requests.");
      }
    } catch (err) {
      if (err.status == 500) {
        setError("Unexpected error occured on the server, please try again!");
      }
      setError("User not found!");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div className="h-screen bg-gray-900  pt-8 ">
        <div className="mx-50 ">
          <h1 className="text-3xl font-bold text-white">
            Research Tasks {isLoading ? "- Loading, please wait..." : ""}
          </h1>

          <div className="mt-8 h-140 border-1 border-gray-400 rounded-md bg-gray-800">
            <div className="flex px-3 py-6 ">
              <div className="content-center text-2xl pl-2 pr-2 font-bold">
                <CiSettings className="text-green-400 " />
              </div>
              <div className="text-white text-xl font-bold">
                Research Configuration
              </div>
            </div>

            <div className="grid gap-x-4 grid-cols-2 px-6">
              <div>
                <div className="bg-teal-900 content-center text-center rounded-md py-6 border-1 border-green-600">
                  <div className="content-center text-6xl pl-3 pr-5"></div>
                  <div className="content-center">
                    <div className="font-bold text-white text-2xl">
                      Specific Influencer
                    </div>
                    <div className="text-gray-300">
                      Research a known health influencer by name
                    </div>
                  </div>
                </div>

                <div className="py-4">
                  <div className="text-lg text-white font-semibold">
                    Time Range
                  </div>
                  <div className="grid gap-x-1 gap-y-1 grid-cols-2 text-gray-400 font-semibold">
                    <div className="text-center border-1 rounded-sm p-1">
                      Last Week
                    </div>
                    <div className="text-center border-1 rounded-sm bg-teal-900 p-1 border-green-600 text-green-500">
                      Last Month
                    </div>
                    <div className="text-center border-1 rounded-sm p-1">
                      Last Year
                    </div>
                    <div className="text-center border-1 rounded-sm p-1">
                      All Time
                    </div>
                  </div>
                </div>

                <div className="flex flex-col">
                  {/* Label */}
                  <label
                    htmlFor="search"
                    className="text-lg text-white font-semibold mb-1"
                  >
                    Influencer name
                  </label>

                  {/* Search Input with Icon */}
                  <div className="flex items-center border border-gray-300 rounded-sm px-4 py-2 shadow-md bg-gray-900 ">
                    <FaSearch className="text-gray-400 mr-2 " />
                    <input
                      id="search"
                      type="text"
                      placeholder="Search..."
                      className="w-full outline-none text-gray-400"
                      onChange={(e) => setUsername(e.target.value)}
                    />
                  </div>
                </div>

                <div className="flex flex-col mt-2">
                  {/* Label */}
                  <label
                    htmlFor="twitterkey"
                    className="text-lg text-white font-semibold mb-1"
                  >
                    Twitter API key (OPTIONAL) - currently only free tier
                    available with predefined key
                  </label>

                  {/* Twitter API Key Input with Icon */}
                  <div className="flex items-center border border-gray-300 rounded-sm px-4 py-2 shadow-md bg-gray-900 ">
                    <FaTwitter className="text-gray-400 mr-2 " />
                    <input
                      id="twitterkey"
                      type="text"
                      placeholder="Enter Twitter API Key..."
                      className="w-full outline-none text-gray-400"
                      onChange={(e) => setTwitterKey(e.target.value)}
                    />
                  </div>
                </div>

                {error && <p className="text-red-500">{error}</p>}
              </div>

              <div>
                <div className="content-center text-center rounded-md py-6 border-1 border-gray-600">
                  <div className="content-center text-6xl pl-3 pr-5"></div>
                  <div>
                    <div className="font-bold text-white text-2xl">
                      Discover New
                    </div>
                    <div className="text-gray-300">
                      Find and analyze new health influencers
                    </div>
                  </div>
                </div>

                <div className="py-4">
                  <div className="text-lg text-white font-semibold">
                    Products to Find Per Influencer
                  </div>
                  <div className="grid text-gray-400 font-semibold bg-gray-900">
                    <div className="border-1 rounded-sm p-1 px-3">10</div>
                  </div>
                </div>
              </div>
            </div>

            <div className="justify-end text-right mr-6 mt-25 flex">
              <button
                className={`px-4 py-2 flex items-center gap-2 rounded-md ${
                  isLoading == true
                    ? "bg-red-300 text-white"
                    : "bg-green-600 text-white  hover:bg-green-500"
                }`}
                type="submit"
              >
                <FaPlus className="text-lg" />
                Start Research
              </button>
            </div>
          </div>
        </div>
      </div>
    </form>
  );
}
