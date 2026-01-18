import type { Metadata } from "next";
import { Head } from "nextra/components";
import "nextra-theme-docs/style.css";
import "../styles/globals.css";

export const metadata: Metadata = {
  title: {
    default: "AI Workflow",
    template: "%s - AI Workflow",
  },
  description: "Pre-configured skill sets for AI coding assistants like Claude Code, Cursor, Codex, and more.",
  metadataBase: new URL("https://ai-workflow.xiaominglab.com"),
  openGraph: {
    title: "AI Workflow",
    description: "Pre-configured skill sets for AI coding assistants",
    url: "https://ai-workflow.xiaominglab.com",
    siteName: "AI Workflow",
    locale: "en_US",
    type: "website",
  },
  twitter: {
    card: "summary_large_image",
    title: "AI Workflow",
    description: "Pre-configured skill sets for AI coding assistants",
  },
  robots: {
    index: true,
    follow: true,
  },
};

export default async function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" dir="ltr" suppressHydrationWarning>
      <Head faviconGlyph="AI" />
      <body>
        {children}
      </body>
    </html>
  );
}
