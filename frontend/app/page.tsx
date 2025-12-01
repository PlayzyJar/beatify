// app/page.tsx
"use client";

import { useState } from "react";

export default function HomePage() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);

  async function handleSearch() {
    if (!query.trim()) return;

    try {
      const res = await fetch(`http://localhost:8000/search?q=${query}`);
      const data = await res.json();
      setResults(data); // salva no estado
    } catch (err) {
      console.error("Erro ao buscar:", err);
    }
  }

  return (
     <main className="flex flex-col items-center gap-6 w-full max-w-md p-6">
       <input
         className="w-full p-3 rounded-xl bg-neutral-800 border border-neutral-700 focus:outline-none focus:ring-2 focus:ring-green-500"
         type="text"
         placeholder="Digite o nome da música..."
         value={query}
         onChange={(e) => setQuery(e.target.value)}
       />

       <button
         onClick={handleSearch}
         className="w-[100px] p-3 rounded-xl bg-green-600 hover:bg-green-700 transition font-semibold"
       >
         Buscar
       </button>

       {/* RESULTADOS DA PESQUISA */}
       <div className="w-full flex flex-col gap-3 mt-4">
         {results.length > 0 &&
           results.map((track: any) => (
             <div
               key={track.id}
               className="p-3 rounded-lg bg-neutral-800 border border-neutral-700"
             >
               <p className="font-semibold">{track.name}</p>
               <p className="text-sm text-neutral-400">
                 {track.artists.map((a: any) => a.name).join(", ")}
               </p>
             </div>
           ))}
       </div>
     </main>
   );
 }
