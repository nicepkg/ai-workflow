"use client";

import { useEffect } from "react";

const DEFAULT_LOCALE = "en";

export default function HomeRedirect() {
  useEffect(() => {
    window.location.replace(`/${DEFAULT_LOCALE}`);
  }, []);

  return (
    <main style={{ padding: "2rem" }}>
      <p>Redirecting to the English site...</p>
      <p>
        <a href={`/${DEFAULT_LOCALE}`}>Continue</a>
      </p>
    </main>
  );
}
