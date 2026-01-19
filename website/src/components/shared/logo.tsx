import React from "react";

export function Logo({
  width = 32,
  height = 32,
  className,
  ...props
}: React.SVGProps<SVGSVGElement>) {
  return (
    <div className="flex items-center gap-2">
      <svg
        width={width}
        height={height}
        viewBox="0 0 256 256"
        xmlns="http://www.w3.org/2000/svg"
        className={className}
        {...props}
      >
        <rect width="256" height="256" fill="none" />
        <defs>
          <linearGradient
            id="logo-gradient"
            x1="0%"
            y1="0%"
            x2="100%"
            y2="100%"
          >
            <stop offset="0%" stopColor="#8b5cf6" /> {/* Purple-500 */}
            <stop offset="100%" stopColor="#3b82f6" /> {/* Blue-500 */}
          </linearGradient>
        </defs>

        {/* Outer Hexagon/Circle hint */}
        <path
          d="M216,128A88,88,0,1,1,128,40,88,88,0,0,1,216,128Z"
          fill="none"
          stroke="currentColor"
          strokeOpacity="0.1"
          strokeWidth="16"
          strokeLinecap="round"
          strokeDasharray="40 20"
          className="animate-[spin_10s_linear_infinite]"
          style={{ transformOrigin: "center" }}
        />

        {/* The W Wave */}
        <path
          d="M64,112l32,48l32-48l32,48l32-48"
          fill="none"
          stroke="url(#logo-gradient)"
          strokeLinecap="round"
          strokeLinejoin="round"
          strokeWidth="28"
        />

        {/* Start/End Dots */}
        <circle cx="64" cy="112" r="14" fill="url(#logo-gradient)" />
        <circle cx="192" cy="112" r="14" fill="url(#logo-gradient)" />
      </svg>
      <span className="font-bold text-xl tracking-tight hidden sm:inline-block">
        AI Workflow
      </span>
    </div>
  );
}
