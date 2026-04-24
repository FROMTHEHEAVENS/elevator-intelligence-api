# Elevator Intelligence API

Pay-per-call structured intelligence dossiers on major elevator OEMs and supply-chain companies.

**11 dossiers live.** USDC payments on your choice of chain. No account. No KYC.

## Live API — 3 Payment Rails

| Chain | URL | USDC Source |
|---|---|---|
| **Polygon PoS** (chain 137) | https://skins-mercy-punk-ladies.trycloudflare.com | Coinbase/Binance/Kraken → withdraw to Polygon |
| **Base L2** (chain 8453) | https://strike-cornell-handed-corpus.trycloudflare.com | Coinbase native or bridge.base.org |
| **HyperEVM** (chain 998) | https://dealer-functionality-vip-porter.trycloudflare.com | Hyperliquid exchange |

> Note: ephemeral cloudflared hostnames. Check [Gist](https://gist.github.com/FROMTHEHEAVENS/5f2a559503942f1b440ec2c59798e73e) for updated URLs.
>
> **Recommended for first-time buyers:** Polygon — USDC available via direct CEX withdrawal, gas ~$0.001.

---

## Dossier Catalog

### OEM Platforms

| Slug | Vendor | Price | Coverage |
|---|---|---|---|
| `schindler` | Schindler Group | **$1.00** | PORT Technology binary TCP protocol (telegram schemas, error codes), Azure B2C auth |
| `kone` | KONE Corporation | **$2.00** | AsyncAPI v1 spec (elevator-call), OAuth2 + WebSocket, full message schema, building ID format |
| `otis` | Otis Elevator Company | **$3.00** | OID Socket.IO API (68 modes, 30 car + 32 group commands), Keycloak auth, Azure APIM, K8s internals |
| `tke` | TK Elevator (ThyssenKrupp) | **$4.00** | MAX platform 8-API surface, Azure B2C OAuth2 ROPC client ID, APIM portal |
| `hyundai` | Hyundai Elevator | **$3.50** | MIRI open API (public dev portal), OAuth2, 60+ integrations, SAP HANA backend |
| `melco` | Mitsubishi Electric | **$2.50** | READY CONNECT gateway, M's BRIDGE IoT SaaS (AWS), Modbus TCP, OpenAM cert auth |
| `hitachi` | Hitachi Building Systems | **$2.00** | HERIOS 600-pt IoT backend, BuilMirai Azure, FIBEE AI dispatch, LINE touchless. Post-TKE merger coverage. |

### Supplier Intelligence

| Slug | Vendor | Price | Coverage |
|---|---|---|---|
| `dewhurst` | Dewhurst Group (AIM: DWHT) | **$3.00** | **Cross-OEM installed-base map**: 20+ landmark buildings mapped to elevator OEM — Heathrow→KONE, Claridges→Schindler, Maybourne Riviera→Otis, Elizabeth Line, The Shard, Tottenham Hotspur FC, TfL, Sofitel Sydney, Royal Perth Hospital... Full US-series pushbutton product line. 22-host fleet. |
| `fermator` | Fermator Group | **$2.00** | Global door market leader — 19 products, 9-entity subsidiary network (IT/ES/BR/IN/FR/UK), ISO internal codes (11 codes, 2 undisclosed entities), Iraq exclusive distribution |
| `songsan` | Songsan Special Elevators (KR) | **$2.00** | Explosion-proof, clean-room (NovaClean), rescue (X-vator), industrial Goliath + **UAM/vertiport positioning** (5 solution types for eVTOL ground infrastructure) |
| `koelsa` | Korea Elevator Safety Agency | **$1.50** | National regulatory API, civil petition portal, 2017-2018 fleet stats by province, 346-entry KR manufacturer registry |

**Bundle: all 11 for $26.50** → `GET /v1/bundle`

---

## API Reference

### Free endpoints

```bash
# Service index + pricing
GET /

# Dossier catalog
GET /v1/dossiers

# Free preview (description, keys — no payment)
GET /v1/dossiers/{slug}/preview
```

### Paid endpoints

```bash
# Single dossier
GET /v1/dossiers/{slug}

# Bundle — all 11 in one payment
GET /v1/bundle
```

---

## Payment Flow

1. **Request dossier:**
   ```bash
   curl https://skins-mercy-punk-ladies.trycloudflare.com/v1/dossiers/kone
   ```
   Response: `HTTP 402` with payment details:
   ```json
   {
     "rail": "polygon_pos_usdc",
     "chain_id": 137,
     "recipient": "0x3c3706...",
     "usdc_contract": "0x3c499c542cEF5E3811e1192ce70d8cC03d5c3359",
     "amount_usdc": 2000000,
     "amount_human": "$2.00"
   }
   ```

2. **Send native USDC on Polygon** to the recipient address.

3. **Retry with tx hash:**
   ```bash
   curl -H "X-Payment-TxHash: 0xYOUR_TX_HASH" \
     https://skins-mercy-punk-ladies.trycloudflare.com/v1/dossiers/kone
   ```

**Server verifies on-chain:** recipient match, amount ≥ price, ≥1 confirmation.

---

## OpenAPI Spec

Available at: `https://raw.githubusercontent.com/FROMTHEHEAVENS/elevator-intelligence-api/main/openapi.json`

Interactive docs: `{base_url}/docs`

---

## Who is this for?

- **Building automation engineers** integrating elevator dispatch into BMS/SCADA
- **Smart building startups** building on KONE, Otis, TKE APIs
- **Elevator modernization contractors** scoping OEM-specific integrations
- **Robotics companies** implementing autonomous elevator dispatch
- **OT/ICS security researchers** mapping vertical transport infrastructure
- **Facilities management platforms** aggregating multi-vendor building data
- **eVTOL/UAM infrastructure teams** — Songsan dossier covers vertiport elevator systems
