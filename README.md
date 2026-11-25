# Internal Systems Gateway

Internal access gateway for autonomous agents. Exposes a small set of
internal tools over the Model Context Protocol (JSON-RPC 2.0) so that
agent runtimes can call them through a single, authenticated endpoint.

## What it is

A lightweight gateway service that sits in front of a few internal
utilities (text tools, data lookups, job runners) and presents them as
MCP tools. Agents connect via HTTP POST and speak standard JSON-RPC.

## Endpoint

```
POST https://mcp-gateway.co.uk/mcp
Content-Type: application/json
```

## Quick start

```python
import json
import urllib.request

payload = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/list",
    "params": {},
}
req = urllib.request.Request(
    "https://mcp-gateway.co.uk/mcp",
    data=json.dumps(payload).encode(),
    headers={"Content-Type": "application/json"},
)
print(urllib.request.urlopen(req).read().decode())
```

See `examples/` for a fuller client with authentication.

## Configuration

Copy `.env.example` to `.env` and set your gateway URL and bearer token.
Schema details are in `config/gateway.yaml` and `endpoints.json`.

## Status

Personal / internal project. Not affiliated with any third-party
service. Do not point it at systems you don't own.
