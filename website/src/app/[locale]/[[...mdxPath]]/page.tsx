/* eslint-disable react-hooks/rules-of-hooks */
/* eslint-disable @typescript-eslint/unbound-method */
import { generateStaticParamsFor, importPage } from "nextra/pages";
import { useMDXComponents as getMDXComponents } from "../../../../mdx-components";

type PageProps = {
  params: Promise<{
    locale: string;
    mdxPath?: string[];
  }>;
};

const baseGenerateStaticParams = generateStaticParamsFor("mdxPath", "locale");

function normalizeMdxPath(mdxPath?: string[] | string) {
  if (!mdxPath) return [];
  const segments = Array.isArray(mdxPath) ? mdxPath : [mdxPath];
  return segments.filter(Boolean);
}

export async function generateStaticParams() {
  const params = await baseGenerateStaticParams();
  return params.map((param) => ({
    locale: param.locale as string,
    mdxPath: normalizeMdxPath(param.mdxPath as string[] | string | undefined),
  }));
}

export async function generateMetadata(props: PageProps) {
  const params = await props.params;
  const mdxPath = normalizeMdxPath(params.mdxPath);
  const { metadata } = await importPage(mdxPath, params.locale);
  return metadata;
}

const Wrapper = getMDXComponents().wrapper;

export default async function Page(props: PageProps) {
  const params = await props.params;
  const mdxPath = normalizeMdxPath(params.mdxPath);
  const result = await importPage(mdxPath, params.locale);
  const { default: MDXContent, toc, metadata, sourceCode } = result;

  return (
    <Wrapper toc={toc} metadata={metadata} sourceCode={sourceCode}>
      <MDXContent {...props} params={params} />
    </Wrapper>
  );
}
