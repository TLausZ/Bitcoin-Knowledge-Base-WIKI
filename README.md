# Bitcoin Knowledge Base

A personal second brain for Bitcoin — compiled wiki articles and BIP summaries, built on the [Karpathy LLM knowledge base pattern](https://youtu.be/ib74sLgjIBM).

## What's here

**`Wiki/`** — ~80 articles on Bitcoin fundamentals, self-custody, economics, privacy, and the ecosystem. **All articles are written in German.** Sourced primarily from [blog.bitbox.swiss](https://blog.bitbox.swiss) and other high-quality Bitcoin writing.

Topics covered:
- Hardware wallets, seed phrases, multisig, backup strategies
- UTXO model, transaction fees, mempool, SegWit, Taproot
- Lightning Network, splicing, rebalancing, privacy
- CoinJoin, silent payments, address reuse, opsec
- Bitcoin monetary theory, Austrian economics, game theory
- Mining, proof-of-work, soft forks, consensus rules

**`BIPs/Wiki/`** — summaries of ~200 Bitcoin Improvement Proposals (BIP-0001 through BIP-0451), each distilled into a structured article with status, summary, and open questions.

## What's not here

Raw source material (articles, PDFs, transcripts) lives locally and is excluded via `.gitignore`. Only the compiled wiki is published.

## How it's built

Claude acts as librarian: ingesting sources from `RAW/`, distilling them into linked wiki articles, and maintaining the index. Every factual claim traces back to a source file. New articles are drafted with web research, sources land in `RAW/` first, then the wiki gets updated.

---

*Work in progress. Articles are added as new sources are ingested.*
