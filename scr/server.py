#!/usr/bin/env python3
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("SheetsNotionReporter")

@mcp.tool()
def append_sale(item: str, qty: int, price: float) -> dict:
    """Demo: compute line total (later: append to Google Sheets)."""
    return {"item": item, "qty": qty, "price": price, "total": qty * price, "status": "stub"}

@mcp.tool()
def post_slack(channel: str, text: str) -> str:
    """Demo: pretend to post to Slack (later: chat.postMessage)."""
    return f"[stub] Would post to {channel or '#general'}: {text}"

if __name__ == "__main__":
    print("MCP server stub is alive. Wire Sheets/Slack next.")