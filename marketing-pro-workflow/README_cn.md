# Marketing Pro Workflow

数字营销人员、增长黑客、营销团队专用的Claude Code工作流。

## 适合人群

- 数字营销人员
- 增长营销 & 需求获取
- 产品市场经理 (PMM)
- 社交媒体经理
- SEO专家
- 付费广告专家

## 已安装Skills (18个)

### 策略与研究
| Skill | 功能 | 触发示例 |
|-------|------|---------|
| marketing-strategy-pmm | 产品营销、定位、GTM、ICP定义、竞品战卡 | "为[产品]创建定位" |
| marketing-demand-acquisition | 多渠道需求获取、付费广告优化、SEO策略、CAC计算 | "规划需求获取活动" |
| buyer-persona-generator | 创建详细买家画像和ICP | "为[角色]创建买家画像" |
| competitive-ads-extractor | 从广告库提取分析竞品广告 | "分析[公司]的竞品广告" |
| lead-research-assistant | 为产品识别和筛选潜在客户 | "为[产品]找10个线索" |

### SEO与内容
| Skill | 功能 | 触发示例 |
|-------|------|---------|
| seo-optimizer | SEO内容优化 | "优化这篇文章的SEO" |
| content-optimizer | 页面SEO、关键词密度、meta标签 | "检查关键词密度" |
| serp-analysis | SERP分析和竞争情报 | "分析[关键词]的搜索结果" |
| keyword-cluster-builder | 关键词扩展和聚类 | "为[主题]构建关键词聚类" |
| content-brief | SEO内容规划简报 | "创建内容规划简报" |

### 广告与活动
| Skill | 功能 | 触发示例 |
|-------|------|---------|
| ad-copy-generator | 生成Google、Meta、LinkedIn、TikTok广告文案 | "创建5个Google广告变体" |
| landing-page-copywriter | 落地页文案（AIDA框架） | "写落地页文案" |
| email-template-generator | 邮件营销模板和序列 | "生成邮件序列" |
| utm-builder | 生成UTM追踪链接 | "为活动创建UTM链接" |

### 社交媒体
| Skill | 功能 | 触发示例 |
|-------|------|---------|
| linkedin-post-optimizer | LinkedIn帖子优化 | "优化LinkedIn帖子" |
| social-repurposer | 跨平台内容转换 | "转换为各平台格式" |
| social-media-analyzer | 分析活动表现、互动、ROI | "分析这份活动数据" |

### 数据分析
| Skill | 功能 | 触发示例 |
|-------|------|---------|
| analytics-interpretation | GA4/GSC数据解读 | "解读这份分析数据" |

## 快速开始

```bash
cd marketing-pro-workflow
# 启动Claude Code，skills自动激活
```

## 自动化营销工作流

### 1. 完整GTM策略
```
1. "为[产品]创建ICP和3个买家画像"
2. "使用April Dunford方法开发定位"
3. "为[竞争对手]创建竞品战卡"
4. "规划90天GTM发布计划"
```

### 2. 全漏斗活动
```
1. "为[产品]规划需求获取活动"
2. "为Google和LinkedIn生成广告文案"
3. "为所有渠道创建UTM链接"
4. "写5封邮件培育序列"
5. "创建落地页文案"
```

### 3. SEO内容策略
```
1. "为[主题]构建关键词聚类"
2. "分析[主要关键词]的搜索结果"
3. "根据分析创建内容规划简报"
4. "使用content-optimizer检查SEO要求"
```

### 4. 竞争情报
```
1. "分析[公司]的竞品广告"
2. "创建竞品战卡"
3. "识别竞品信息的差距"
4. "生成差异化广告文案"
```

### 5. 线索获取活动
```
1. "找20个符合我们ICP的潜在客户"
2. "创建个性化外联信息"
3. "生成针对这个细分市场的LinkedIn广告"
4. "为所有触点创建UTM追踪"
```

### 6. 效果分析
```
1. "分析这份GA4活动数据"
2. "按渠道计算CAC"
3. "解读社交媒体互动指标"
4. "提供优化建议"
```

## Skill组合

- **产品发布**: buyer-persona-generator → marketing-strategy-pmm → ad-copy-generator → landing-page-copywriter → email-template-generator
- **ABM活动**: lead-research-assistant → buyer-persona-generator → ad-copy-generator → linkedin-post-optimizer
- **SEO活动**: keyword-cluster-builder → serp-analysis → content-brief → content-optimizer
- **付费广告优化**: competitive-ads-extractor → ad-copy-generator → utm-builder → analytics-interpretation
- **品牌认知**: marketing-strategy-pmm → ad-copy-generator → social-repurposer → social-media-analyzer

## 输出标准

- **定位**: April Dunford框架、竞品替代方案映射
- **画像**: 完整人口统计、心理特征、行为特征
- **广告文案**: 平台特定格式、字符限制验证、5+变体
- **UTM链接**: 一致命名规范、表格文档记录
- **邮件**: 3-5封序列、渐进式互动、清晰CTA
- **报告**: 可执行洞察与具体建议

## 多AI工具支持

本workflow支持：
- Claude Code (`.claude/skills/`)
- Codex (`.codex/skills/`)
- Cursor (`.cursor/skills/`)
- OpenCode (`.opencode/skill/`)

## License

MIT
