"use client";

import { motion } from "framer-motion";
import {
  ArrowRight,
  Github,
  Terminal,
  Zap,
  BookOpen,
  TrendingUp,
  Video,
  BarChart2,
  Presentation,
  CheckCircle,
} from "lucide-react";
import dynamic from "next/dynamic";
import Link from "next/link";
import { Button } from "~/components/ui/button";
import { cn } from "~/lib/utils";

const Hero3D = dynamic(() => import("./hero-3d").then((mod) => mod.Hero3D), {
  ssr: false,
});

const workflows = [
  {
    icon: BookOpen,
    title: { en: "Content Creator", zh: "内容创作者" },
    desc: { en: "SEO, Blog, Social Media", zh: "SEO, 博客, 社交媒体" },
    link: "/workflows/content-creator",
    color: "text-blue-500",
    bg: "bg-blue-500/10",
  },
  {
    icon: Zap,
    title: { en: "Marketing Pro", zh: "营销专家" },
    desc: { en: "Growth, Copywriting, Funnels", zh: "增长, 文案, 漏斗" },
    link: "/workflows/marketing-pro",
    color: "text-purple-500",
    bg: "bg-purple-500/10",
  },
  {
    icon: Video,
    title: { en: "Video Creator", zh: "视频创作者" },
    desc: { en: "Script, Hooks, Thumbnails", zh: "脚本, 钩子, 封面" },
    link: "/workflows/video-creator",
    color: "text-red-500",
    bg: "bg-red-500/10",
  },
  {
    icon: TrendingUp,
    title: { en: "Stock Trader", zh: "股票交易员" },
    desc: { en: "Technical Analysis, Macro", zh: "技术分析, 宏观" },
    link: "/workflows/stock-trader",
    color: "text-green-500",
    bg: "bg-green-500/10",
  },
  {
    icon: BarChart2,
    title: { en: "Product Manager", zh: "产品经理" },
    desc: { en: "PRD, User Stories, Strategy", zh: "PRD, 用户故事, 策略" },
    link: "/workflows/product-manager",
    color: "text-orange-500",
    bg: "bg-orange-500/10",
  },
  {
    icon: Presentation,
    title: { en: "Talk to Slidev", zh: "Talk to Slidev" },
    desc: { en: "Presentations, Storytelling", zh: "演示文稿, 讲故事" },
    link: "/workflows/talk-to-slidev",
    color: "text-yellow-500",
    bg: "bg-yellow-500/10",
  },
];

const problems = [
  {
    role: { en: "Content Creator", zh: "内容创作者" },
    pain: {
      en: "Explaining SEO basics, H2 structure, meta descriptions... every single time",
      zh: "每次都要解释 SEO 基础、H2 结构、meta 描述...",
    },
    gain: {
      en: "AI pre-loaded with SEO best practices, content frameworks",
      zh: "AI 已预装 SEO 最佳实践、内容框架",
    },
  },
  {
    role: { en: "Marketer", zh: "营销人员" },
    pain: {
      en: "Teaching UTM parameters, AIDA copywriting, funnel optimization...",
      zh: "教 UTM 参数、AIDA 文案法、漏斗优化...",
    },
    gain: {
      en: "AI equipped with GTM strategy, campaign templates, analytics frameworks",
      zh: "AI 已配备 GTM 策略、活动模板、分析框架",
    },
  },
  {
    role: { en: "Stock Trader", zh: "股票交易员" },
    pain: {
      en: "MACD means..., RSI indicates..., check the 200-day MA...",
      zh: "MACD 意味着...、RSI 表示...、看 200 日均线...",
    },
    gain: {
      en: "AI loaded with technical analysis, fundamentals, multi-market expertise",
      zh: "AI 已加载技术分析、基本面、多市场专业知识",
    },
  },
];

type Translation = {
  hero: {
    title: string;
    subtitle: string;
    desc: string;
    getStarted: string;
    viewGithub: string;
  };
  problem: {
    title: string;
    without: string;
    with: string;
  };
  workflows: {
    title: string;
    subtitle: string;
  };
  tools: {
    title: string;
  };
  cta: {
    title: string;
    desc: string;
    button: string;
  };
};

export function LandingPage({ lang }: { lang: "en" | "zh" }) {
  const t: Translation = {
    hero: {
      title:
        lang === "en" ? "Supercharge your AI Workflow" : "AI 工作流的究极形态",
      subtitle:
        lang === "en"
          ? "Stop repeating yourself. Start with context."
          : "告别重复解释。让 AI 真正懂你。",
      desc:
        lang === "en"
          ? "Every session starts from zero. One command adds professional skills, best practices, and project context to your AI."
          : "每次对话都从零开始？一条命令，为你的 AI 注入专业技能、最佳实践和项目上下文。",
      getStarted: lang === "en" ? "Get Started" : "开始使用",
      viewGithub: lang === "en" ? "Star on GitHub" : "Star on GitHub",
    },
    problem: {
      title: lang === "en" ? "The Problem We Solve" : "我们解决的痛点",
      without: lang === "en" ? "Without AI Workflow" : "没有 AI Workflow",
      with: lang === "en" ? "With AI Workflow" : "有了 AI Workflow",
    },
    workflows: {
      title: lang === "en" ? "Explore Workflows" : "探索工作流",
      subtitle:
        lang === "en"
          ? " Specialized skills for every role"
          : "为每个角色打造的专业技能",
    },
    tools: {
      title:
        lang === "en" ? "Works with your favorite tools" : "支持你喜爱的工具",
    },
    cta: {
      title:
        lang === "en"
          ? "Ready to upgrade your AI?"
          : "准备好升级你的 AI 了吗？",
      desc:
        lang === "en"
          ? "Join the community and start building better context."
          : "加入社区，开始构建更好的上下文。",
      button: lang === "en" ? "Get Started Now" : "立即开始",
    },
  };

  return (
    <div className="relative flex min-h-screen flex-col font-sans">
      {/* Hero Section */}
      <section className="relative z-10 overflow-hidden pt-24 pb-56">
        <Hero3D />
        <div className="relative z-10 container mx-auto px-4">
          <div className="mx-auto max-w-4xl text-center">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.5 }}
            >
              <h1 className="mb-8 text-5xl leading-tight font-extrabold tracking-tight md:text-7xl">
                <span className="from-primary animate-gradient-x bg-gradient-to-r via-purple-500 to-blue-500 bg-clip-text text-transparent">
                  {t.hero.title}
                </span>
              </h1>
              <p className="text-foreground mb-6 text-2xl font-semibold md:text-3xl">
                {t.hero.subtitle}
              </p>
              <p className="text-muted-foreground mx-auto mb-12 max-w-2xl text-lg leading-relaxed md:text-xl">
                {t.hero.desc}
              </p>
              <div className="mb-16 flex flex-col items-center justify-center gap-4 sm:flex-row">
                <Link href={`/${lang}/docs/getting-started`}>
                  <Button
                    size="lg"
                    className="shadow-primary/25 hover:shadow-primary/40 h-14 rounded-full px-8 text-lg font-semibold shadow-lg transition-shadow"
                  >
                    {t.hero.getStarted} <ArrowRight className="ml-2 h-5 w-5" />
                  </Button>
                </Link>
                <Link
                  href="https://github.com/nicepkg/ai-workflow"
                  target="_blank"
                >
                  <Button
                    variant="outline"
                    size="lg"
                    className="bg-background/50 hover:bg-muted/50 border-primary/20 hover:border-primary/50 h-14 rounded-full px-8 text-lg backdrop-blur-sm"
                  >
                    <Github className="mr-2 h-5 w-5" /> {t.hero.viewGithub}
                  </Button>
                </Link>
              </div>

              <motion.div
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.3, duration: 0.5 }}
                className="mx-auto mt-8 max-w-3xl"
              >
                <div className="via-primary/20 rounded-2xl bg-gradient-to-r from-transparent to-transparent p-1">
                  <div className="bg-card/80 border-primary/10 rounded-xl border p-6 shadow-2xl backdrop-blur-md">
                    <div className="flex items-center overflow-x-auto text-left font-mono text-sm whitespace-nowrap md:text-base">
                      <span className="text-primary mr-3 select-none">$</span>
                      <span className="text-foreground">
                        npx add-skill
                        nicepkg/ai-workflow/workflows/content-creator-workflow
                      </span>
                    </div>
                  </div>
                </div>
              </motion.div>
            </motion.div>
          </div>
        </div>

        {/* Background gradients - Removed old static blobs */}
      </section>

      {/* Comparison Section */}
      <section className="relative overflow-hidden pt-0 pb-24">
        <div className="relative z-10 container mx-auto px-4">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="mb-20 text-center"
          >
            <h2 className="mb-6 text-3xl font-bold tracking-tight md:text-5xl">
              {t.problem.title}
            </h2>
          </motion.div>

          <div className="mx-auto grid max-w-7xl gap-8 md:grid-cols-3">
            {problems.map((item, i) => (
              <motion.div
                key={i}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                transition={{ delay: i * 0.1 }}
                viewport={{ once: true }}
                whileHover={{ y: -8 }}
                className="group relative h-full"
              >
                {/* Card Glow Effect */}
                <div className="from-primary/30 absolute -inset-0.5 rounded-3xl bg-gradient-to-b to-purple-600/30 opacity-30 blur transition duration-500 group-hover:opacity-100" />

                <div className="bg-card/80 relative flex h-full flex-col overflow-hidden rounded-3xl border border-white/10 p-8 backdrop-blur-xl dark:border-white/5">
                  {/* Subtle noise texture or pattern could go here */}

                  <div className="mb-8">
                    <h3 className="from-foreground to-foreground/70 group-hover:from-primary bg-gradient-to-r bg-clip-text text-2xl font-bold text-transparent transition-all duration-300 group-hover:to-purple-500">
                      {item.role[lang]}
                    </h3>
                  </div>

                  <div className="flex-1 space-y-6">
                    {/* The 'Pain' part */}
                    <div className="border-muted-foreground/20 relative border-l-2 pl-6 transition-colors group-hover:border-red-500/30">
                      <div className="bg-card border-muted-foreground/30 absolute top-0 -left-[9px] flex h-4 w-4 items-center justify-center rounded-full border-2">
                        <div className="bg-muted-foreground/50 h-1.5 w-1.5 rounded-full" />
                      </div>
                      <p className="text-muted-foreground mb-1 text-sm font-medium tracking-wider uppercase">
                        {t.problem.without}
                      </p>
                      <p className="text-muted-foreground/80 text-sm leading-relaxed line-through decoration-red-500/30 decoration-2">
                        {item.pain[lang]}
                      </p>
                    </div>

                    {/* Connector */}
                    <div className="flex items-center gap-4 opacity-30 transition-opacity duration-500 group-hover:opacity-100">
                      <div className="via-primary/50 h-px w-full bg-gradient-to-r from-transparent to-transparent" />
                      <ArrowRight className="text-primary h-4 w-4 shrink-0 rotate-90 md:rotate-0" />
                      <div className="via-primary/50 h-px w-full bg-gradient-to-r from-transparent to-transparent" />
                    </div>

                    {/* The 'Gain' part */}
                    <div className="border-primary/50 relative border-l-2 pl-6">
                      <div className="bg-primary absolute top-0 -left-[9px] flex h-4 w-4 items-center justify-center rounded-full shadow-[0_0_10px_rgba(139,92,246,0.5)]">
                        <CheckCircle className="h-3 w-3 text-white" />
                      </div>
                      <p className="text-primary mb-1 text-sm font-medium tracking-wider uppercase">
                        {t.problem.with}
                      </p>
                      <p className="text-foreground leading-relaxed font-medium">
                        {item.gain[lang]}
                      </p>
                    </div>
                  </div>
                </div>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Workflows Grid */}
      <section className="py-24">
        <div className="container mx-auto px-4">
          <div className="mb-20 text-center">
            <h2 className="mb-6 text-3xl font-bold md:text-5xl">
              {t.workflows.title}
            </h2>
            <p className="text-muted-foreground mx-auto max-w-2xl text-xl">
              {t.workflows.subtitle}
            </p>
          </div>

          <div className="mx-auto grid max-w-7xl grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-3">
            {workflows.map((wf, i) => (
              <Link
                href={`/${lang}${wf.link}`}
                key={i}
                className="block h-full"
              >
                <motion.div
                  whileHover={{ scale: 1.02, translateY: -4 }}
                  className="group border-border/50 from-card to-background hover:shadow-primary/5 relative h-full overflow-hidden rounded-3xl border bg-gradient-to-b p-8 transition-all duration-300 hover:shadow-2xl"
                >
                  <div
                    className={cn(
                      "absolute top-0 right-0 h-32 w-32 rounded-bl-full opacity-10 transition-transform group-hover:scale-110",
                      wf.bg,
                      wf.color,
                    )}
                  />

                  <div
                    className={cn(
                      "mb-6 flex h-14 w-14 items-center justify-center rounded-2xl shadow-sm",
                      wf.bg,
                      wf.color,
                    )}
                  >
                    <wf.icon className="h-7 w-7" />
                  </div>

                  <h3 className="group-hover:text-primary mb-3 text-2xl font-bold transition-colors">
                    {wf.title[lang]}
                  </h3>
                  <p className="text-muted-foreground text-lg leading-relaxed">
                    {wf.desc[lang]}
                  </p>

                  <div className="text-primary mt-8 flex -translate-x-2 items-center text-sm font-medium opacity-0 transition-all group-hover:translate-x-0 group-hover:opacity-100">
                    Learn more <ArrowRight className="ml-2 h-4 w-4" />
                  </div>
                </motion.div>
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* Tools Section */}
      <section className="bg-muted/20 border-y py-24">
        <div className="container mx-auto px-4 text-center">
          <h2 className="mb-12 text-2xl font-bold opacity-80">
            {t.tools.title}
          </h2>
          <div className="flex flex-wrap justify-center gap-x-12 gap-y-8">
            {[
              "Claude Code",
              "Cursor",
              "GitHub Copilot",
              "Codex",
              "OpenCode",
              "Roo Code",
              "Windsurf",
              "Gemini CLI",
              "Goose",
            ].map((tool) => (
              <div
                key={tool}
                className="text-muted-foreground hover:text-foreground flex cursor-default items-center gap-3 text-lg font-semibold transition-colors"
              >
                <div className="bg-background rounded-lg border p-2 shadow-sm">
                  <Terminal className="h-5 w-5" />
                </div>
                {tool}
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="relative overflow-hidden pt-24 pb-16 text-center">
        <div className="to-primary/5 absolute inset-0 -z-10 bg-gradient-to-b from-transparent" />
        <div className="relative container mx-auto px-4">
          <div className="bg-primary/10 absolute top-1/2 left-1/2 -z-10 h-[600px] w-[600px] -translate-x-1/2 -translate-y-1/2 rounded-full blur-[120px]" />

          <h2 className="mb-8 text-4xl font-bold tracking-tight md:text-6xl">
            {t.cta.title}
          </h2>
          <p className="text-muted-foreground mx-auto mb-12 max-w-2xl text-xl leading-relaxed md:text-2xl">
            {t.cta.desc}
          </p>
          <Link href={`/${lang}/docs/getting-started`}>
            <Button
              size="lg"
              className="shadow-primary/30 hover:shadow-primary/50 h-16 rounded-full px-12 text-xl shadow-2xl transition-all hover:scale-105"
            >
              {t.cta.button}
            </Button>
          </Link>
        </div>
      </section>
    </div>
  );
}
