import Link from "next/link";
import { GitHubIcon, BilibiliIcon, DouyinIcon, XIcon } from "./social-icons";
import { cn } from "~/lib/utils";

const socialLinks = [
  {
    label: "GitHub",
    href: "https://github.com/2214962083",
    Icon: GitHubIcon,
  },
  {
    label: "Bilibili",
    href: "https://space.bilibili.com/83540912",
    Icon: BilibiliIcon,
  },
  {
    label: "Douyin",
    href: "https://www.douyin.com/user/MS4wLjABAAAA52y61t47bXUa3_w0g_A4g8x8q8q8q8q8q8q8q8q8q8o",
    handle: "葬爱非主流小明",
    Icon: DouyinIcon,
  },
  {
    label: "X (Twitter)",
    href: "https://x.com/jinmingyang666",
    Icon: XIcon,
  },
];

const footerLinks = [
  { label: "Xiaoming Lab", href: "https://xiaominglab.com" },
  { label: "NicePkg", href: "https://github.com/nicepkg" },
  { label: "About Author", href: "https://github.com/2214962083" },
];

export function SiteFooter() {
  return (
    <footer className="bg-background border-t">
      <div className="container mx-auto px-4 py-12 md:py-16">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8 lg:gap-12">
          {/* Left Column: Brand & Description */}
          <div className="flex flex-col gap-4">
            <Link href="/" className="text-xl font-bold flex items-center gap-2">
              AI Workflow
            </Link>
            <p className="text-muted-foreground text-sm leading-relaxed max-w-sm">
              Supercharge your AI coding workflow with context-aware skills and best practices. 
              Built for developers who want to stop repeating themselves.
            </p>
          </div>

          {/* Right Column: Links & Socials */}
          <div className="flex flex-col gap-6 md:items-end justify-between">
             {/* Navigation Links - Prominent & Horizontal */}
             <nav className="flex flex-wrap gap-x-8 gap-y-4 text-sm font-medium">
              {footerLinks.map((link) => (
                <Link
                  key={link.label}
                  href={link.href}
                  target="_blank"
                  rel="noreferrer"
                  className="hover:text-primary transition-colors"
                >
                  {link.label}
                </Link>
              ))}
            </nav>

            {/* Social Icons */}
            <div className="flex items-center gap-4">
              {socialLinks.map((social) => (
                <Link
                  key={social.label}
                  href={social.href || "#"}
                  target="_blank"
                  rel="noreferrer"
                  className={cn(
                    "text-muted-foreground hover:text-foreground transition-all hover:scale-110 p-2 rounded-full hover:bg-muted/50",
                    !social.href && "cursor-default hover:text-muted-foreground hover:bg-transparent hover:scale-100"
                  )}
                  title={social.handle ? `${social.label}: ${social.handle}` : social.label}
                  aria-label={social.label}
                >
                  <social.Icon className="w-5 h-5 fill-current" />
                </Link>
              ))}
            </div>
          </div>
        </div>

        {/* Bottom Bar: Copyright */}
        <div className="mt-12 pt-8 border-t flex flex-col md:flex-row justify-between items-center gap-4 text-xs text-muted-foreground">
          <p>© {new Date().getFullYear()} AI Workflow. Released under the MIT License.</p>
          <p className="flex items-center gap-1">
            Built with <span className="text-red-500">♥</span> by <a href="https://github.com/2214962083" target="_blank" rel="noreferrer" className="hover:underline hover:text-foreground">Xiaoming</a>
          </p>
        </div>
      </div>
    </footer>
  );
}
