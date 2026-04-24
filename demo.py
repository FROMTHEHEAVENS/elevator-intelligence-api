"""
Elevator Intelligence API — Python client demo

Demonstrates the full pay-per-call flow using the HyperEVM USDC payment rail.

Requirements:
    pip install httpx web3

Usage:
    python api_client_demo.py

Workflow:
  1. GET /v1/dossiers/{slug}  →  receives 402 + payment instructions
  2. Send USDC transfer on HyperEVM chain (chain ID 998) to the recipient
  3. Retry GET with X-Payment-TxHash header
  4. Receive structured JSON dossier

Docs: https://dealer-functionality-vip-porter.trycloudflare.com/docs
"""

import sys
import httpx

API_BASE = "https://dealer-functionality-vip-porter.trycloudflare.com"
# Update this if the cloudflared URL changes; permanent URL pending fly.io deploy


def list_dossiers() -> None:
    r = httpx.get(f"{API_BASE}/v1/dossiers")
    r.raise_for_status()
    data = r.json()
    print("\nAvailable dossiers:")
    for d in data["dossiers"]:
        print(f"  {d['slug']:12s}  {d['price']:30s}  {d['tier']}")


def preview(slug: str) -> dict:
    r = httpx.get(f"{API_BASE}/v1/dossiers/{slug}/preview")
    r.raise_for_status()
    return r.json()


def request_payment_details(slug: str) -> dict:
    """Returns the 402 payment-required response body."""
    r = httpx.get(f"{API_BASE}/v1/dossiers/{slug}")
    if r.status_code != 402:
        raise ValueError(f"Expected 402, got {r.status_code}")
    return r.json()["detail"]


def pay_and_fetch(slug: str, tx_hash: str) -> dict:
    """Retry with the HyperEVM transaction hash after paying."""
    r = httpx.get(
        f"{API_BASE}/v1/dossiers/{slug}",
        headers={"X-Payment-TxHash": tx_hash},
    )
    r.raise_for_status()
    return r.json()


def main() -> None:
    print("=== Elevator Intelligence API Demo ===")

    # Step 1: List dossiers
    list_dossiers()

    # Step 2: Preview a dossier (free)
    slug = "otis"
    prev = preview(slug)
    print(f"\nPreview '{slug}':")
    print(f"  Vendor : {prev['vendor']}")
    print(f"  Price  : {prev['price']}")
    print(f"  Keys   : {prev['top_level_keys']}")

    # Step 3: Trigger payment flow
    print(f"\nRequesting payment details for '{slug}'...")
    payment = request_payment_details(slug)
    print(f"  Amount : {payment['amount_human']}")
    print(f"  Recipient : {payment['recipient']}")
    print(f"  USDC contract : {payment['usdc_contract']}")
    print(f"  Chain : HyperEVM (chain_id {payment['chain_id']})")
    print(f"  Nonce : {payment['nonce']}")
    print()
    print("  ── How to pay ──────────────────────────────────────────────")
    print(f"  1. Add HyperEVM to MetaMask: RPC https://rpc.hyperliquid.xyz/evm  chain_id 998")
    print(f"  2. Bridge USDC to HyperEVM via app.hyperliquid.xyz")
    print(f"  3. Send {payment['amount_human']} USDC to {payment['recipient']}")
    print(f"     USDC contract: {payment['usdc_contract']}")
    print(f"     Include nonce in calldata (see calldata_hint in 402 response)")
    print(f"  4. Retry this request with header: X-Payment-TxHash: <your_tx_hash>")
    print()
    print("  Alternatively, use the bundle endpoint for all 8 dossiers at once:")
    r = httpx.get(f"{API_BASE}/")
    bundle = r.json().get("bundle", {})
    print(f"  POST {API_BASE}/v1/bundle  →  {bundle.get('price', 'see /v1/bundle')}")
    print()

    # Step 4: Demo of retry with tx_hash (requires real payment)
    if len(sys.argv) > 1:
        tx_hash = sys.argv[1]
        print(f"Fetching dossier with tx_hash: {tx_hash}")
        dossier = pay_and_fetch(slug, tx_hash)
        print(f"Dossier keys: {list(dossier.keys())}")
        import json
        print(json.dumps(dossier, indent=2)[:2000])
    else:
        print("To fetch a dossier after payment:")
        print(f"  python api_client_demo.py 0x<your_tx_hash>")


if __name__ == "__main__":
    main()
