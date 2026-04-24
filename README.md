# Elevator Intelligence API

Pay-per-call structured intelligence dossiers on major elevator OEMs and supply-chain companies.

**10 dossiers live.** USDC payments on HyperEVM (chain 998). No account. No KYC.

## Live API

```
https://dealer-functionality-vip-porter.trycloudflare.com
```

> Note: ephemeral cloudflared hostname. Permanent deployment in progress. Check [Gist](https://gist.github.com/FROMTHEHEAVENS/5f2a559503942f1b440ec2c59798e73e) for updated URL.

---

## Dossier Catalog

### OEM Platforms

| Slug | Vendor | Price | Coverage |
|---|---|---|---|
| `schindler` | Schindler Group | **$1.00 USDC** | PORT Technology binary TCP protocol (dispatch/sync/record telegram schemas, error codes), Azure B2C auth flow, developer portal surface |
| `kone` | KONE Corporation | **$2.00 USDC** | Official AsyncAPI v1 spec (elevator-call API), OAuth2 + WebSocket architecture, full message schema, building ID format, 4-API surface map |
| `otis` | Otis Elevator Company | **$3.00 USDC** | OID Socket.IO dispatch API (68 operating modes, 30 car + 32 group commands), Keycloak auth (realm: ems), Azure APIM surface, K8s internals, zero rate-limiting design |
| `tke` | TK Elevator (ThyssenKrupp) | **$4.00 USDC** | MAX platform: 8 APIs (Equipment, IoT, Service, WOM, Touchless, Elevator Calls, Robot Call, Statistical), Azure B2C OAuth2 ROPC client ID, APIM portal, MAX Box IoT gateway |
| `hyundai` | Hyundai Elevator | **$3.50 USDC** | MIRI open developer API (developers.hyundaielevator.com), OAuth2 client credentials, 60+ active building integrations, robot dispatch (30+ buildings), SAP HANA backend, HELIAS destination dispatch |
| `melco` | Mitsubishi Electric (MELCO) | **$2.50 USDC** | READY CONNECT proprietary gateway, M's BRIDGE IoT SaaS (AWS + Maisart AI), EPS Portal (OpenAM certificate auth), Modbus TCP G-50 controllers, Serendie platform, AWS cloud migration in progress |
| `hitachi` | Hitachi Building Systems | **$2.00 USDC** | HERIOS 600-datapoint IoT backend (operational since 1994), BuilMirai Azure building IoT (2024), FIBEE AI dispatch (+50% capacity), EMIEW robot integration, LINE touchless mobile API. Post-TKE merger: ROPC client ID covers 1M+ elevators. |

### Supplier Intelligence

| Slug | Vendor | Price | Coverage |
|---|---|---|---|
| `dewhurst` | Dewhurst Group (AIM: DWHT) | **$3.00 USDC** | Cross-OEM installed-base map: 20+ landmark buildings mapped to elevator OEM — Heathrow Airport (KONE + Express), Claridges Hotel (Schindler), Maybourne Riviera (Otis), Bluewater Shopping Mall (Schindler), Elizabeth Line, The Shard, Tottenham Hotspur FC Stadium, Transport for London, Royal Perth Hospital + 11 more. Full US-series pushbutton product line (US1/US85/US95/US96-EN). 22-host subdomain fleet. Dupar/ALC/TVC/TMT subsidiary map. |
| `fermator` | Fermator Group | **$2.00 USDC** | Global elevator door systems market leader — full 19-product WooCommerce catalog (MOD MC, Platinum HR, 40/10 variants, 50/11 SLIM/MEGA), 9-entity global subsidiary network (Tecnidoors IT, Tecnolama ES, Tecnoamerica BR, Tecno Doors IN, Ets Henri Peignen FR, Global1Partners UK, INGECO IT), ISO quality system internal codes (11 codes, 2 undisclosed entities), Iraq exclusive distribution. |
| `koelsa` | Korea Elevator Safety Agency | **$1.50 USDC** | National regulatory intelligence: civil petition portal endpoints, 2017-2018 fleet statistics (14 elevator types × 17 provinces × 11 building categories), eGov stack fingerprint, GPKI admin surface, form templates. Also includes: 346-entry Korean national manufacturer/importer registry from eac.purpleo.kr. |

**Bundle: all 10 dossiers for $24.50** → `GET /v1/bundle`

---

## API Reference

### Free endpoints

```bash
# Service index + pricing
GET /

# Dossier catalog (all slugs + descriptions + prices)
GET /v1/dossiers

# Free preview (top-level keys, description, price — no payment)
GET /v1/dossiers/{slug}/preview
```

### Paid endpoints

```bash
# Single dossier — returns 402 + payment instructions if unpaid
GET /v1/dossiers/{slug}

# Bundle — all 10 dossiers in one payment
GET /v1/bundle
```

---

## Payment Flow (HyperEVM)

1. **Request dossier:**
   ```bash
   curl https://dealer-functionality-vip-porter.trycloudflare.com/v1/dossiers/kone
   ```
   Response: `HTTP 402` with payment details:
   ```json
   {
     "error": "Payment required",
     "price_usdc": 2000000,
     "price_human": "$2.00",
     "recipient": "0x3c3706...",
     "usdc_contract": "0x0d1257...",
     "chain_id": 998,
     "nonce": "0xabc123...",
     "expires_at": 1234567890
   }
   ```

2. **Send USDC on HyperEVM** (chain 998) to `recipient` — include `nonce` in tx calldata.

3. **Retry with tx hash:**
   ```bash
   curl -H "X-Payment-TxHash: 0xYOUR_TX_HASH" \
     https://dealer-functionality-vip-porter.trycloudflare.com/v1/dossiers/kone
   ```
   Response: full dossier JSON.

**Server verifies:** recipient matches, amount ≥ price, ≥1 confirmation, nonce not replayed.

---

## Python Client

```python
import httpx

API = "https://dealer-functionality-vip-porter.trycloudflare.com"

# List all dossiers
resp = httpx.get(f"{API}/v1/dossiers")
catalog = resp.json()

# Free preview
preview = httpx.get(f"{API}/v1/dossiers/dewhurst/preview").json()
print(preview["description"])

# After sending USDC on HyperEVM:
dossier = httpx.get(
    f"{API}/v1/dossiers/kone",
    headers={"X-Payment-TxHash": "0xYOUR_TX"}
).json()
```

Full demo: [api_client_demo.py in the Gist](https://gist.github.com/FROMTHEHEAVENS/5f2a559503942f1b440ec2c59798e73e)

---

## Who is this for?

- **Building automation engineers** integrating elevator dispatch into BMS/SCADA
- **Smart building startups** building on top of OEM platforms (KONE, Otis, TKE)
- **Elevator modernization contractors** scoping integration with existing installations
- **BAS consultants** researching which OEMs are installed in target buildings
- **Facilities management platforms** aggregating building system data
- **OT/ICS security researchers** studying vertical transport infrastructure attack surface
- **Robotics companies** integrating autonomous robot-elevator dispatch

---

## Interactive Docs

Swagger UI: `https://dealer-functionality-vip-porter.trycloudflare.com/docs`
