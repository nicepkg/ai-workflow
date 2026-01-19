import Link from "next/link";
import { cn } from "~/lib/utils";
import { GitHubIcon, BilibiliIcon, DouyinIcon, XIcon } from "./social-icons";

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
        <div className="grid grid-cols-1 gap-8 md:grid-cols-2 lg:gap-12">
          {/* Left Column: Brand & Description */}
          <div className="flex flex-col gap-4">
            <Link
              href="/"
              className="flex items-center gap-2 text-xl font-bold"
            >
              AI Workflow
            </Link>
            <p className="text-muted-foreground max-w-sm text-sm leading-relaxed">
              Supercharge your AI coding workflow with context-aware skills and
              best practices. Built for developers who want to stop repeating
              themselves.
            </p>
          </div>

          {/* Right Column: Links & Socials */}
          <div className="flex flex-col justify-between gap-6 md:items-end">
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
                    "text-muted-foreground hover:text-foreground hover:bg-muted/50 rounded-full p-2 transition-all hover:scale-110",
                    !social.href &&
                      "hover:text-muted-foreground cursor-default hover:scale-100 hover:bg-transparent",
                  )}
                  title={
                    social.handle
                      ? `${social.label}: ${social.handle}`
                      : social.label
                  }
                  aria-label={social.label}
                >
                  <social.Icon className="h-5 w-5 fill-current" />
                </Link>
              ))}
            </div>
          </div>
        </div>

        {/* Bottom Bar: Copyright */}
        <div className="text-muted-foreground mt-12 flex flex-col items-center justify-between gap-4 border-t pt-8 text-xs md:flex-row">
          <p>
            © {new Date().getFullYear()} AI Workflow. Released under the MIT
            License.
          </p>
          <p className="flex items-center gap-1">
            Built with <span className="text-red-500">♥</span> by{" "}
            <a
              href="https://github.com/2214962083"
              target="_blank"
              rel="noreferrer"
              className="hover:text-foreground hover:underline"
            >
              Xiaoming
            </a>
          </p>
        </div>
      </div>
    </footer>
  );
}
