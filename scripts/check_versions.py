#!/usr/bin/env python3
"""检查三套插件清单的 name / version 是否一致。发布前运行：python3 scripts/check_versions.py"""
import json, pathlib, sys
root = pathlib.Path(__file__).resolve().parent.parent
files = {
    "Claude Code": root / "plugins/sanyi-manhua-writing/.claude-plugin/plugin.json",
    "Codex":       root / "plugins/sanyi-manhua-writing/.codex-plugin/plugin.json",
    "Kimi Code":   root / "kimi.plugin.json",
}
seen = {}
for tool, f in files.items():
    d = json.loads(f.read_text(encoding="utf-8"))
    seen[tool] = (d.get("name"), d.get("version"))
    print(f"{tool:12} {d.get('name')}  {d.get('version')}")
if len(set(seen.values())) != 1:
    print("\n✗ 版本或名称不一致，请把三个清单改成同一个值后再发布"); sys.exit(1)
print("\n✓ 三套清单一致")
