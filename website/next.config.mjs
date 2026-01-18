import nextra from "nextra";

const withNextra = nextra({
  // Nextra config options
  defaultShowCopyCode: true,
  search: {
    codeblocks: false,
  },
});

/** @type {import("next").NextConfig} */
const config = {
  // Static export for Cloudflare Pages (no server functions)
  output: "export",

  // Required for static export
  images: {
    unoptimized: true,
  },

  // Trailing slash for better static hosting compatibility
  trailingSlash: true,

  // Disable x-powered-by header
  poweredByHeader: false,

  // Enable React strict mode
  reactStrictMode: true,

  // Eslint config
  eslint: {
    // Warning: This allows production builds to successfully complete even if
    // your project has ESLint errors.
    ignoreDuringBuilds: true,
  },

  // TypeScript config
  typescript: {
    // Warning: This allows production builds to successfully complete even if
    // your project has type errors.
    ignoreBuildErrors: true,
  },
};

export default withNextra(config);
