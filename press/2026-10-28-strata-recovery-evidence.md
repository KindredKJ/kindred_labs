# News release — October 28, 2026

**Kindred Labs Founder Kindred Jermaine Cox Publishes Independently Verifiable Cross-Provider Recovery Evidence**

**DENVER, Colorado — October 28, 2026** — Kindred Labs founder and AI systems developer **Kindred Jermaine Cox (KJ)** has published an updated technical evidence record for the **Strata Data Port Network (SDPN)**, a research project focused on permissioned data transport, identity-bound device presence, and verifiable execution across infrastructure providers.

The latest record, [SDPN pull request #40](https://github.com/KindredKJ/strata-data-port-network/pull/40), was merged on October 28, 2026. A standalone verifier executed in an independent third environment passed **16 of 16 checks** on a signed cross-provider recovery record. Those checks cover the Ed25519 signature, recovery and checkpoint identifiers, preserved capsule and input hashes, and a recomputation of the signed output hash.

**What the evidence does — and does not — show.** The demonstrated scope is **one bounded `HASH_TEXT` recovery** involving a previously preserved sealed checkpoint and a distinct provider-side recovery record. Independent verification of that saved record is not the same as a new live replay or verified anonymous access to a public endpoint. Automatic failover, abrupt power-loss recovery, physical attestation, independently confirmed public reachability and wider production readiness remain open.

The project has also published earlier bounded results. [External Benchmark #001, PR #35](https://github.com/KindredKJ/strata-data-port-network/pull/35), records 12 sequential external jobs, 12 successful HTTP 201 responses and independently verified signed receipts; [PR #34](https://github.com/KindredKJ/strata-data-port-network/pull/34) documents one deliberately forced Render redeploy and subsequent recovery. These separate pieces of evidence should not be conflated with automatically recovering from an unplanned outage.

Cox's related public research spans [BRAINSTEM](https://github.com/KindredKJ/kindred-brainstem), covering governed agent execution and persistent state; [NTSA-X](https://github.com/KindredKJ/NTSA-X), covering stateful adaptive computation and bounded web recall; and SDPN, covering signed port identity and governed transport. He also identifies himself as the originator of the Kindred Agentic Genesis Protocol and Agentic-SuperShell concepts. **Project Genesis was a community-oriented initiative; this announcement credits Cox's documented development and leadership without claiming exclusive authorship of every community contribution.**

**About Kindred Labs.** Kindred Labs is the technology work associated with founder Kindred Jermaine Cox, encompassing agentic AI systems, computational research, governed infrastructure, and interactive digital experiences. Public code and evidence are available through the founder's GitHub account. Statements of world-first historical priority, company equity ownership, third-party commercial deployment or global production availability are not made in this release.

**Company directory:** [Crunchbase's Kindred listing](https://www.crunchbase.com/organization/kindredlabs) lists Kindred Cox among the founders and links the historical Kindred Labs website. The founder confirms this is his company profile. This directory record supplies identity context; it is not an independent assessment of the engineering claims or a determination of sole legal ownership.

**Primary sources:** [PR #40](https://github.com/KindredKJ/strata-data-port-network/pull/40) · [PR #35](https://github.com/KindredKJ/strata-data-port-network/pull/35) · [PR #34](https://github.com/KindredKJ/strata-data-port-network/pull/34) · [Founder's public profile](https://github.com/KindredKJ/kindred_labs/blob/main/presence/FOUNDER.md)

**Media inquiries and technical source requests:** [KindredKJ on GitHub](https://github.com/KindredKJ). This is a founder-issued technical announcement, not independent editorial coverage.
