# 数据源配置

## LongPort 与 AkShare 集成

- **LongPort**：分组、行情数据（优先使用）
  - 环境变量：`LONGPORT_APP_KEY`, `LONGPORT_APP_SECRET`, `LONGPORT_ACCESS_TOKEN`
  - 支持多个交易所：港股（.HK）、美股（.US）、A股（.SZ/.SH）
  - 返回字段：symbol, timestamp, open, high, low, close, volume

- **AkShare**：行情补齐（LongPort 缺失时回退）
  - 免费数据源，无需凭证
  - 注意字段对齐和时区统一

## 数据处理要点

- 统一使用前复权
- 统一时区处理（建议转换为 UTC）
- 缺失值先补齐，再进行指标计算
