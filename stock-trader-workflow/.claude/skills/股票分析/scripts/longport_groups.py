"""LongPort 自选分组命令行管理工具，支持分组的增删改查及成员批量导出。

Main Functions:
  - list_groups: 列出所有分组
  - create_group: 创建新分组
  - update_group: 更新分组成员（增/删/替换）
  - get_symbols: 导出分组成员列表
  - delete_group: 清空分组

Usage:
  python scripts/longport_groups.py list
  python scripts/longport_groups.py create --name my_group --symbols 700.HK,AAPL.US
  python scripts/longport_groups.py update --id 1 --add-symbols 000001.SZ
  python scripts/longport_groups.py get-symbols --id 1
  python scripts/longport_groups.py delete --id 1
"""

import argparse
from contextlib import contextmanager
from typing import Iterator

from longport.openapi import Config, QuoteContext, SecuritiesUpdateMode


@contextmanager
def open_quote_ctx() -> Iterator[QuoteContext]:
    """从 .env 初始化 QuoteContext，用完自动关闭。"""
    ctx = QuoteContext(Config.from_env())
    try:
        yield ctx
    finally:
        close_fn = getattr(ctx, "close", None)
        if callable(close_fn):
            close_fn()


def list_groups(args) -> None:
    """列出所有分组。"""
    with open_quote_ctx() as ctx:
        groups = ctx.watchlist()
        if not groups:
            print("无分组")
            return
        print(f"{'ID':<8} {'Name':<30} {'Count':<10}")
        print("-" * 50)
        for g in groups:
            name = g.name[:28] if len(g.name) > 28 else g.name
            print(f"{g.id:<8} {name:<30} {len(g.securities):<10}")


def create_group(args) -> None:
    """创建分组。"""
    symbols = None
    if args.symbols:
        symbols = [s.strip() for s in args.symbols.split(",") if s.strip()]
    with open_quote_ctx() as ctx:
        group_id = ctx.create_watchlist_group(name=args.name, securities=symbols)
    print(
        f"✓ 分组已创建: ID={group_id}, Name={args.name}, Count={len(symbols) if symbols else 0}"
    )


def update_group(args) -> None:
    """更新分组（增/删/替换成员）。"""
    mode = SecuritiesUpdateMode.Add
    if args.remove_symbols:
        mode = SecuritiesUpdateMode.Remove
    elif args.replace_symbols:
        mode = SecuritiesUpdateMode.Replace

    symbols = None
    if args.add_symbols:
        symbols = [s.strip() for s in args.add_symbols.split(",") if s.strip()]
    elif args.remove_symbols:
        symbols = [s.strip() for s in args.remove_symbols.split(",") if s.strip()]
    elif args.replace_symbols:
        symbols = [s.strip() for s in args.replace_symbols.split(",") if s.strip()]

    if symbols is None:
        print("错误: 需要 --add-symbols 或 --remove-symbols 或 --replace-symbols")
        return

    with open_quote_ctx() as ctx:
        ctx.update_watchlist_group(args.id, securities=symbols, mode=mode)
        groups = ctx.watchlist()
        updated = next((g for g in groups if g.id == args.id), None)
        if updated is None:
            print(f"✗ 错误: 分组不存在 (ID={args.id})")
            return
        print(
            f"✓ 分组已更新: ID={args.id}, Name={updated.name}, Count={len(updated.securities)}"
        )


def get_symbols(args) -> None:
    """导出分组成员列表。"""
    with open_quote_ctx() as ctx:
        groups = ctx.watchlist()
        group = next((g for g in groups if g.id == args.id), None)
        if group is None:
            print(f"✗ 错误: 分组不存在 (ID={args.id})")
            return
        symbols = [s.symbol for s in group.securities]

    if not symbols:
        print("分组为空")
        return
    if args.output:
        with open(args.output, "w") as f:
            f.write("\n".join(symbols))
        print(f"✓ 已写入: {args.output}")
    else:
        print("\n".join(symbols))


def delete_group(args) -> None:
    """清空分组（替换为空列表）。"""
    with open_quote_ctx() as ctx:
        groups = ctx.watchlist()
        group = next((g for g in groups if g.id == args.id), None)
        if group is None:
            print(f"✗ 错误: 分组不存在 (ID={args.id})")
            return
        ctx.update_watchlist_group(
            args.id, securities=[], mode=SecuritiesUpdateMode.Replace
        )
        print(f"✓ 分组已清空: ID={args.id}")


def main() -> None:
    parser = argparse.ArgumentParser(description="LongPort 自选分组管理")
    subparsers = parser.add_subparsers(dest="command", help="子命令")

    # list
    subparsers.add_parser("list", help="列出所有分组")

    # create
    create_p = subparsers.add_parser("create", help="创建分组")
    create_p.add_argument("--name", required=True, help="分组名")
    create_p.add_argument("--symbols", help="初始成员，逗号分隔，如 700.HK,AAPL.US")

    # update
    update_p = subparsers.add_parser("update", help="更新分组成员")
    update_p.add_argument("--id", type=int, required=True, help="分组 ID")
    update_p.add_argument("--add-symbols", help="增加成员，逗号分隔")
    update_p.add_argument("--remove-symbols", help="删除成员，逗号分隔")
    update_p.add_argument("--replace-symbols", help="替换全部成员，逗号分隔")

    # get-symbols
    get_p = subparsers.add_parser("get-symbols", help="导出分组成员")
    get_p.add_argument("--id", type=int, required=True, help="分组 ID")
    get_p.add_argument(
        "--output", help="输出文件路径（逐行一个符号）；不填则打印到 stdout"
    )

    # delete
    delete_p = subparsers.add_parser("delete", help="清空分组")
    delete_p.add_argument("--id", type=int, required=True, help="分组 ID")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    try:
        if args.command == "list":
            list_groups(args)
        elif args.command == "create":
            create_group(args)
        elif args.command == "update":
            update_group(args)
        elif args.command == "get-symbols":
            get_symbols(args)
        elif args.command == "delete":
            delete_group(args)
    except Exception as e:
        print(f"✗ 错误: {e}")
        exit(1)


if __name__ == "__main__":
    main()
