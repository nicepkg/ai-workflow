import type { Metadata } from "next";
import { Footer, Layout, Navbar } from "nextra-theme-docs";
import { Banner, Head } from "nextra/components";
import { getPageMap } from "nextra/page-map";
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

const logo = (
  <span style={{ fontWeight: 700 }}>
    AI Workflow
  </span>
);

const footerContent = (
  <span>
    MIT {new Date().getFullYear()} &copy;{" "}
    <a href="https://github.com/nicepkg/ai-workflow" target="_blank" rel="noopener noreferrer">
      AI Workflow
    </a>
  </span>
);

export default async function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const pageMap = await getPageMap();

  return (
    <html lang="en" dir="ltr" suppressHydrationWarning>
      <Head faviconGlyph="AI" />
      <body>
        <Layout
          pageMap={pageMap}
          docsRepositoryBase="https://github.com/nicepkg/ai-workflow/tree/main/website/content"
          editLink="Edit this page on GitHub"
          sidebar={{
            defaultMenuCollapseLevel: 1,
            toggleButton: true,
          }}
          toc={{
            backToTop: true,
          }}
          feedback={{
            content: "Question? Give us feedback",
            labels: "feedback",
          }}
          i18n={[
            { locale: "en", name: "English" },
            { locale: "zh", name: "中文" },
          ]}
          navbar={
            <Navbar
              logo={logo}
              projectLink="https://github.com/nicepkg/ai-workflow"
            />
          }
          footer={<Footer>{footerContent}</Footer>}
          banner={
            <Banner storageKey="ai-workflow-banner">
              AI Workflow is now open source! Star us on GitHub
            </Banner>
          }
        >
          {children}
        </Layout>
      </body>
    </html>
  );
}
