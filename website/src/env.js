import { createEnv } from "@t3-oss/env-nextjs";
import { z } from "zod";

export const env = createEnv({
  /**
   * For static export, we only use client-side environment variables.
   * Server-side variables are not available in static builds.
   */
  server: {},

  /**
   * Specify your client-side environment variables schema here.
   * To expose them to the client, prefix them with `NEXT_PUBLIC_`.
   */
  client: {
    NEXT_PUBLIC_SITE_URL: z.string().url().optional(),
    NEXT_PUBLIC_GIT_SHA: z.string().optional(),
  },

  /**
   * Runtime environment mapping.
   */
  runtimeEnv: {
    NEXT_PUBLIC_SITE_URL: process.env.NEXT_PUBLIC_SITE_URL,
    NEXT_PUBLIC_GIT_SHA: process.env.NEXT_PUBLIC_GIT_SHA,
  },

  /**
   * Skip validation during build if needed.
   */
  skipValidation: !!process.env.SKIP_ENV_VALIDATION,

  /**
   * Empty strings are treated as undefined.
   */
  emptyStringAsUndefined: true,
});
