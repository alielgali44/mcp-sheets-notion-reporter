# MCP Sheets & Notion Reporter (+ Slack / WhatsApp alerts)

An **MCP** server that turns a spreadsheet into quick daily summaries and team pings.
- Append a sale to **Google Sheets**
- Generate a short summary (demo)
- Post to **Slack** (demo)
- Optional: send **WhatsApp Cloud API** **template** message (transactional only)

MCP (“USB-C for AI”) lets assistants use standard tools; this server exposes simple **tools** the client can call.  
- MCP: https://modelcontextprotocol.io  
- Connect local servers: https://modelcontextprotocol.io/docs/develop/connect-local-servers

## Quick start
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python src/server.py
