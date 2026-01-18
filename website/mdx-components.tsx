import { useMDXComponents as getDocsMDXComponents } from "nextra-theme-docs";

const docsComponents = getDocsMDXComponents();

export function useMDXComponents(components?: Record<string, React.ComponentType>) {
  return {
    ...docsComponents,
    ...components,
  };
}
