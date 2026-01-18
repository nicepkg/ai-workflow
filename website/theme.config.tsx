import type { ReactNode } from "react";

interface ThemeConfig {
  logo: ReactNode;
  project: {
    link: string;
  };
  docsRepositoryBase: string;
  footer: {
    content: ReactNode;
  };
  editLink: {
    content: string;
  };
  sidebar: {
    defaultMenuCollapseLevel: number;
    toggleButton: boolean;
  };
  toc: {
    backToTop: boolean;
  };
  i18n: Array<{
    locale: string;
    name: string;
  }>;
  feedback: {
    content: string;
    labels: string;
  };
}

const config: ThemeConfig = {
  logo: (
    <span style={{ fontWeight: 700 }}>
      AI Workflow
    </span>
  ),
  project: {
    link: "https://github.com/nicepkg/ai-workflow",
  },
  docsRepositoryBase: "https://github.com/nicepkg/ai-workflow/tree/main/website/content",
  footer: {
    content: (
      <span>
        MIT {new Date().getFullYear()} &copy;{" "}
        <a href="https://github.com/nicepkg/ai-workflow" target="_blank" rel="noopener noreferrer">
          AI Workflow
        </a>
      </span>
    ),
  },
  editLink: {
    content: "Edit this page on GitHub",
  },
  sidebar: {
    defaultMenuCollapseLevel: 1,
    toggleButton: true,
  },
  toc: {
    backToTop: true,
  },
  i18n: [
    { locale: "en", name: "English" },
    { locale: "zh", name: "中文" },
  ],
  feedback: {
    content: "Question? Give us feedback",
    labels: "feedback",
  },
};

export default config;
