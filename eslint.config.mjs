import { defineConfig, globalIgnores } from "eslint/config";

export default defineConfig(
  // Root config only to satisfy the ESLint extension; linting happens in /website.
  globalIgnores(["**/*"]),
);
