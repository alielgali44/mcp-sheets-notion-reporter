# MCP Sheets & Notion Reporter (Slack/WhatsApp alerts)

**What it is:** An MCP server that appends a sale to Google Sheets, recomputes KPIs, generates a short summary/PDF, and posts a team digest (Slack). Optional: send a WhatsApp Cloud API **template** message for order-ready notifications.

## Quick start
Create `.env` with:
- SHEETS_SPREADSHEET_ID, GOOGLE_APPLICATION_CREDENTIALS
- SLACK_BOT_TOKEN  (for chat.postMessage)
- NOTION_TOKEN (optional)
- WHATSAPP_TOKEN / PHONE_ID / TEMPLATE (transactional templates only)

## Example prompts
- “Add 2× S21 cases @ 45,000 UGX, recompute weekly KPIs, post Slack summary, send ‘order_ready’ template to +2567xxxxxxx.”

## Notes
- Slack messages via Web API. 
- WhatsApp **must** use approved **message templates** (no general chatbots).
