import { FaExternalLinkAlt } from "react-icons/fa";

export default function Navbar() {
  return (
    <div className="h-screen bg-gray-900  pt-8 ">
      <div className="mx-10 ">
        {/* Influencer name */}
        <h1 className="text-4xl font-bold text-white ml-5">Andrew Huberman</h1>
        {/* Topics */}
        <div className="flex text-white ml-5 gap-3 mt-5">
          <div className="p-1 px-3 bg-gray-700  rounded-full">Neuroscience</div>
          <div className="p-1 px-3 bg-gray-700  rounded-full">Sleep</div>
          <div className="p-1 px-3 bg-gray-700  rounded-full">Performance</div>
          <div className="p-1 px-3 bg-gray-700  rounded-full">Hormones</div>
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

          {/* Single claim with details*/}
          <div className="text-white pt-4 px-5 mx-5 mt-3 bg-gray-800 rounded-lg">
            {/* Claim text, status and trust score */}
            <div className="border-b-1 border-gray-700 mx-10">
              <div className="flex  pb-4">
                {/* Claim status */}
                <div className="text-green-200 bg-green-700 rounded-full text-center my-auto px-2">
                  Verified
                </div>
                {/* Claim text */}
                <div className="text-lg ml-5">
                  Claim Claim Claim Claim Claim Claim Lorem ipsum dolor sit amet
                  Lorem, ipsum dolor sit amet consectetur adipisicing elit.
                  Minima voluptatibus cum dicta nulla. Eligendi quis nam
                  incidunt, provident architecto ut laudantium iusto nemo
                  consequatur possimus. Quos, expedita nam. Dolor, aspernatur!
                  Lorem ipsum dolor sit amet consectetur adipisicing elit.
                  Aliquid, sint ratione. Cupiditate impedit officiis magni
                  architecto fuga officia odio praesentium. Id error quasi nulla
                  corporis unde, enim eos voluptate tenetur.
                </div>
              </div>
              <div className="mb-4 text-right">
                <div className="text-lg">Trust score: </div>
                <div className="text-xl font-bold ml-5 text-green-600">
                  92 %
                </div>
              </div>
            </div>
            {/* Researches */}
            <div>
              <div className=" ml-4 pt-3 text-lg pb-2">Researches</div>
              {/* Researches lsit */}
              <div className="pl-4 text-lg pb-2">
                <a
                  href="https://docs.google.com/document/d/1ABmykiy"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="flex items-center text-blue-500 hover:underline"
                >
                  A new and extravagant research{" "}
                  <FaExternalLinkAlt className="ml-2" />
                </a>
              </div>
              <div className="pl-4 text-lg pb-2">
                <a
                  href="https://docs.google.com/document/d/1ABmykiy"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="flex items-center text-blue-500 hover:underline"
                >
                  ANOTHER ONE HERES
                  <FaExternalLinkAlt className="ml-2" />
                </a>
              </div>
              <div className="pl-4 text-lg pb-2">
                <a
                  href="https://docs.google.com/document/d/1ABmykiy"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="flex items-center text-blue-500 hover:underline"
                >
                  A nd the last one is here
                  <FaExternalLinkAlt className="ml-2" />
                </a>
              </div>
            </div>
          </div>

          {/* Single claim with details*/}
          <div className="text-white pt-4 px-5 mx-5 mt-3 bg-gray-800 rounded-lg">
            {/* Claim text, status and trust score */}
            <div className="border-b-1 border-gray-700 mx-10">
              <div className="flex  pb-4">
                {/* Claim status */}
                <div className="text-green-200 bg-green-700 rounded-full text-center my-auto px-2">
                  Verified
                </div>
                {/* Claim text */}
                <div className="text-lg ml-5">
                  Claim Claim Claim Claim Claim Claim Lorem ipsum dolor sit amet
                  Lorem, ipsum dolor sit amet consectetur adipisicing elit.
                </div>
              </div>
              <div className="mb-4 text-right">
                <div className="text-lg">Trust score: </div>
                <div className="text-xl font-bold ml-5 text-green-600">
                  92 %
                </div>
              </div>
            </div>
            {/* Researches */}
            <div>
              <div className=" ml-4 pt-3 text-lg pb-2">Researches</div>
              {/* Researches lsit */}
              <div className="pl-4 text-lg pb-2">
                <a
                  href="https://docs.google.com/document/d/1ABmykiy"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="flex items-center text-blue-500 hover:underline"
                >
                  A new and extravagant research{" "}
                  <FaExternalLinkAlt className="ml-2" />
                </a>
              </div>
              <div className="pl-4 text-lg pb-2">
                <a
                  href="https://docs.google.com/document/d/1ABmykiy"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="flex items-center text-blue-500 hover:underline"
                >
                  ANOTHER ONE HERES
                  <FaExternalLinkAlt className="ml-2" />
                </a>
              </div>
              <div className="pl-4 text-lg pb-2">
                <a
                  href="https://docs.google.com/document/d/1ABmykiy"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="flex items-center text-blue-500 hover:underline"
                >
                  A nd the last one is here
                  <FaExternalLinkAlt className="ml-2" />
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
