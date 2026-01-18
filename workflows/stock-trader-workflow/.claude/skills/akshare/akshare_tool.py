#!/usr/bin/env python3
"""
Akshare 财经数据工具 - 为 AI 模型提供便捷的中国金融市场数据查询功能
使用方法: python akshare_tool.py --code 000001
"""

import argparse
import sys
from datetime import datetime
import akshare as ak
import pandas as pd

class AkshareTool:
    """Akshare 数据工具封装类"""
    
    def __init__(self):
        """初始化 Akshare 工具"""
        pass
    
    def get_stock_realtime(self, symbol: str, symbol_type: str = "stock") -> str:
        """
        获取股票/指数实时行情
        
        Args:
            symbol: 股票代码（如 000001, 600000）或指数代码（如 000001）
            symbol_type: 类型，stock（股票）或 index（指数）
        """
        try:
            if symbol_type == "index":
                # 获取指数实时行情
                df = ak.stock_zh_index_spot_em()
                data = df[df['代码'] == symbol]
            else:
                # 获取股票实时行情
                df = ak.stock_zh_a_spot_em()
                data = df[df['代码'] == symbol]
            
            if data.empty:
                return f"未找到代码 {symbol} 的数据，请检查代码是否正确。"
            
            row = data.iloc[0]
            
            # 构建输出
            output = [f"## {row['名称']} ({row['代码']}) 实时行情\n"]
            output.append(f"| 项目 | 数值 |")
            output.append(f"|------|------|")
            output.append(f"| 最新价 | {row['最新价']} |")
            output.append(f"| 涨跌幅 | {row['涨跌幅']}% |")
            output.append(f"| 涨跌额 | {row['涨跌额']} |")
            output.append(f"| 今开 | {row['今开']} |")
            output.append(f"| 昨收 | {row['昨收']} |")
            output.append(f"| 最高 | {row['最高']} |")
            output.append(f"| 最低 | {row['最低']} |")
            output.append(f"| 成交量 | {row['成交量']} |")
            output.append(f"| 成交额 | {row['成交额']} |")
            output.append(f"| 振幅 | {row['振幅']}% |")
            output.append(f"| 换手率 | {row['换手率']}% |")
            output.append(f"| 市盈率-动态 | {row['市盈率-动态']} |")
            output.append(f"| 市净率 | {row['市净率']} |")
            
            return "\n".join(output)
            
        except Exception as e:
            return f"获取数据出错: {str(e)}"
    
    def get_stock_history(self, symbol: str, period: str = "daily", 
                         start_date: str = None, end_date: str = None) -> str:
        """
        获取股票/指数历史K线数据
        
        Args:
            symbol: 股票代码或指数代码
            period: 周期（daily=日线, weekly=周线, monthly=月线）
            start_date: 开始日期，格式 YYYYMMDD
            end_date: 结束日期，格式 YYYYMMDD
        """
        try:
            # 设置默认日期
            if not end_date:
                end_date = datetime.now().strftime("%Y%m%d")
            
            # 根据周期选择接口
            if period == "daily":
                df = ak.stock_zh_a_hist(symbol=symbol, period="daily", 
                                        start_date=start_date, end_date=end_date, adjust="")
            elif period == "weekly":
                df = ak.stock_zh_a_hist(symbol=symbol, period="weekly", 
                                        start_date=start_date, end_date=end_date, adjust="")
            elif period == "monthly":
                df = ak.stock_zh_a_hist(symbol=symbol, period="monthly", 
                                        start_date=start_date, end_date=end_date, adjust="")
            else:
                return f"不支持的周期: {period}"
            
            if df.empty:
                return f"未找到代码 {symbol} 的历史数据。"
            
            # 只显示最近的10条记录
            df = df.tail(10)
            
            # 格式化输出
            output = [f"## {symbol} 历史{period}K线数据\n"]
            output.append(f"查询时间范围: {start_date} 至 {end_date}\n")
            output.append("| 日期 | 开盘 | 收盘 | 最高 | 最低 | 成交量 |")
            output.append("|------|------|------|------|------|--------|")
            
            for _, row in df.iterrows():
                output.append(f"| {row['日期']} | {row['开盘']} | {row['收盘']} | "
                            f"{row['最高']} | {row['最低']} | {row['成交量']} |")
            
            return "\n".join(output)
            
        except Exception as e:
            return f"获取历史数据出错: {str(e)}"
    
    def get_index_overview(self) -> str:
        """获取 A股主要指数概览"""
        try:
            df = ak.stock_zh_index_spot_em()
            
            # 筛选主要指数
            major_indices = {
                '000001': '上证指数',
                '399001': '深证成指',
                '399006': '创业板指',
                '000300': '沪深300',
                '000905': '中证500',
                '000016': '上证50'
            }
            
            output = ["## A股主要指数实时行情\n"]
            output.append("| 指数名称 | 代码 | 最新价 | 涨跌幅 | 涨跌额 | 成交量 |")
            output.append("|----------|------|--------|--------|--------|--------|")
            
            for code, name in major_indices.items():
                idx_data = df[df['代码'] == code]
                if not idx_data.empty:
                    row = idx_data.iloc[0]
                    output.append(f"| {name} | {code} | {row['最新价']} | "
                                f"{row['涨跌幅']}% | {row['涨跌额']} | {row['成交量']} |")
                else:
                    output.append(f"| {name} | {code} | N/A | N/A | N/A | N/A |")
            
            return "\n".join(output)
            
        except Exception as e:
            return f"获取指数概览出错: {str(e)}"
    
    def get_sector_top(self, limit: int = 10) -> str:
        """获取热门板块排行"""
        try:
            # 获取行业板块数据
            df_sector = ak.stock_board_industry_name_em()
            # 获取概念板块数据
            df_concept = ak.stock_board_concept_name_em()
            
            # 按涨跌幅排序，取前N个
            df_sector_top = df_sector.sort_values('涨跌幅', ascending=False).head(limit)
            df_concept_top = df_concept.sort_values('涨跌幅', ascending=False).head(limit)
            
            output = ["## 热门板块排行\n"]
            
            # 行业板块
            output.append(f"\n### 🏭 行业板块 TOP {limit}")
            output.append("| 板块名称 | 最新价 | 涨跌幅 | 总市值 |")
            output.append("|----------|--------|--------|--------|")
            for _, row in df_sector_top.iterrows():
                output.append(f"| {row['板块名称']} | {row['最新价']} | "
                            f"{row['涨跌幅']}% | {row['总市值']} |")
            
            # 概念板块
            output.append(f"\n### 💡 概念板块 TOP {limit}")
            output.append("| 板块名称 | 最新价 | 涨跌幅 | 总市值 |")
            output.append("|----------|--------|--------|--------|")
            for _, row in df_concept_top.iterrows():
                output.append(f"| {row['板块名称']} | {row['最新价']} | "
                            f"{row['涨跌幅']}% | {row['总市值']} |")
            
            return "\n".join(output)
            
        except Exception as e:
            return f"获取板块数据出错: {str(e)}"
    
    def get_stock_info(self, symbol: str) -> str:
        """获取股票基本信息"""
        try:
            # 获取个股资料
            df = ak.stock_individual_info_em(symbol=symbol)
            
            output = [f"## {symbol} 股票基本信息\n"]
            output.append("| 项目 | 内容 |")
            output.append("|------|------|")
            
            for _, row in df.iterrows():
                output.append(f"| {row['item']} | {row['value']} |")
            
            return "\n".join(output)
            
        except Exception as e:
            return f"获取股票信息出错: {str(e)}"
    
    def get_financial_data(self, symbol: str) -> str:
        """获取财务数据（财务指标）"""
        try:
            # 获取财务指标
            df = ak.stock_financial_analysis_indicator(symbol=symbol)
            
            if df.empty:
                return f"未找到代码 {symbol} 的财务数据。"
            
            # 只显示最近4个季度
            df = df.head(4)
            
            output = [f"## {symbol} 财务指标\n"]
            output.append("| 日期 | 净利润 | 营业收入 | 净资产收益率(%) | 毛利率(%) | 资产负债率(%) |")
            output.append("|------|--------|----------|----------------|----------|----------------|")
            
            for _, row in df.iterrows():
                output.append(f"| {row['日期']} | {row['净利润']} | {row['营业收入']} | "
                            f"{row['净资产收益率']} | {row['毛利率']} | {row['资产负债率']} |")
            
            return "\n".join(output)
            
        except Exception as e:
            return f"获取财务数据出错: {str(e)}"


def main():
    """命令行接口"""
    parser = argparse.ArgumentParser(
        description="Akshare 财经数据工具 - 中国金融市场数据查询",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用示例:
  查询股票实时行情:
    python akshare_tool.py --code 000001
  
  查询指数实时行情:
    python akshare_tool.py --code 000001 --type index
  
  查询历史数据:
    python akshare_tool.py --code 000001 --mode history --start 20250101
  
  查看指数概览:
    python akshare_tool.py --mode index-overview
  
  查看热门板块:
    python akshare_tool.py --mode sector-top
  
  查询股票信息:
    python akshare_tool.py --code 000001 --mode info
  
  查询财务数据:
    python akshare_tool.py --code 000001 --mode financial
        """
    )
    
    parser.add_argument("--code", "-c", help="股票/指数代码")
    parser.add_argument("--type", "-t", choices=["stock", "index"], 
                       default="stock", help="代码类型")
    parser.add_argument("--mode", "-m", 
                       choices=["realtime", "history", "index-overview", "sector-top", "info", "financial"],
                       default="realtime", help="查询模式")
    parser.add_argument("--period", "-p", choices=["daily", "weekly", "monthly"],
                       default="daily", help="K线周期")
    parser.add_argument("--start", help="开始日期 (YYYYMMDD)")
    parser.add_argument("--end", help="结束日期 (YYYYMMDD)")
    
    args = parser.parse_args()
    
    try:
        # 创建工具实例
        tool = AkshareTool()
        
        # 根据模式执行查询
        if args.mode == "realtime":
            if not args.code:
                print("错误: 实时行情模式需要指定 --code 参数")
                sys.exit(1)
            print(tool.get_stock_realtime(args.code, args.type))
            
        elif args.mode == "history":
            if not args.code:
                print("错误: 历史数据模式需要指定 --code 参数")
                sys.exit(1)
            print(tool.get_stock_history(args.code, args.period, args.start, args.end))
            
        elif args.mode == "index-overview":
            print(tool.get_index_overview())
            
        elif args.mode == "sector-top":
            print(tool.get_sector_top())
            
        elif args.mode == "info":
            if not args.code:
                print("错误: 股票信息模式需要指定 --code 参数")
                sys.exit(1)
            print(tool.get_stock_info(args.code))
            
        elif args.mode == "financial":
            if not args.code:
                print("错误: 财务数据模式需要指定 --code 参数")
                sys.exit(1)
            print(tool.get_financial_data(args.code))
            
    except Exception as e:
        print(f"发生错误: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
