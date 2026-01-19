import nextra from "nextra";

const withNextra = nextra({
  // Nextra config options
  defaultShowCopyCode: true,
  search: {
    codeblocks: false,
  },
  unstable_shouldAddLocaleToLinks: true,
});

/** @type {import("next").NextConfig} */
const config = {
  // Static export for Cloudflare Pages (no server functions)
  output: "export",

  i18n: {
    locales: ["en", "zh"],
    defaultLocale: "en",
  },

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

  experimental: {
    turbo: {
      rules: {
        "*.svg": {
          loaders: ["@svgr/webpack"],
          as: "*.js",
        },
      },
    },
  },

  webpack(config) {
    config.module.rules.push({
      test: /\.svg$/i,
      issuer: /\.[jt]sx?$/,
      use: ["@svgr/webpack"],
    });
    return config;
  },
};

export default withNextra(config);
