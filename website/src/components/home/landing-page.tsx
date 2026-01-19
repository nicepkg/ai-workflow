"use client";

import { motion } from "framer-motion";
import {
  ArrowRight,
  Github,
  Zap,
  BookOpen,
  TrendingUp,
  Video,
  BarChart2,
  Presentation,
  CheckCircle,
  XCircle,
} from "lucide-react";
import dynamic from "next/dynamic";
import Link from "next/link";
import {
  AiToolIcon,
  toolLabelNameMap,
  toolLabels,
} from "~/components/shared/ai-tool-icon";
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
      <section className="relative overflow-hidden pt-0 pb-32">
        <div className="relative z-10 container mx-auto px-4">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="mb-24 text-center"
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
                whileHover={{ y: -5 }}
                className="group relative h-full"
              >
                {/* Card Container */}
                <div className="relative flex h-full flex-col overflow-hidden rounded-[2rem] border border-black/5 bg-white/80 shadow-2xl shadow-zinc-200/50 backdrop-blur-xl transition-all duration-500 hover:border-primary/20 hover:shadow-primary/5 dark:border-white/10 dark:bg-zinc-900/60 dark:shadow-black/50">
                  {/* Header: Role */}
                  <div className="px-8 pt-8 pb-4 text-center">
                    <h3 className="bg-gradient-to-br from-zinc-900 to-zinc-600 bg-clip-text text-2xl font-bold text-transparent transition-all duration-300 group-hover:from-primary group-hover:to-purple-600 dark:from-white dark:to-zinc-400">
                      {item.role[lang]}
                    </h3>
                  </div>

                  {/* Body */}
                  <div className="flex flex-1 flex-col p-4">
                    {/* The 'Pain' State */}
                    <div className="relative flex-1 rounded-2xl bg-zinc-50 p-6 transition-colors group-hover:bg-red-50/50 dark:bg-white/5 dark:group-hover:bg-red-950/20">
                      <div className="mb-3 flex items-center justify-between">
                        <span className="text-xs font-bold tracking-widest text-zinc-400 uppercase">
                          BEFORE
                        </span>
                        <XCircle className="h-5 w-5 text-zinc-300 transition-colors group-hover:text-red-400 dark:text-zinc-600" />
                      </div>
                      <p className="font-mono text-sm leading-relaxed text-zinc-500 transition-all decoration-red-400/50 group-hover:text-zinc-400 group-hover:line-through dark:text-zinc-400">
                        {item.pain[lang]}
                      </p>
                    </div>

                    {/* The Transformation Node */}
                    <div className="relative z-10 -my-5 flex justify-center">
                      <div className="flex h-12 w-12 items-center justify-center rounded-full border border-white bg-white shadow-lg transition-all duration-500 group-hover:scale-110 group-hover:border-primary/20 group-hover:shadow-primary/20 dark:border-zinc-800 dark:bg-zinc-900">
                        <Zap className="h-5 w-5 text-zinc-300 transition-colors group-hover:fill-primary group-hover:text-primary dark:text-zinc-600" />
                      </div>
                    </div>

                    {/* The 'Gain' State */}
                    <div className="relative flex-1 rounded-2xl bg-gradient-to-b from-blue-50/50 to-purple-50/50 p-6 pt-8 transition-colors group-hover:from-blue-50/80 group-hover:to-purple-50/80 dark:from-blue-900/10 dark:to-purple-900/10">
                      <div className="mb-3 flex items-center justify-between">
                        <span className="text-xs font-bold tracking-widest text-primary/80 uppercase">
                          AFTER
                        </span>
                        <CheckCircle className="h-5 w-5 text-primary" />
                      </div>
                      <p className="text-base font-semibold leading-relaxed text-zinc-800 dark:text-zinc-100">
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
      <section className="relative py-32">
        <div className="container relative z-10 mx-auto px-4">
          <div className="mb-24 text-center">
            <h2 className="mb-6 text-3xl font-bold md:text-5xl">
              {t.workflows.title}
            </h2>
            <p className="mx-auto max-w-2xl text-xl text-muted-foreground">
              {t.workflows.subtitle}
            </p>
          </div>

          <div className="mx-auto grid max-w-7xl grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">
            {workflows.map((wf, i) => (
              <Link
                href={`/${lang}${wf.link}`}
                key={i}
                className="group block h-full"
              >
                <motion.div
                  initial={{ opacity: 0, y: 20 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  transition={{ delay: i * 0.05 }}
                  viewport={{ once: true }}
                  className="relative h-full overflow-hidden rounded-[2rem] border border-border/50 bg-background/50 p-1 transition-all duration-500 hover:border-primary/20 hover:shadow-2xl hover:shadow-primary/5"
                >
                  <div className="relative flex h-full flex-col overflow-hidden rounded-[1.8rem] bg-card/50 p-8 backdrop-blur-xl transition-colors duration-500 group-hover:bg-card/80">
                    {/* Background Glow */}
                    <div
                      className={cn(
                        "absolute -right-20 -top-20 h-64 w-64 rounded-full opacity-0 blur-[80px] transition-all duration-700 group-hover:opacity-20",
                        wf.bg.replace("/10", ""), // Remove opacity modifier if present to get pure color
                        wf.color.replace("text-", "bg-"), // Convert text color class to bg color class
                      )}
                    />

                    {/* Icon Box */}
                    <div className="mb-8 flex items-start justify-between">
                      <div
                        className={cn(
                          "flex h-16 w-16 items-center justify-center rounded-2xl border border-white/10 shadow-lg transition-transform duration-500 group-hover:scale-110 group-hover:rotate-3",
                          wf.bg,
                          wf.color,
                        )}
                      >
                        <wf.icon className="h-8 w-8" />
                      </div>

                      <div className="flex h-10 w-10 items-center justify-center rounded-full border border-border/50 bg-background/50 opacity-0 transition-all duration-300 group-hover:opacity-100 group-hover:shadow-sm">
                        <ArrowRight className="h-4 w-4 -rotate-45 text-foreground transition-transform duration-300 group-hover:rotate-0" />
                      </div>
                    </div>

                    {/* Content */}
                    <div className="relative z-10 flex flex-1 flex-col">
                      <h3 className="mb-3 text-2xl font-bold tracking-tight text-foreground transition-colors group-hover:text-primary">
                        {wf.title[lang]}
                      </h3>
                      <p className="flex-1 text-lg leading-relaxed text-muted-foreground/80 transition-colors group-hover:text-muted-foreground">
                        {wf.desc[lang]}
                      </p>
                    </div>

                    {/* Bottom Decoration */}
                    <div className="mt-8 h-1 w-12 rounded-full bg-border transition-all duration-500 group-hover:w-full group-hover:bg-primary/20" />
                  </div>
                </motion.div>
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* Tools Section */}
      <section className="relative overflow-hidden border-y bg-muted/20 pt-24 pb-20">
        <div className="absolute inset-0 z-0 opacity-30">
          <div className="absolute inset-0 bg-[linear-gradient(to_right,#80808012_1px,transparent_1px),linear-gradient(to_bottom,#80808012_1px,transparent_1px)] bg-[size:24px_24px]"></div>
        </div>

        <div className="container relative z-10 mx-auto px-4 text-center">
          <h2 className="mb-6 text-3xl font-bold md:text-5xl">
            {t.tools.title}
          </h2>
          <p className="mx-auto mb-16 max-w-2xl text-xl text-muted-foreground">
            {lang === "en"
              ? "Seamlessly integrates with the AI coding assistants you already use."
              : "与你现有的 AI 编程助手无缝集成，即插即用。"}
          </p>
        </div>

        <div className="relative flex w-full flex-col gap-8">
          {/* Gradient Masks */}
          <div className="absolute top-0 bottom-0 left-0 z-20 w-32 bg-gradient-to-r from-background to-transparent" />
          <div className="absolute top-0 right-0 bottom-0 z-20 w-32 bg-gradient-to-l from-background to-transparent" />

          {/* First Row - Scrolling Left */}
          <div className="flex w-full overflow-hidden">
            <div className="flex animate-marquee items-center gap-6 pt-2 pb-6">
              {[...toolLabels, ...toolLabels.reverse()]
                .slice(0, 14)
                .map((toolLabel, i) => (
                  <div
                    key={`row1-${i}`}
                    className="group flex w-[240px] cursor-default items-center gap-4 rounded-2xl border border-white/5 bg-background/40 p-5 shadow-sm backdrop-blur-md transition-all duration-300 hover:border-primary/50 hover:bg-background/80 hover:shadow-xl hover:shadow-primary/10"
                  >
                    <div className="flex h-12 w-12 items-center justify-center rounded-xl bg-background shadow-inner">
                      <AiToolIcon
                        label={toolLabel}
                        size={28}
                        className="text-muted-foreground transition-all duration-300 group-hover:scale-110 group-hover:text-foreground"
                      />
                    </div>
                    <span className="text-lg font-semibold text-muted-foreground transition-colors group-hover:text-foreground">
                      {toolLabelNameMap[toolLabel]}
                    </span>
                  </div>
                ))}
            </div>
          </div>

          {/* Second Row - Scrolling Right */}
          <div className="flex w-full overflow-hidden">
            <div className="flex animate-marquee-reverse items-center gap-6 pt-2 pb-6">
              {[...toolLabels, ...toolLabels]
                .slice(7, 21)
                .map((toolLabel, i) => (
                  <div
                    key={`row2-${i}`}
                    className="group flex w-[240px] cursor-default items-center gap-4 rounded-2xl border border-white/5 bg-background/40 p-5 shadow-sm backdrop-blur-md transition-all duration-300 hover:border-primary/50 hover:bg-background/80 hover:shadow-xl hover:shadow-primary/10"
                  >
                    <div className="flex h-12 w-12 items-center justify-center rounded-xl bg-background shadow-inner">
                      <AiToolIcon
                        label={toolLabel}
                        size={28}
                        className="text-muted-foreground transition-all duration-300 group-hover:scale-110 group-hover:text-foreground"
                      />
                    </div>
                    <span className="text-lg font-semibold text-muted-foreground transition-colors group-hover:text-foreground">
                      {toolLabelNameMap[toolLabel]}
                    </span>
                  </div>
                ))}
            </div>
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
