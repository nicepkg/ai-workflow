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
    href: "https://www.douyin.com/user/MS4wLjABAAAA52y61t47bXUa3_w0g_A4g8x8q8q8q8q8q8q8q8q8q8o", // Placeholder or just disable link if unknown
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
    <footer className="bg-background border-t py-12">
      <div className="container mx-auto px-4">
        <div className="flex flex-col md:flex-row justify-between items-center gap-6">
          <div className="flex flex-col items-center md:items-start gap-4">
            <div className="text-lg font-bold">AI Workflow</div>
            <p className="text-sm text-muted-foreground text-center md:text-left max-w-sm">
              Supercharge your AI coding workflow with context-aware skills and best practices.
            </p>
            <div className="flex gap-4 text-sm text-muted-foreground">
              <span>© {new Date().getFullYear()} AI Workflow</span>
            </div>
          </div>

          <div className="flex flex-col items-center md:items-end gap-4">
            <div className="flex gap-4">
              {socialLinks.map((social) => (
                <Link
                  key={social.label}
                  href={social.href || "#"}
                  target="_blank"
                  rel="noreferrer"
                  className={cn(
                    "text-muted-foreground hover:text-foreground transition-colors p-2 rounded-full hover:bg-muted",
                    !social.href && "cursor-default hover:text-muted-foreground hover:bg-transparent"
                  )}
                  title={social.handle ? `${social.label}: ${social.handle}` : social.label}
                >
                  <social.Icon className="w-5 h-5 fill-current" />
                  <span className="sr-only">{social.label}</span>
                </Link>
              ))}
            </div>
            <div className="flex gap-6 text-sm">
              {footerLinks.map((link) => (
                <Link
                  key={link.label}
                  href={link.href}
                  target="_blank"
                  rel="noreferrer"
                  className="text-muted-foreground hover:text-foreground transition-colors"
                >
                  {link.label}
                </Link>
              ))}
            </div>
          </div>
        </div>
      </div>
    </footer>
  );
}
