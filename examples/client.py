#!/usr/bin/env python3
"""Minimal JSON-RPC client for the internal systems gateway.

Usage:
    export GATEWAY_URL=https://mcp-gateway.co.uk/mcp
    export GATEWAY_BEARER_TOKEN=<redacted>   # your own token
    python3 examples/client.py tools/list
"""

import json
import os
import sys
import urllib.request

GATEWAY_URL = os.environ.get("GATEWAY_URL", "https://mcp-gateway.co.uk/mcp")
BEARER_TOKEN = os.environ.get("GATEWAY_BEARER_TOKEN", "")


def rpc_call(method: str, params: dict | None = None) -> dict:
    """POST a single JSON-RPC 2.0 message to the gateway."""
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": method,
        "params": params or {},
    }
    headers = {"Content-Type": "application/json"}
    if BEARER_TOKEN:
        headers["Authorization"] = f"Bearer {BEARER_TOKEN}"

    req = urllib.request.Request(GATEWAY_URL, data=json.dumps(payload).encode(), headers=headers)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode())


def main() -> int:
    method = sys.argv[1] if len(sys.argv) > 1 else "tools/list"
    try:
        result = rpc_call(method)
    except Exception as exc:  # connection errors, HTTP errors, bad JSON
        print(f"gateway call failed: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
