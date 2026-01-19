import type { SVGProps } from "react";
import { cn } from "~/lib/utils";
import AmpIcon from "../../../public/icons/amp.svg";
import AntigravityIcon from "../../../public/icons/antigravity.svg";
import ClaudeCodeIcon from "../../../public/icons/claude-code.svg";
import ClawdbotIcon from "../../../public/icons/clawdbot.svg";
import CodexIcon from "../../../public/icons/codex.svg";
import CursorIcon from "../../../public/icons/cursor.svg";
import DroidIcon from "../../../public/icons/droid.svg";
import GeminiCliIcon from "../../../public/icons/gemini-cli.svg";
import GithubCopilotIcon from "../../../public/icons/github-copilot.svg";
import GooseIcon from "../../../public/icons/goose.svg";
import KiloCodeIcon from "../../../public/icons/kilo-code.svg";
import OpenCodeIcon from "../../../public/icons/opencode.svg";
import RooCodeIcon from "../../../public/icons/roo-code.svg";
import WindsurfIcon from "../../../public/icons/windsurf.svg";

const toolIconMap = {
  // Claude Code
  "claude-code": ClaudeCodeIcon,
  // Cursor
  cursor: CursorIcon,
  // GitHub Copilot
  "github-copilot": GithubCopilotIcon,
  // Codex
  codex: CodexIcon,
  // OpenCode
  opencode: OpenCodeIcon,
  // Amp
  amp: AmpIcon,
  // Roo Code
  "roo-code": RooCodeIcon,
  // Kilo Code
  "kilo-code": KiloCodeIcon,
  // Goose
  goose: GooseIcon,
  // Gemini CLI
  "gemini-cli": GeminiCliIcon,
  // Antigravity
  antigravity: AntigravityIcon,
  // Clawdbot
  clawdbot: ClawdbotIcon,
  // Droid
  droid: DroidIcon,
  // Windsurf
  windsurf: WindsurfIcon,
} as const;

export type AiToolName = keyof typeof toolIconMap;

type AiToolIconProps = {
  name: AiToolName;
  size?: number;
  className?: string;
  title?: string;
  decorative?: boolean;
} & Omit<SVGProps<SVGSVGElement>, "name" | "width" | "height">;

export const toolLabels: Record<AiToolName, string> = {
  "claude-code": "Claude Code",
  cursor: "Cursor",
  "github-copilot": "GitHub Copilot",
  codex: "Codex",
  opencode: "OpenCode",
  amp: "Amp",
  "roo-code": "Roo Code",
  "kilo-code": "Kilo Code",
  goose: "Goose",
  "gemini-cli": "Gemini CLI",
  antigravity: "Antigravity",
  clawdbot: "Clawdbot",
  droid: "Droid",
  windsurf: "Windsurf",
};

export function AiToolIcon({
  name,
  size = 24,
  className,
  title,
  decorative = false,
  ...props
}: AiToolIconProps) {
  const Icon = toolIconMap[name];
  const label = title ?? toolLabels[name];

  return (
    <Icon
      width={size}
      height={size}
      className={cn("shrink-0 text-foreground", className)}
      role="img"
      aria-label={decorative ? undefined : label}
      aria-hidden={decorative || undefined}
      {...props}
    />
  );
}
