# Elevator Intelligence API

Pay-per-call structured intelligence dossiers on major elevator OEMs and supply-chain companies.

**14 dossiers live.** USDC payments on 3 chains. No account. No KYC.

## Live API — 3 Payment Rails

| Chain | URL | USDC Source |
|---|---|---|
| **HyperEVM** (chain 998) | https://dealer-functionality-vip-porter.trycloudflare.com | Hyperliquid exchange |
| **Base L2** (chain 8453) | https://strike-cornell-handed-corpus.trycloudflare.com | Coinbase native or bridge.base.org |
| **Polygon PoS** (chain 137) | https://skins-mercy-punk-ladies.trycloudflare.com | Coinbase/Binance/Kraken → withdraw to Polygon |

> **Note:** ephemeral cloudflared hostnames. If a URL is down, check the [Gist](https://gist.github.com/FROMTHEHEAVENS/5f2a559503942f1b440ec2c59798e73e) for updated URLs.
>
> **Recommended for first-time buyers:** Polygon — native USDC from any CEX withdrawal, gas < $0.001.

---

## Dossier Catalog ($36 bundle, all 14)

### Flagship OEM Platforms

| Slug | Vendor | Price | Highlights |
|---|---|---|---|
| `schindler` | Schindler Group | **$3.00** | CoLab API (82 ops, physical elevator commands), ActionBoard (8 endpoints), PORT Technology binary TCP protocol, Azure B2C tenant 08932c55, real equipment IDs confirmed live |
| `kone` | KONE Corporation | **$3.00** | AsyncAPI v1 spec (elevator-call), Cognito pool eu-west-1_Vxl193uuj, myKONE IDOR paths, Salesforce Full sandbox, RemoteCall APK |
| `otis` | Otis Elevator Company | **$4.00** | BMS REST v1.6.0 (18 endpoints, physical dispatch), OID Socket.IO (68 modes, 62 commands), IDOR targets, Keycloak DCR |
| `tke` | TK Elevator | **$4.00** | 8-API MAX platform, ROPC client ID 74c72ab2, Azure B2C, APIM portal |
| `hyundai` | Hyundai Elevator | **$3.50** | MIRI public developer portal, OAuth2 client_credentials, 60+ integrations, SAP HANA backend |
| `melco` | Mitsubishi Electric | **$2.50** | Darwin platform (Tomcat + OpenAM), M's BRIDGE IoT SaaS, Modbus TCP G-50 controllers, Serendie platform |
| `hitachi` | Hitachi Building Systems | **$2.00** | HERIOS 600-point IoT backend (1994), BuilMirai Azure (2024), LINE touchless API, TKE ROPC covers 1M+ elevators post-merger |

### Supplier & Component Intelligence

| Slug | Vendor | Price | Highlights |
|---|---|---|---|
| `dewhurst` | Dewhurst Group (AIM:DWHT) | **$3.00** | 20+ landmark buildings mapped to OEM: Heathrow/KONE, Claridges/Schindler, Elizabeth Line, The Shard, Tottenham Hotspur, Sofitel Sydney |
| `fermator` | Fermator Group | **$2.00** | 19-product door catalog, 9-entity subsidiary network (IT/ES/BR/IN/FR/UK), Iraq exclusive distribution |
| `songsan` | Songsan Special Elevators | **$2.00** | Explosion-proof, clean-room, rescue + UAM/vertiport product line (5 eVTOL solution types — unique in catalog) |
| `buildingminds` | BuildingMinds (Schindler+KONE JV) | **$2.50** | MCP server at mcp.onbuildingminds.com, 93-subdomain architecture, ArgoCD+Airflow, Azure B2C |
| `kleemann` | Kleemann Group (GR) | **$1.50** | Keycloak admin console exposed, realm '3s' public RSA key, 70+ country distribution network |
| `haushahn` | Haushahn GmbH (DE) | **$1.50** | TYPO3 install.php exposed, 3 unauthenticated eID endpoints, 40k+ units (Germany's oldest independent servicer) |
| `koelsa` | Korea Elevator Safety Agency | **$1.50** | National regulatory API, civil petition portal, fleet stats by province (14 types × 17 provinces) |

**Bundle: all 14 for $36.00** → `GET /v1/bundle` (or `?bundle=1`)

---

## API Reference

### Free endpoints

```bash
# Service index + pricing
curl https://dealer-functionality-vip-porter.trycloudflare.com/

# Dossier catalog with descriptions
curl https://dealer-functionality-vip-porter.trycloudflare.com/v1/dossiers

# Free preview — real intelligence teasers, no payment
curl https://dealer-functionality-vip-porter.trycloudflare.com/v1/dossiers/schindler/preview
```

### Pay-per-call (HyperEVM example)

```bash
# 1. Get payment info
curl https://dealer-functionality-vip-porter.trycloudflare.com/

# 2. Send USDC on HyperEVM (chain 998) to recipient address shown in /payment
# 3. Retry with tx hash header
curl https://dealer-functionality-vip-porter.trycloudflare.com/v1/dossiers/schindler \
  -H "X-Payment-TxHash: 0xYOURTXHASH"
```

### Python client

```python
import requests

BASE_URL = "https://dealer-functionality-vip-porter.trycloudflare.com"

# List dossiers
catalog = requests.get(f"{BASE_URL}/v1/dossiers").json()
for d in catalog["dossiers"]:
    print(f"{d['slug']}: {d['price']} — {d['description'][:80]}...")

# Free preview
preview = requests.get(f"{BASE_URL}/v1/dossiers/otis/preview").json()
print(preview["intelligence_teasers"])

# Pay and fetch (after sending USDC on-chain)
tx_hash = "0x..."  # your on-chain tx
resp = requests.get(
    f"{BASE_URL}/v1/dossiers/otis",
    headers={"X-Payment-TxHash": tx_hash}
)
dossier = resp.json()
```

Full Python demo: [api_client_demo.py](https://gist.github.com/FROMTHEHEAVENS/5f2a559503942f1b440ec2c59798e73e)

---

## Use Cases

- **Building automation integrators** — need to understand OEM API surfaces before committing to an integration project
- **Security researchers** — elevator OEM attack surface mapping, IoT/BACnet exposure assessment
- **Facility managers** — understand what data your elevator OEM is collecting and what APIs expose it
- **M&A / due diligence** — digital infrastructure assessment for elevator company acquisitions
- **Smart building developers** — know which OEMs have open APIs and what auth flows they use

---

## OpenAPI Spec

Interactive docs at `/docs` (FastAPI auto-generated Swagger UI).

---

## Contact / Updates

- GitHub: [@FROMTHEHEAVENS](https://github.com/FROMTHEHEAVENS)
- New dossiers added weekly
- `[earner]` pilot on the GoodWillHunting fleet
