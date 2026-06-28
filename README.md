```
██████╗ ██╗████████╗ ██████╗ ██████╗ ██╗███╗   ██╗
██╔══██╗██║╚══██╔══╝██╔════╝██╔═══██╗██║████╗  ██║
██████╔╝██║   ██║   ██║     ██║   ██║██║██╔██╗ ██║
██╔══██╗██║   ██║   ██║     ██║   ██║██║██║╚██╗██║
██████╔╝██║   ██║   ╚██████╗╚██████╔╝██║██║ ╚████║
╚═════╝ ╚═╝   ╚═╝    ╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝

██╗    ██╗         ██╗        ██╗  ██╗         ██╗
██║    ██║         ██║        ██║ ██╔╝         ██║
██║ █╗ ██║         ██║        █████╔╝          ██║
██║███╗██║         ██║        ██╔═██╗          ██║
╚███╔███╔╝         ██║        ██║  ██╗         ██║
 ╚══╝╚══╝          ╚═╝        ╚═╝  ╚═╝         ╚═╝
```

# Bitcoin Knowledge Base

A personal second brain for Bitcoin — compiled wiki articles and BIP summaries, built on the [Karpathy LLM knowledge base pattern](https://youtu.be/ib74sLgjIBM).

## What's here

**`Wiki/`** — ~380 articles. This includes ~170 topic articles (written in German) on Bitcoin fundamentals, self-custody, economics, privacy, and the ecosystem, plus ~210 BIP summaries (BIP-0001 through BIP-0451) in English, each distilled into a structured article with status, summary, and open questions. Sources span blogs, FAQs, books, papers, and historical texts — from early cypherpunk writing to recent technical deep-dives.

Topics covered include hardware wallets, seed phrases, multisig, and backup strategies; the UTXO model, transaction fees, mempool, SegWit, and Taproot; Lightning Network, splicing, rebalancing, and privacy; CoinJoin, silent payments, address reuse, and opsec; Bitcoin monetary theory, Austrian economics, and game theory; and mining, proof-of-work, soft forks, and consensus rules.

## Peer-reviewed energy & mining research

The corpus includes ~17 peer-reviewed papers on Bitcoin mining's relationship to energy grids, renewables, and climate. A selection:

| Paper | Journal | Year |
|---|---|---|
| Ibañez & Freier (UCL) — *Bitcoin's Carbon Footprint Revisited: PoW Mining for Renewable Energy Expansion* | [Challenges](https://doi.org/10.3390/challe14030035) | 2023 |
| Rudd, Jones, Sechrest, Batten & Porter — *Bitcoin Mining and Methane Mitigation* | [J. Cleaner Production](https://doi.org/10.1016/j.jclepro.2024.143516) | 2024 |
| Lal, Zhu & You (Cornell) — *From Mining to Mitigation: How Bitcoin Can Support Renewable Energy Development and Climate Action* | [ACS Sustainable Chem. Eng.](https://doi.org/10.1021/acssuschemeng.3c05445) | 2023 |
| Lal & You (Cornell) — *Green Hydrogen and Crypto as a Dynamic Duo* | [PNAS](https://doi.org/10.1073/pnas.2313911121) | 2024 |
| Velický — *Renewable Energy Transition Facilitated by Bitcoin* | [ACS Sustainable Chem. Eng.](https://doi.org/10.1021/acssuschemeng.3c03156) | 2023 |
| Bruno, Weber & Yates (UNC) — *Can Bitcoin Mining Increase Renewable Electricity Capacity?* | Resource and Energy Economics | 2023 |
| Moghimi et al. (Sharif / Aalto) — *Bitcoin Mining as a Virtual Energy Storage System in Microgrids* | [Int. J. Electrical Power & Energy Systems](https://doi.org/10.1016/j.ijepes.2024.109915) | 2024 |
| Menati et al. (Texas A&M / ERCOT) — *High-Resolution Modeling of Crypto Mining's Impact on Power Grids* | Advances in Applied Energy (IF 13) | 2023 |
| Bastian-Pinto et al. (PUC-Rio) — *Hedging Renewable Energy Investments with Bitcoin Mining* | [Renewable & Sustainable Energy Reviews](https://doi.org/10.1016/j.rser.2020.110520) | 2021 |
| Sai & Vranken (Open Universiteit / Radboud) — *Promoting Rigor in Blockchain Energy Footprint Research* | [Blockchain: Research and Applications](https://doi.org/10.1016/j.bcra.2023.100169) (IF 6.9) | 2024 |
| Rudd et al. (15 authors) — *Bitcoin and Its Energy, Environmental, and Social Impacts* | [Challenges](https://doi.org/10.3390/challe14040047) | 2023 |
| Ehyaei et al. — *Feasibility of Bitcoin Mining with Geothermal Energy* | [Energy Science & Engineering](https://doi.org/10.1002/ese3.1648) | 2023 |
| Dasaklis et al. — *Rethinking Bitcoin's Energy Use through Sustainable Business Models* | [Digital Business](https://doi.org/10.1016/j.digbus.2025.100114) | 2025 |

These papers cover demand response, curtailment reduction, methane mitigation, grid stability, and the use of Bitcoin mining as a flexible load alongside wind, solar, geothermal, and biorefinery systems.

## What's not here

Raw source material (articles, PDFs, transcripts) lives locally and is excluded via `.gitignore`. Only the compiled wiki is published.

## How it's built

Claude acts as librarian: ingesting sources from `RAW/`, distilling them into linked wiki articles in `Wiki/`, and maintaining the index. Every factual claim traces back to a source file. New articles are drafted with web research — sources land in `RAW/` first, then the wiki gets updated. A monthly health check audits the corpus for drift, broken links, and promotion candidates.

## Using this wiki in Obsidian

Clone or download the repo, then open the `bitcoin_kb` folder as an Obsidian vault.

**Graph View** (`Ctrl/Cmd + G`) renders the backlink network across all wiki articles. Dense clusters show where concepts overlap — useful for spotting gaps or finding related reading.

**Recommended plugins:**
- **Dataview** — query articles by status (`established`, `emerging`, `speculative`) or filter by tag. Example query to list all speculative articles:
  ````
  ```dataview
  LIST FROM "Wiki" WHERE contains(status, "speculative")
  ```
  ````
- **Obsidian Canvas** — drag articles onto a canvas to build visual mind maps around a topic (e.g. all Lightning-related nodes).
- **Backlinks pane** — open any article and check the backlinks panel to see which other articles reference it.

**Tips:**
- Start at `Wiki/INDEX.md` for the full article list.
- `Wiki/QUESTIONS.md` tracks open threads and unresolved tensions across the corpus.
- `CHANGELOG.md` at the root records what changed in each health check pass.

## Other tools

The wiki is plain markdown, so it works equally well in VS Code, iA Writer, Typora, or any other markdown editor. The `[[backlink]]` syntax is Obsidian-native but readable anywhere — just treat them as article references.

---

*Work in progress. Articles are added as new sources are ingested.*

---

Built with [Claude](https://claude.ai) · Pattern by [Andrej Karpathy](https://youtu.be/ib74sLgjIBM)
