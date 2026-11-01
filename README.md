<img src="banner.svg" alt="George Apostolakis" width="100%">

I'm 15 and I live in Athens. I build AI software and web products end to end, and I invest in the companies building the AI stack.

![TypeScript](https://img.shields.io/badge/TypeScript-141110?style=flat-square&logo=typescript&logoColor=FF8A2A)
![Python](https://img.shields.io/badge/Python-141110?style=flat-square&logo=python&logoColor=FF8A2A)
![Next.js](https://img.shields.io/badge/Next.js-141110?style=flat-square&logo=nextdotjs&logoColor=FF8A2A)
![React](https://img.shields.io/badge/React-141110?style=flat-square&logo=react&logoColor=FF8A2A)
![Node.js](https://img.shields.io/badge/Node.js-141110?style=flat-square&logo=nodedotjs&logoColor=FF8A2A)
![Supabase](https://img.shields.io/badge/Supabase-141110?style=flat-square&logo=supabase&logoColor=FF8A2A)
![Postgres](https://img.shields.io/badge/Postgres-141110?style=flat-square&logo=postgresql&logoColor=FF8A2A)
![Claude Code](https://img.shields.io/badge/Claude_Code-141110?style=flat-square&logo=anthropic&logoColor=FF8A2A)
![n8n](https://img.shields.io/badge/n8n-141110?style=flat-square&logo=n8n&logoColor=FF8A2A)
![Vercel](https://img.shields.io/badge/Vercel-141110?style=flat-square&logo=vercel&logoColor=FF8A2A)

**Now:** starting my next company, in AI security · open-sourcing the tools I built along the way · shipping with Claude Code agent teams.

---

### Net Worth Tracker: everything you own, one number

[![stack](https://img.shields.io/badge/Next.js_16-Supabase-141110?style=flat-square&labelColor=141110&color=FF6A00)](https://github.com/geo0apostolakis/networth-tracker)
[![chains](https://img.shields.io/badge/wallets-10_chains-141110?style=flat-square&labelColor=141110&color=2A2420)](https://github.com/geo0apostolakis/networth-tracker)
[![license](https://img.shields.io/badge/license-MIT-141110?style=flat-square&labelColor=141110&color=2A2420)](https://github.com/geo0apostolakis/networth-tracker/blob/main/LICENSE)

My own finance dashboard. Bank, brokerage, cash and crypto in any currency, converted with live FX into one net-worth line. Revolut syncs through Open Banking, broker positions through the Freedom24 API, and watch-only wallets are read straight from public RPCs on Bitcoin, Solana and eight EVM chains, with no key that can move money.

```bash
git clone https://github.com/geo0apostolakis/networth-tracker && cd networth-tracker && npm install && npm run dev
```

Card statements from a PDF become a ledger · spending rules by merchant · a wallet map that flags address-poisoning lookalikes · passkey login, a one-tap mode that hides every figure, and several skins over the same data.

**[Source](https://github.com/geo0apostolakis/networth-tracker)**

---

### PDF to Word: same pages, working links

[![live](https://img.shields.io/badge/live-pdf--to--word--pages.vercel.app-FF6A00?style=flat-square&labelColor=141110)](https://pdf-to-word-pages.vercel.app)
[![offline](https://img.shields.io/badge/runs-in_your_browser-141110?style=flat-square&labelColor=141110&color=2A2420)](https://github.com/geo0apostolakis/pdf-to-word)
[![license](https://img.shields.io/badge/license-MIT-141110?style=flat-square&labelColor=141110&color=2A2420)](https://github.com/geo0apostolakis/pdf-to-word/blob/main/LICENSE)

Drop a PDF, an HTML page or a slide deck and get a `.docx` where every page looks exactly like the original, with the links still clickable and the link words as real text. One offline HTML file; nothing you drop on it leaves the browser.

The hard part was Apple: Mail's preview adds 5.4 pt under every page and places floating objects from the top of their section, so each page is its own section with a full-size copy of the picture floating on top. Word and Apple now line up exactly. The [README](https://github.com/geo0apostolakis/pdf-to-word#the-hard-parts) has the rest, including how untrusted HTML is sandboxed.

**[Try it](https://pdf-to-word-pages.vercel.app)** · **[Source](https://github.com/geo0apostolakis/pdf-to-word)**

---

### Tools and products

| Project | What it does | Try it |
|---|---|---|
| [**redate**](https://github.com/geo0apostolakis/redate) | Change the dates in a Word or PDF file and get the same file back. PDF edits keep the font (or a metric twin), keep the alignment and are appended, so every original byte stays | [live](https://imerominies.vercel.app) · `npm test` |
| [**Handoff**](https://github.com/geo0apostolakis/handoff) | Send a tokenized stock to a GitHub or X handle. The wallet exists the moment it lands, bound to the account's permanent user id, so renaming a handle moves nothing | [repo](https://github.com/geo0apostolakis/handoff) |
| [**Preclear**](https://github.com/geo0apostolakis/preclear) | Pre-trade clearance for tokenized stocks: five checks that must all pass before an order reaches a router, and a receipt with a reason code for every decision | `npx tsx scripts/gate.check.ts` |
| [**ColdReach**](https://github.com/geo0apostolakis/coldreach-share) | Cold email from a Google Sheet: per-lead AI lines, ramped daily volume, Outlook sending, and a claim-before-send lock so a crashed run never emails anyone twice | [repo](https://github.com/geo0apostolakis/coldreach-share) |

---

```text
$ cat how-i-build.txt
  agents   Claude Code with my own skills; several agents on one repo in parallel
  verify   tests and end-to-end checks against the real APIs before I call it done
  ship     Next.js, Supabase and Vercel; idea to live product in days, not months
  before   a year running an AI automation agency, closed in Oct 2026 to build my own
```

### Links

[georgeapostolakis.com](https://georgeapostolakis.com) · [X @Apostolakis_Geo](https://x.com/Apostolakis_Geo) · [LinkedIn](https://www.linkedin.com/in/apostolakis-george)
