"use client";

import React, { useEffect, useState } from "react";
import { useSearchParams } from "next/navigation";
import Image from "next/image";

type Beatmap = {
  title?: string;
  artist?: string;
  creator?: string;
  play_count?: number;
  image?: any;
  last_updated?: string;
  preview_url?: string;
  [key: string]: any;
};

export default function Beatmaps() {
  const searchParams = useSearchParams();

  const title = searchParams.get("title") ?? "";
  const artist = searchParams.get("artist") ?? "";

  const [beatmaps, setBeatmaps] = useState<Beatmap[]>([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    async function fetchBeatmaps() {
      if (title === "" || artist === "") {
        setBeatmaps([]);
        return;
      }

      setLoading(true);

      try {
        const response = await fetch(
          `http://localhost:8000/osu_beatmaps?track=${encodeURIComponent(title)}&artist=${encodeURIComponent(artist)}`,
        );

        const data = await response.json();

        setBeatmaps(data);
      } catch (error) {
        console.error(error);
      } finally {
        setLoading(false);
      }
    }

    fetchBeatmaps();
  }, [title, artist]);

  return (
    <div className="justify-center flex flex-col gap-4 items-center w-screen h-screen text-slate-200 py-4">
      {/*área principal*/}
      <div className="w-3/8 h-9/10 rounded-md flex flex-col justify-start items-start bg-zinc-900">
        {/*resultados*/}
        {beatmaps.length > 0 && (
          <div className="w-full px-4 py-4 h-full flex flex-col justify-center items-center gap-2">
            {beatmaps.slice(0, 5).map((beatmap, i) => (
              <div
                type="button"
                key={beatmap.id ?? i}
                className="group relative hover:bg-zinc-800 transition ease-in-out duration-300 hover:scale-102 px-2 w-full h-25 rounded-md grid grid-cols-6 grid-rows-2 gap-2 justify-end items-center bg-zinc-900 text-zinc-100"
              >
                <div className="flex justify-center items-center row-span-2 col-1 relative overflow-hidden rounded-md">
                  <Image
                    className="group-hover:brightness-50 object-cover transition duration-200 group-hover:scale-102 group-hover: shadow-lg shadow-zinc-900 w-full h-auto row-span-2 col-1 rounded-md"
                    src={beatmap.image}
                    alt={beatmap.title}
                    width={100}
                    height={100}
                  />
                </div>

                <div className="text-xl font-semibold truncate text-overflow-ellipsis row-1 justify-start items-start col-start-2 col-end-7">
                  {beatmap.title}
                </div>

                <div className="text-sm truncate text-overflow-ellipsis row-2 justify-start items-end col-start-2 col-end-7">
                  {beatmap.artist}
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
