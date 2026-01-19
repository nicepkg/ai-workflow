'use client'

import { cn } from "~/lib/utils"
import { Button } from "~/components/ui/button"
import { motion } from "framer-motion"
import { ArrowRight, Github, Terminal, Zap, BookOpen, TrendingUp, Video, BarChart2, Presentation, CheckCircle, XCircle } from "lucide-react"
import Link from "next/link"

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
]

const problems = [
  {
    role: { en: "Content Creator", zh: "内容创作者" },
    pain: { en: "Explaining SEO basics, H2 structure, meta descriptions... every single time", zh: "每次都要解释 SEO 基础、H2 结构、meta 描述..." },
    gain: { en: "AI pre-loaded with SEO best practices, content frameworks", zh: "AI 已预装 SEO 最佳实践、内容框架" }
  },
  {
    role: { en: "Marketer", zh: "营销人员" },
    pain: { en: "Teaching UTM parameters, AIDA copywriting...", zh: "教 UTM 参数、AIDA 文案法..." },
    gain: { en: "AI equipped with GTM strategy, campaign templates", zh: "AI 已配备 GTM 策略、活动模板" }
  },
    {
    role: { en: "Developer", zh: "开发者" },
    pain: { en: "Copy-pasting context, explaining stack...", zh: "复制粘贴上下文，解释技术栈..." },
    gain: { en: "One command adds full project context & skills", zh: "一条命令添加完整项目上下文和技能" }
  },
]

export function LandingPage({ lang }: { lang: 'en' | 'zh' }) {
  const t = {
    hero: {
      title: lang === 'en' ? "Supercharge your AI Workflow" : "AI 工作流的究极形态",
      subtitle: lang === 'en' 
        ? "Stop repeating yourself. Start with context." 
        : "告别重复解释。让 AI 真正懂你。",
      desc: lang === 'en'
        ? "Every session starts from zero. One command adds professional skills, best practices, and project context to your AI."
        : "每次对话都从零开始？一条命令，为你的 AI 注入专业技能、最佳实践和项目上下文。",
      getStarted: lang === 'en' ? "Get Started" : "开始使用",
      viewGithub: lang === 'en' ? "View on GitHub" : "GitHub",
    },
    problem: {
      title: lang === 'en' ? "The Problem" : "我们解决的痛点",
      without: lang === 'en' ? "Without AI Workflow" : "没有 AI Workflow",
      with: lang === 'en' ? "With AI Workflow" : "有了 AI Workflow",
    },
    workflows: {
      title: lang === 'en' ? "Explore Workflows" : "探索工作流",
      subtitle: lang === 'en' ? " Specialized skills for every role" : "为每个角色打造的专业技能",
    },
    tools: {
      title: lang === 'en' ? "Works with your favorite tools" : "支持你喜爱的工具",
    },
    cta: {
      title: lang === 'en' ? "Ready to upgrade your AI?" : "准备好升级你的 AI 了吗？",
      desc: lang === 'en' 
        ? "Join the community and start building better context."
        : "加入社区，开始构建更好的上下文。",
      button: lang === 'en' ? "Get Started Now" : "立即开始",
    }
  }

  return (
    <div className="flex flex-col min-h-screen">
      {/* Hero Section */}
      <section className="relative pt-20 pb-32 overflow-hidden">
        <div className="container mx-auto px-4 relative z-10">
          <div className="max-w-4xl mx-auto text-center">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.5 }}
            >
              <h1 className="text-5xl md:text-7xl font-bold tracking-tight mb-6 bg-clip-text text-transparent bg-gradient-to-r from-primary to-purple-600 dark:to-purple-400">
                {t.hero.title}
              </h1>
              <p className="text-2xl md:text-3xl font-medium text-muted-foreground mb-6">
                {t.hero.subtitle}
              </p>
              <p className="text-lg text-muted-foreground/80 mb-10 max-w-2xl mx-auto">
                {t.hero.desc}
              </p>
              <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
                <Link href={`/${lang}/docs/getting-started`}>
                  <Button size="lg" className="rounded-full px-8 text-lg h-12">
                    {t.hero.getStarted} <ArrowRight className="ml-2 w-5 h-5" />
                  </Button>
                </Link>
                <Link href="https://github.com/nicepkg/ai-workflow" target="_blank">
                  <Button variant="outline" size="lg" className="rounded-full px-8 text-lg h-12">
                    <Github className="mr-2 w-5 h-5" /> {t.hero.viewGithub}
                  </Button>
                </Link>
              </div>
              
              <div className="mt-12 p-4 rounded-xl bg-muted/50 backdrop-blur-sm border inline-block text-left font-mono text-sm md:text-base">
                 <span className="text-primary mr-2">$</span>
                 npx add-skill nicepkg/ai-workflow/workflows/content-creator-workflow
              </div>
            </motion.div>
          </div>
        </div>
        
        {/* Background gradients */}
        <div className="absolute top-0 left-1/2 -translate-x-1/2 w-full h-full max-w-7xl -z-10 opacity-30 dark:opacity-20 pointer-events-none">
            <div className="absolute top-10 left-10 w-72 h-72 bg-purple-500 rounded-full mix-blend-multiply filter blur-3xl animate-blob" />
            <div className="absolute top-10 right-10 w-72 h-72 bg-yellow-500 rounded-full mix-blend-multiply filter blur-3xl animate-blob animation-delay-2000" />
            <div className="absolute -bottom-8 left-20 w-72 h-72 bg-pink-500 rounded-full mix-blend-multiply filter blur-3xl animate-blob animation-delay-4000" />
        </div>
      </section>

      {/* Comparison Section */}
      <section className="py-20 bg-muted/30">
        <div className="container mx-auto px-4">
          <h2 className="text-3xl font-bold text-center mb-12">{t.problem.title}</h2>
          <div className="grid md:grid-cols-3 gap-6 max-w-6xl mx-auto">
            {problems.map((item, i) => (
              <motion.div 
                key={i}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                transition={{ delay: i * 0.1 }}
                viewport={{ once: true }}
                className="bg-background rounded-xl border shadow-sm p-6 hover:shadow-md transition-shadow"
              >
                <h3 className="font-bold text-xl mb-4 text-center">{item.role[lang]}</h3>
                <div className="space-y-4">
                  <div className="p-3 bg-red-500/5 rounded-lg border border-red-500/10">
                    <div className="flex items-start gap-2 text-red-600 dark:text-red-400 text-sm">
                      <XCircle className="w-5 h-5 shrink-0" />
                      <span>{item.pain[lang]}</span>
                    </div>
                  </div>
                  <div className="p-3 bg-green-500/5 rounded-lg border border-green-500/10">
                    <div className="flex items-start gap-2 text-green-600 dark:text-green-400 text-sm">
                      <CheckCircle className="w-5 h-5 shrink-0" />
                      <span>{item.gain[lang]}</span>
                    </div>
                  </div>
                </div>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Workflows Grid */}
      <section className="py-20">
        <div className="container mx-auto px-4">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold mb-4">{t.workflows.title}</h2>
            <p className="text-muted-foreground text-lg">{t.workflows.subtitle}</p>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 max-w-6xl mx-auto">
            {workflows.map((wf, i) => (
              <Link href={`/${lang}${wf.link}`} key={i}>
                <motion.div
                  whileHover={{ scale: 1.02 }}
                  className="group h-full p-6 rounded-2xl border bg-card hover:border-primary/50 transition-colors"
                >
                  <div className={cn("w-12 h-12 rounded-lg flex items-center justify-center mb-4", wf.bg, wf.color)}>
                    <wf.icon className="w-6 h-6" />
                  </div>
                  <h3 className="text-xl font-bold mb-2 group-hover:text-primary transition-colors">{wf.title[lang]}</h3>
                  <p className="text-muted-foreground">{wf.desc[lang]}</p>
                </motion.div>
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* Tools Section */}
      <section className="py-20 bg-muted/30 border-y">
        <div className="container mx-auto px-4 text-center">
          <h2 className="text-2xl font-bold mb-10">{t.tools.title}</h2>
          <div className="flex flex-wrap justify-center gap-x-8 gap-y-4 text-muted-foreground font-medium">
             {["Claude Code", "Cursor", "GitHub Copilot", "Codex", "OpenCode", "Roo Code", "Windsurf"].map((tool) => (
               <span key={tool} className="flex items-center gap-2">
                 <Terminal className="w-4 h-4" /> {tool}
               </span>
             ))}
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="py-24 text-center">
        <div className="container mx-auto px-4">
          <h2 className="text-3xl md:text-4xl font-bold mb-6">{t.cta.title}</h2>
          <p className="text-xl text-muted-foreground mb-10 max-w-2xl mx-auto">{t.cta.desc}</p>
          <Link href={`/${lang}/docs/getting-started`}>
            <Button size="lg" className="rounded-full px-10 h-14 text-lg shadow-lg shadow-primary/20">
              {t.cta.button}
            </Button>
          </Link>
        </div>
      </section>
    </div>
  )
}
