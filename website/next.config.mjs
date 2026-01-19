import nextra from "nextra";

const withNextra = nextra({
  // Nextra config options
  defaultShowCopyCode: true,
  search: {
    codeblocks: false,
  },
  unstable_shouldAddLocaleToLinks: true,
});

const svgrLoader = {
  loader: "@svgr/webpack",
  options: {
    svgoConfig: {
      plugins: [
        {
          name: "preset-default",
          params: {
            overrides: {
              // disable a default plugin
              removeViewBox: false,
            },
          },
        },
        {
          name: "prefixIds",
        },
      ],
    },
  },
};

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
  turbopack: {
    rules: {
      // eslint-disable-next-line @typescript-eslint/ban-ts-comment
      // @ts-expect-error
      "*.svg": {
        loaders: [svgrLoader],
        as: "*.js",
      },
    },
  },
  webpack(config) {
    // Grab the existing rule that handles SVG imports
    // eslint-disable-next-line @typescript-eslint/ban-ts-comment
    // @ts-ignore
    const fileLoaderRule = config.module.rules.find((rule) =>
      rule.test?.test?.(".svg"),
    );

    config.module.rules.push(
      // Reapply the existing rule, but only for svg imports ending in ?url
      {
        ...fileLoaderRule,
        test: /\.svg$/i,
        resourceQuery: /url/, // *.svg?url
      },
      // Convert all other *.svg imports to React components
      {
        test: /\.svg$/i,
        issuer: fileLoaderRule.issuer,
        resourceQuery: { not: [...fileLoaderRule.resourceQuery.not, /url/] }, // exclude if *.svg?url
        use: [svgrLoader],
      },
    );

    // Modify the file loader rule to ignore *.svg, since we have it handled now.
    fileLoaderRule.exclude = /\.svg$/i;

    return config;
  },
};

export default withNextra(config);
