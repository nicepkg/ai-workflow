import type { MetaRecord } from "nextra";

export default {
  index: {
    title: "Home",
    type: "page",
    display: "hidden",
    theme: {
      layout: "full",
      breadcrumb: false,
      sidebar: false,
      toc: false,
      pagination: false,
      copyPage: false,
      timestamp: false,
    }
  },
  docs: {
    title: "Documentation",
    type: "page",
  },
  workflows: {
    title: "Workflows",
    type: "page",
  },
} satisfies MetaRecord;
