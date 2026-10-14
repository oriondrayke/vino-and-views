# Vino & Views

Free wallet and API reports, direct USDC payment links, and a small capped escrow pilot.

[Try the tools](https://vinoandviews.online/?utm_source=github&utm_medium=organic&utm_campaign=public-launch) · [Create a payment request](https://vinoandviews.online/payments/?utm_source=github&utm_medium=organic&utm_campaign=public-launch) · [Explore escrow](https://vinoandviews.online/escrow/?utm_source=github&utm_medium=organic&utm_campaign=public-launch)

This repository contains public integration examples. It does not contain the production application or wallet keys.

## Get a free report in one command

Python 3, standard library only. No API key, wallet connection, or payment required:

```sh
python3 examples/free_agent.py
```

The example checks a hypothetical $1 spend against a $2 budget on Base using a public placeholder address. It reads a report and never signs or sends a transaction. Reports provide evidence and limitations, not a guarantee that a transaction or project is safe.

```sh
curl --fail-with-body https://api.vinoandviews.online/v1/agent-budget-guard \
  -H 'Content-Type: application/json' \
  -d '{"chain":"base","target":"0x0000000000000000000000000000000000000001","spend_usd":"1","max_spend_usd":"2"}'
```

## Connect an MCP client

For clients supporting remote Streamable HTTP, configure the following server. Configuration placement varies by client. No Authorization header is required for free report tools.

```json
{"mcpServers":{"vino-and-views":{"url":"https://api.vinoandviews.online/mcp/"}}}
```

The MCP listing describes discovery and tool access. Payment and escrow transfers require separate wallet signatures.

## Choose a tool

| Tool | Use it to investigate |
| --- | --- |
| `claim-worth-it` | Whether a supported claim warrants further investigation |
| `collectible-quote` | Available evidence for a supported collectible quote |
| `launchpad-fee-audit` | Supported launchpad fee evidence |
| `agent-budget-guard` | A proposed spend against a budget |
| `tx-preflight` | Transaction inputs before signing |
| `x402-health-check` | An x402 endpoint's payment challenge behavior |
| `launch-economics` | Launch economics under supplied assumptions |
| `allowance-risk-check` | Token allowance evidence for an owner and spender |
| `dependency-report` | Evidence about an API dependency |

All nine report endpoints are free. See [request examples](examples/service-examples.json) for supported input shapes. Chain and platform support varies by tool; the payment networks below do not imply every report supports every network. A wallet snapshot is also available through the website. Optional donations support the service and do not unlock paid tiers.

## Request USDC payments

Create a payment link for native USDC on Base, Polygon, Arbitrum, or Ethereum, then share it with the payer. Vino & Views charges no service fee for direct payments; network gas still applies. Direct payment links have no escrow protection. Verify the network, recipient and amount before signing.

[Payment policy](https://vinoandviews.online/payments/policy.html)

## Try escrow with a tiny pilot

The escrow workflow supports wallet login, agreement by both parties before funding, private text evidence, and wallet-signed settlement actions on Base, Polygon, Arbitrum and Ethereum.

Current pilot limits: **1 USDC per case and 3 USDC outstanding per deployed contract**. The fee is **0.5% of the receiver award**, plus network gas. Contracts have **not been independently audited**. This is a limited pilot, not a high-value custody service.

Disputes use a 12-hour evidence window followed by a 12-hour judgement window. If judgement is missed, a timeout transaction is required to return the full amount to the sender; funds do not move automatically. There is no committed 24/7 response SLA. Review the live terms and transaction preview before funding.

## Share useful feedback

Open an issue with the tool name, network, expected result, and a redacted error. Do not post wallet keys, access tokens, private dispute evidence, or personal information. Public issues are suitable for integration feedback, not private dispute resolution.

Published for the 0.7.1 release. Live terms and availability may change; check the website before transacting.
