# ⛓️ Blockchain Implementation

> A blockchain built from scratch — linked blocks, SHA-256 hashing, ECDSA-signed transactions, Proof-of-Work consensus · Google Colab

[![License](https://img.shields.io/badge/License-AGPL--3.0-e8b84b?style=flat-square)](LICENSE)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python)
![Cryptography](https://img.shields.io/badge/cryptography-42%2B-4B8BBE?style=flat-square)
![Colab](https://img.shields.io/badge/Run%20on-Google%20Colab-F9AB00?style=flat-square&logo=googlecolab)

---

## 🚀 Features

- **Linked-Block Data Structure** — each block stores its transactions, a timestamp, and the previous block's hash, making the chain tamper-evident
- **Digital Wallets** — ECDSA (SECP256K1) key pairs, the same curve Bitcoin uses, for generating addresses and signing transactions
- **Signed Transactions** — every non-reward transaction must carry a valid signature from the sender's private key before it's accepted
- **Proof-of-Work Mining** — blocks must be mined by finding a nonce that produces a hash with N leading zeros, with adjustable difficulty
- **Chain Validation** — walks the full chain checking hash integrity, block linkage, PoW difficulty, and every transaction's signature
- **Tampering Demo** — shows exactly how editing past data breaks validation, even after recomputing the tampered block's own hash
- **Consensus Simulation** — multiple simulated nodes with diverging chains resolved via the longest-valid-chain rule
- **Balance Tracking** — computes any address's balance by walking the full transaction history
- **Zero Local Setup** — runs entirely inside one Colab notebook, nothing to install on your machine

---

## 📁 Project Structure

```
blockchain_implementation/
├── Blockchain_Implementation.ipynb    # The entire project — one notebook, run top to bottom
└── README.md
```

Since this is built specifically to run in Google Colab, it's structured as a single notebook rather than a package of scripts. Each section below corresponds to a group of cells inside it:

```
Blockchain_Implementation.ipynb
├── 1. Install dependencies         # cryptography
├── 2. Imports
├── 3. Wallet class                 # ECDSA key pairs, addresses, signing
├── 4. Transaction class            # signed transfers between addresses
├── 5. Block class                  # data structure + compute_hash()
├── 6. Blockchain class             # chain, mempool, mine_pending_transactions()
├── 7. Demo                         # wallets, a payment, mining, balances
├── 8. Tampering demo               # why edited history fails validation
├── 9. resolve_conflicts()          # longest-valid-chain consensus rule
└── 10. Difficulty comparison       # how mining time scales with difficulty
```

---

## ⚙️ Setup

```bash
# 1. Open the notebook in Google Colab
# (upload Blockchain_Implementation.ipynb, or open it directly from Drive/GitHub)

# 2. Run the first cell inside Colab — installs the one dependency
!pip install -q cryptography
```

No accounts, API keys, or external services needed — everything runs locally within the notebook.

---

## ▶️ Usage

All usage happens by running notebook cells in order, no command line involved.

```python
# Create a chain and some wallets
chain = Blockchain(difficulty=4, mining_reward=10.0)
alice, bob, miner = Wallet(), Wallet(), Wallet()

# Fund Alice, then have her pay Bob (signed with her private key)
chain.add_transaction(Transaction(sender="SYSTEM", recipient=alice.address, amount=50.0))
chain.mine_pending_transactions(miner_address=miner.address)

tx = Transaction(sender=alice.address, recipient=bob.address, amount=15.0)
tx.sign_with(alice)
chain.add_transaction(tx)
chain.mine_pending_transactions(miner_address=miner.address)

# Check balances and validate the whole chain
chain.get_balance(bob.address)
chain.is_chain_valid()
```

### Key settings

| Setting          | Default | Description                                                    |
|-------------------|---------|--------------------------------------------------------------------|
| `difficulty`        | `4`     | Number of leading zeros required in a block's hash to mine it        |
| `mining_reward`      | `10.0`  | Amount paid to the miner's address for successfully mining a block   |
| Curve                | `SECP256K1` | Elliptic curve used for wallet key pairs (same as Bitcoin)       |

---

## 📊 Output

No files are written by default — the notebook prints the chain, balances, and validation results directly. Add your own `json.dump(...)` calls if you want to persist a chain snapshot to disk.

---

## ⚠️ Disclaimer

> This project is for **educational purposes only** — it's a teaching model, not production blockchain infrastructure.
> It has no real peer-to-peer networking, no Merkle trees, no UTXO/account-state model, and no fee market — all of which real blockchains rely on. It implements Proof-of-Work specifically because it's the most intuitive consensus mechanism to demonstrate with a mining loop; modern networks like Ethereum use Proof-of-Stake instead, which works quite differently.

---

## 📄 License

AGPL-3.0 License — see [LICENSE](LICENSE)
