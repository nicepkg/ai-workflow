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
    pain: { en: "Teaching UTM parameters, AIDA copywriting, funnel optimization...", zh: "教 UTM 参数、AIDA 文案法、漏斗优化..." },
    gain: { en: "AI equipped with GTM strategy, campaign templates, analytics frameworks", zh: "AI 已配备 GTM 策略、活动模板、分析框架" }
  },
  {
    role: { en: "Stock Trader", zh: "股票交易员" },
    pain: { en: "MACD means..., RSI indicates..., check the 200-day MA...", zh: "MACD 意味着...、RSI 表示...、看 200 日均线..." },
    gain: { en: "AI loaded with technical analysis, fundamentals, multi-market expertise", zh: "AI 已加载技术分析、基本面、多市场专业知识" }
  },
]

type Translation = {
  hero: {
    title: string
    subtitle: string
    desc: string
    getStarted: string
    viewGithub: string
  }
  problem: {
    title: string
    without: string
    with: string
  }
  workflows: {
    title: string
    subtitle: string
  }
  tools: {
    title: string
  }
  cta: {
    title: string
    desc: string
    button: string
  }
}

export function LandingPage({ lang }: { lang: 'en' | 'zh' }) {
  const t: Translation = {
    hero: {
      title: lang === 'en' ? "Supercharge your AI Workflow" : "AI 工作流的究极形态",
      subtitle: lang === 'en' 
        ? "Stop repeating yourself. Start with context." 
        : "告别重复解释。让 AI 真正懂你。",
      desc: lang === 'en'
        ? "Every session starts from zero. One command adds professional skills, best practices, and project context to your AI."
        : "每次对话都从零开始？一条命令，为你的 AI 注入专业技能、最佳实践和项目上下文。",
      getStarted: lang === 'en' ? "Get Started" : "开始使用",
      viewGithub: lang === 'en' ? "Star on GitHub" : "Star on GitHub",
    },
    problem: {
      title: lang === 'en' ? "The Problem We Solve" : "我们解决的痛点",
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
    <div className="flex flex-col min-h-screen font-sans relative">
      {/* Hero Section */}
      <section className="relative pt-24 pb-32 md:pt-32 md:pb-40 overflow-hidden z-10">
        <div className="container mx-auto px-4 relative z-10">
          <div className="max-w-4xl mx-auto text-center">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.5 }}
            >
              <h1 className="text-5xl md:text-7xl font-extrabold tracking-tight mb-8 leading-tight">
                <span className="bg-clip-text text-transparent bg-gradient-to-r from-primary via-purple-500 to-blue-500 animate-gradient-x">
                  {t.hero.title}
                </span>
              </h1>
              <p className="text-2xl md:text-3xl font-semibold text-foreground mb-6">
                {t.hero.subtitle}
              </p>
              <p className="text-lg md:text-xl text-muted-foreground mb-12 max-w-2xl mx-auto leading-relaxed">
                {t.hero.desc}
              </p>
              <div className="flex flex-col sm:flex-row items-center justify-center gap-4 mb-16">
                <Link href={`/${lang}/docs/getting-started`}>
                  <Button size="lg" className="rounded-full px-8 h-14 text-lg font-semibold shadow-lg shadow-primary/25 hover:shadow-primary/40 transition-shadow">
                    {t.hero.getStarted} <ArrowRight className="ml-2 w-5 h-5" />
                  </Button>
                </Link>
                <Link href="https://github.com/nicepkg/ai-workflow" target="_blank">
                  <Button variant="outline" size="lg" className="rounded-full px-8 h-14 text-lg bg-background/50 backdrop-blur-sm hover:bg-muted/50 border-primary/20 hover:border-primary/50">
                    <Github className="mr-2 w-5 h-5" /> {t.hero.viewGithub}
                  </Button>
                </Link>
              </div>
              
              <motion.div 
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.3, duration: 0.5 }}
                className="mt-8 mx-auto max-w-3xl"
              >
                <div className="p-1 rounded-2xl bg-gradient-to-r from-transparent via-primary/20 to-transparent">
                  <div className="bg-card/80 backdrop-blur-md border border-primary/10 rounded-xl p-6 shadow-2xl">
                    <div className="font-mono text-sm md:text-base text-left overflow-x-auto whitespace-nowrap flex items-center">
                      <span className="text-primary mr-3 select-none">$</span>
                      <span className="text-foreground">npx add-skill nicepkg/ai-workflow/workflows/content-creator-workflow</span>
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
      <section className="py-24 relative overflow-hidden">
        <div className="absolute inset-0 bg-muted/50 -z-20" />
        <div className="container mx-auto px-4">
          <motion.div
             initial={{ opacity: 0, y: 20 }}
             whileInView={{ opacity: 1, y: 0 }}
             viewport={{ once: true }}
             className="text-center mb-16"
          >
            <h2 className="text-3xl md:text-5xl font-bold mb-6">{t.problem.title}</h2>
          </motion.div>
          
          <div className="grid md:grid-cols-3 gap-8 max-w-7xl mx-auto">
            {problems.map((item, i) => (
              <motion.div 
                key={i}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                transition={{ delay: i * 0.1 }}
                viewport={{ once: true }}
                whileHover={{ y: -5 }}
                className="bg-background rounded-2xl border border-border/50 shadow-sm p-8 hover:shadow-xl hover:shadow-primary/5 transition-all duration-300 relative group"
              >
                <div className="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-transparent via-primary/50 to-transparent opacity-0 group-hover:opacity-100 transition-opacity" />
                <h3 className="font-bold text-2xl mb-6 text-center">{item.role[lang]}</h3>
                <div className="space-y-6">
                  <div className="space-y-2">
                     <div className="text-sm font-semibold text-muted-foreground uppercase tracking-wider pl-1">{t.problem.without}</div>
                     <div className="p-4 bg-red-500/5 rounded-xl border border-red-500/10 group-hover:border-red-500/20 transition-colors">
                      <div className="flex items-start gap-3 text-red-600 dark:text-red-400">
                        <XCircle className="w-5 h-5 shrink-0 mt-0.5" />
                        <span className="leading-relaxed">{item.pain[lang]}</span>
                      </div>
                    </div>
                  </div>
                  
                  <div className="flex justify-center">
                    <ArrowRight className="w-6 h-6 text-muted-foreground/30 rotate-90 md:rotate-0" />
                  </div>

                  <div className="space-y-2">
                    <div className="text-sm font-semibold text-muted-foreground uppercase tracking-wider pl-1">{t.problem.with}</div>
                    <div className="p-4 bg-green-500/5 rounded-xl border border-green-500/10 group-hover:border-green-500/20 transition-colors">
                      <div className="flex items-start gap-3 text-green-600 dark:text-green-400">
                        <CheckCircle className="w-5 h-5 shrink-0 mt-0.5" />
                        <span className="leading-relaxed font-medium">{item.gain[lang]}</span>
                      </div>
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
          <div className="text-center mb-20">
            <h2 className="text-3xl md:text-5xl font-bold mb-6">{t.workflows.title}</h2>
            <p className="text-muted-foreground text-xl max-w-2xl mx-auto">{t.workflows.subtitle}</p>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 max-w-7xl mx-auto">
            {workflows.map((wf, i) => (
              <Link href={`/${lang}${wf.link}`} key={i} className="block h-full">
                <motion.div
                  whileHover={{ scale: 1.02, translateY: -4 }}
                  className="group h-full p-8 rounded-3xl border border-border/50 bg-gradient-to-b from-card to-background hover:shadow-2xl hover:shadow-primary/5 transition-all duration-300 relative overflow-hidden"
                >
                  <div className={cn("absolute top-0 right-0 w-32 h-32 rounded-bl-full opacity-10 transition-transform group-hover:scale-110", wf.bg, wf.color)} />
                  
                  <div className={cn("w-14 h-14 rounded-2xl flex items-center justify-center mb-6 shadow-sm", wf.bg, wf.color)}>
                    <wf.icon className="w-7 h-7" />
                  </div>
                  
                  <h3 className="text-2xl font-bold mb-3 group-hover:text-primary transition-colors">{wf.title[lang]}</h3>
                  <p className="text-muted-foreground leading-relaxed text-lg">{wf.desc[lang]}</p>
                  
                  <div className="mt-8 flex items-center text-sm font-medium text-primary opacity-0 -translate-x-2 group-hover:opacity-100 group-hover:translate-x-0 transition-all">
                    Learn more <ArrowRight className="ml-2 w-4 h-4" />
                  </div>
                </motion.div>
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* Tools Section */}
      <section className="py-24 border-y bg-muted/20">
        <div className="container mx-auto px-4 text-center">
          <h2 className="text-2xl font-bold mb-12 opacity-80">{t.tools.title}</h2>
          <div className="flex flex-wrap justify-center gap-x-12 gap-y-8">
             {["Claude Code", "Cursor", "GitHub Copilot", "Codex", "OpenCode", "Roo Code", "Windsurf", "Gemini CLI", "Goose"].map((tool) => (
               <div key={tool} className="flex items-center gap-3 text-lg font-semibold text-muted-foreground hover:text-foreground transition-colors cursor-default">
                 <div className="p-2 bg-background rounded-lg shadow-sm border">
                    <Terminal className="w-5 h-5" />
                 </div>
                 {tool}
               </div>
             ))}
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="py-32 text-center relative overflow-hidden">
        <div className="absolute inset-0 bg-gradient-to-b from-transparent to-primary/5 -z-10" />
        <div className="container mx-auto px-4 relative">
          <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-primary/10 rounded-full blur-[120px] -z-10" />
          
          <h2 className="text-4xl md:text-6xl font-bold mb-8 tracking-tight">{t.cta.title}</h2>
          <p className="text-xl md:text-2xl text-muted-foreground mb-12 max-w-2xl mx-auto leading-relaxed">{t.cta.desc}</p>
          <Link href={`/${lang}/docs/getting-started`}>
            <Button size="lg" className="rounded-full px-12 h-16 text-xl shadow-2xl shadow-primary/30 hover:shadow-primary/50 hover:scale-105 transition-all">
              {t.cta.button}
            </Button>
          </Link>
        </div>
      </section>
    </div>
  )
}
