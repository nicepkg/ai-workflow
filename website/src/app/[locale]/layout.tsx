import { Layout, LocaleSwitch, Navbar, ThemeSwitch } from "nextra-theme-docs";
import { Banner } from "nextra/components";
import { getPageMap } from "nextra/page-map";
import { SiteFooter } from "~/components/shared/site-footer";

const logo = (
  <span style={{ fontWeight: 700 }}>
    AI Workflow
  </span>
);

type LayoutProps = {
  children: React.ReactNode;
  params: Promise<{
    locale: string;
  }>;
};

export default async function LocaleLayout({ children, params }: LayoutProps) {
  const { locale } = await params;
  const pageMap = await getPageMap(`/${locale}`);

  return (
    <>
      <Layout
        pageMap={pageMap}
        docsRepositoryBase="https://github.com/nicepkg/ai-workflow/tree/main/website"
        editLink="Edit this page on GitHub"
        sidebar={{
          defaultMenuCollapseLevel: 1,
          toggleButton: true,
        }}
        toc={{
          backToTop: true,
        }}
        feedback={{
          content: "Question? Give us feedback →",
          labels: "feedback,documentation",
          link: "https://github.com/nicepkg/ai-workflow/issues/new?labels=feedback,documentation&template=feedback.md",
        }}
        i18n={[
          { locale: "en", name: "English" },
          { locale: "zh", name: "中文" },
        ]}
        navbar={
          <Navbar
            logo={logo}
            logoLink={`/${locale}`}
            projectLink="https://github.com/nicepkg/ai-workflow"
          >
            <LocaleSwitch className="x:ml-2" />
            <ThemeSwitch className="x:ml-2" />
          </Navbar>
        }
        footer={<SiteFooter />}
        banner={
          <Banner storageKey="ai-workflow-banner">
            <span>
              🎉 AI Workflow is now open source!{" "}
              <a
                href="https://github.com/nicepkg/ai-workflow"
                target="_blank"
                rel="noopener noreferrer"
                className="x:underline x:underline-offset-2"
              >
                Star us on GitHub
              </a>
            </span>
          </Banner>
        }
      >
        {children}
      </Layout>
    </>
  );
}
