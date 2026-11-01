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

Right now I'm starting my next company, in AI security, and open-sourcing the tools I built along the way.

---

### Net Worth Tracker · one number for everything I own

[![source](https://img.shields.io/badge/source-networth--tracker-FF6A00?style=flat-square&labelColor=141110)](https://github.com/geo0apostolakis/networth-tracker)
[![size](https://img.shields.io/badge/TypeScript-14.7k_lines-141110?style=flat-square&labelColor=141110&color=2A2420)](https://github.com/geo0apostolakis/networth-tracker)
[![license](https://img.shields.io/badge/license-MIT-141110?style=flat-square&labelColor=141110&color=2A2420)](https://github.com/geo0apostolakis/networth-tracker/blob/main/LICENSE)

The dashboard I run my own money on. Bank, broker, cash and crypto each stay in their own currency and are converted with live FX into one net-worth line.

- It syncs on its own. Revolut comes in over Open Banking (Enable Banking, 90-day consent, the bank is asked at most every 4 hours), broker positions over the Freedom24 API, and watch-only wallets from public RPCs on Bitcoin, Solana and eight EVM chains. Nothing in it holds a key that can move money.
- The whole state is one JSON row in Postgres. Every write carries a state version, so a tab still open on an older build gets a 409 instead of overwriting a newer save.
- The PDF statement a card app exports is parsed into a ledger, and merchant rules sort it into spending categories. A hand edit always beats a rule.
- A wallet map pulls every transfer and drops spam such as zero-value moves and fake tickers. It also catches address poisoning, meaning any counterparty that shares the first four and last four hex characters with one of your own wallets.
- Two auth layers. The proxy only redirects; every API route checks the session again by itself. Login is a passkey or a password, ten wrong passwords in 15 minutes close password sign-in, and both tables run RLS with no policies, so a leaked anon key reads nothing.
- It is single-user by design, one deployment per person. There is no test suite yet.

**[Source](https://github.com/geo0apostolakis/networth-tracker)**

---

### AI Command Center · three AI agents for a US tax firm

[![source](https://img.shields.io/badge/source-ai--command--center-FF6A00?style=flat-square&labelColor=141110)](https://github.com/geo0apostolakis/ai-command-center)
[![stack](https://img.shields.io/badge/Express-Pinecone_·_Microsoft_Graph-141110?style=flat-square&labelColor=141110&color=2A2420)](https://github.com/geo0apostolakis/ai-command-center)
[![license](https://img.shields.io/badge/license-MIT-141110?style=flat-square&labelColor=141110&color=2A2420)](https://github.com/geo0apostolakis/ai-command-center/blob/main/LICENSE)

I built it in June 2026 for a live sales demo with the head of operations of a US CPA firm. The firm and every client in the repo are placeholders.

- The Librarian answers tax questions from the firm's own documents. They are cut into chunks of up to 150 words, embedded and stored in Pinecone. A question searches three namespaces (tax law, IRS guidance, client memory), and the best four hits go into the prompt as numbered sources the answer has to cite.
- The Sorter reads the first 3,000 characters of an incoming PDF and must answer with strict JSON naming one of 14 document types, the client, the tax year and a confidence. The file is then filed under client, year and type. An answer that is not valid JSON sends the file to review instead of a guessed folder.
- The Newsletter turns one plain-English instruction into targeting rules (entity types, services, states). Code applies those rules to the client list, so the model never picks recipients directly, and each matching client gets its own email written from its profile.
- Those emails are created as Outlook drafts through Microsoft Graph and are never sent by the app. A person reads them and presses send.
- Demo mode runs the whole dashboard with canned answers and no API keys, which is how the sales call ran without depending on the network.
- The repo lists its limits. There is no login, so it listens on localhost only, citation page numbers are estimates, and a newsletter rule that matches nobody falls back to every client.

**[Source](https://github.com/geo0apostolakis/ai-command-center)**

---

### Handoff · send a tokenized stock to a GitHub or X handle

[![source](https://img.shields.io/badge/source-handoff-FF6A00?style=flat-square&labelColor=141110)](https://github.com/geo0apostolakis/handoff)
[![stack](https://img.shields.io/badge/Next.js_16-viem_·_Privy_·_Postgres-141110?style=flat-square&labelColor=141110&color=2A2420)](https://github.com/geo0apostolakis/handoff)
[![license](https://img.shields.io/badge/license-MIT-141110?style=flat-square&labelColor=141110&color=2A2420)](https://github.com/geo0apostolakis/handoff/blob/main/LICENSE)

Type a handle, pick a stock, send. The recipient needs no account, no seed phrase, and may not know the app exists.

- On send, the server pregenerates a wallet for the recipient through Privy's API. Whenever they sign in with that GitHub or X account, the wallet is already theirs, with no claim transaction.
- Wallets are bound to the platform's permanent numeric user id, never to the handle. `@torvalds` can be renamed or sold; GitHub user `1024025` cannot. A `unique (platform, platform_user_id)` constraint in the schema enforces it.
- The sender never logs in or signs anything through the app. The server reads the recipient wallet's balance as a baseline, returns the address and a QR code, and credits the send once the on-chain balance delta covers the amount.
- The README states what having no sender login costs. The app cannot know who paid, and two identical requests share one deposit address and race for it.
- X handles resolve through the official API when a token is set, otherwise through a public mirror. The resolver refuses unless the screen name that comes back matches the one asked for and the id is numeric.

**[Source](https://github.com/geo0apostolakis/handoff)**

---

### SAC Capital · AI agents that trade US stocks (hackathon, team of three)

[![hackathon](https://img.shields.io/badge/DoraHacks-Turing_Test_Hackathon_2026-FF6A00?style=flat-square&labelColor=141110)](https://github.com/nikolas-sapa/sac-capital)
[![tests](https://img.shields.io/badge/tests-790-141110?style=flat-square&labelColor=141110&color=2A2420)](https://github.com/nikolas-sapa/sac-capital)
[![mode](https://img.shields.io/badge/mode-paper_trading-141110?style=flat-square&labelColor=141110&color=2A2420)](https://sapa-fund.vercel.app)

Built for the AI Alpha & Data track with [Nikolas Sapalidis](https://github.com/nikolas-sapa) (lead developer) and Ilias Konstantakopoulos (safety features and stock research). I funded the project, including its on-chain deployment, and worked on the investment strategy and the build decisions with the team.

- Claude agents trade with no human in the loop. An event screen feeds a Haiku pre-filter, a Sonnet bull case, a second Sonnet arguing against it, and then an auditor.
- A risk kernel sizes every position at quarter Kelly, with caps of 25% per name and 35% per sector, a correlation gate on 90 days of real returns, a 5% daily loss halt and a 15% drawdown breaker. New entries are blocked from 24 hours before to 2 hours after FOMC, CPI and NFP releases, while exits stay allowed.
- Each decision is serialised as canonical JSON, hashed with SHA-256 to a `bytes32` and recorded on Mantle. The dashboard recomputes the hash in the browser, so anyone can check that the on-chain record matches what the AI decided.
- Paper trading only. A live order is refused unless three separate switches are all set.
- In week six the six open positions were up about $3,980 combined on a $100k paper account, five of them green. That is paper money, and the biggest percentage winners were on positions of about $5.

**[Live](https://sapa-fund.vercel.app)** · **[Source](https://github.com/nikolas-sapa/sac-capital)**

---

```text
$ cat how-i-build.txt
  agents   Claude Code with my own skills; several agents on one repo in parallel
  verify   tests and end-to-end checks against the real APIs before I call it done
  ship     Next.js, Supabase and Vercel; idea to live product in days
  before   a year running an AI automation agency, closed in Oct 2026 to build my own
```

### Links

[georgeapostolakis.com](https://georgeapostolakis.com) · [X @Apostolakis_Geo](https://x.com/Apostolakis_Geo) · [LinkedIn](https://www.linkedin.com/in/apostolakis-george)
