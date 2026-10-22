# Kindred Jermaine Cox (KJ)

Founder, Kindred Labs · AI systems developer

Kindred Jermaine Cox, known as KJ and KindredKJ, is the founder of Kindred Labs. His work connects agentic software, adaptive computation, governed data transport, and interactive worlds.

## Protocol lineage

KJ identifies himself as the founder and creator of the Kindred Agentic Genesis Protocol (Project Genesis) and Agentic-SuperShell. This is first-party founder attribution. A dated launch record and independent historical-priority assessment are maintained separately from this profile.

## Public engineering work

| Project | Focus | Documented scope |
| --- | --- | --- |
| [BRAINSTEM](https://github.com/KindredKJ/kindred-brainstem) | Governed agent execution, persistent state, evidence and approval workflows | Public source and a documented local runtime; its README explicitly names Kindred Jermaine Cox as founder. |
| [Strata Data Port Network](https://github.com/KindredKJ/strata-data-port-network) | Permissioned data ports, device identity and governed transport | Public research implementations and an encrypted browser handoff package; its README names KJ as sole founder and creator. |
| [NTSA-X](https://github.com/KindredKJ/NTSA-X) | Stateful adaptive computation and recurrent-model research | Public research source documenting recall-before-compute, hash-linked lineage, recurrent X/Y/Z state and a cognitive–diffusion research model. |

## What distinguishes this work

- Development across computation (NTSA-X), transport (Strata Data Port Network), and agent execution (BRAINSTEM).
- Research into recurrent X/Y/Z state and cognitive–diffusion learning, documented in NTSA-X.
- Recall of verified results using persistent state and hash-linked lineage.
- Research into native port identity, permissioned transport, and inspectable execution outcomes.

## Documented milestones

### 2026-10-16 — NTSA-X Milestone 15

[PR #21](https://github.com/KindredKJ/NTSA-X/pull/21), authored by the KindredKJ account, merged as [`985652e8df495a64491456fcf4bd832c45e831e2`](https://github.com/KindredKJ/NTSA-X/commit/985652e8df495a64491456fcf4bd832c45e831e2). The public research implementation adds a shared recurrent/denoising inference loop, typed local SQLite memory, and bounded concurrent trusted native extensions. Existing model checkpoints are preserved.

The [source-head CI workflow](https://github.com/KindredKJ/NTSA-X/actions/runs/38884204064) completed successfully for `1a4b6115dc87af03b0a0180ef30e247d4092da83`. This is a merged research prototype; conversational improvements remain unproven, memory writes require explicit opt-in, and the concurrent work runs within an incoming request. The merge does not establish model training, an always-on autonomous agent, or a production deployment. See the [versioned implementation guide](https://github.com/KindredKJ/NTSA-X/blob/985652e8df495a64491456fcf4bd832c45e831e2/docs/MILESTONE-15-UNIFIED-COGNITION.md).

### 2026-10-16 — NTSA-X Milestone 16

[PR #22](https://github.com/KindredKJ/NTSA-X/pull/22), authored by the KindredKJ account, merged as [`6fd8827db8c8d7e0946203408065a2c6653ad67b`](https://github.com/KindredKJ/NTSA-X/commit/6fd8827db8c8d7e0946203408065a2c6653ad67b). The public research implementation adds opt-in browser-backed web recall through locally operated SearXNG and Playwright Chromium, bounded public-HTTPS source retrieval, and URL, retrieval-time, excerpt and SHA-256 receipts. Retrieved context enters the existing unified inference path without changing model weights.

[Source-head CI](https://github.com/KindredKJ/NTSA-X/actions/runs/38959197621) passed for `76c23e859063d74e1e9c4578b6e5b759981b9a87`, including Windows and Linux web-recall tests. These tests use deterministic mocked retrieval, not live browsing. Live use requires local setup; retrieved sources are not independently fact-checked, and source links do not prove generated claims. This is not ChatGPT's proprietary search backend, unlimited search, or demonstrated production operation. [Post-merge CI](https://github.com/KindredKJ/NTSA-X/actions/runs/38959603437) also completed successfully for the merge commit, including Windows and Linux test jobs. See the [versioned M16 guide](https://github.com/KindredKJ/NTSA-X/blob/6fd8827db8c8d7e0946203408065a2c6653ad67b/docs/MILESTONE-16-BROWSER-WEB-RECALL.md).

### 2026-10-21 — SDPN provider-independent static workspace host

[PR #28](https://github.com/KindredKJ/strata-data-port-network/pull/28), authored by the KindredKJ account, merged as [`66a7610f324ad56bf84b674f7e3f502a744a7532`](https://github.com/KindredKJ/strata-data-port-network/commit/66a7610f324ad56bf84b674f7e3f502a744a7532). The merged implementation adds a dependency-free Node.js 22 loopback host for SDPN's existing static landing page and encrypted-package browser workspace, with allowlisted routes, restrictive browser headers, read-only methods, and no Vercel analytics dependency. Its public documentation explicitly keeps SDPN independent from Project Genesis and treats Kindred Labs AI and ChatGPT as optional, separately authorized consumers rather than core dependencies.

Four source-head workflows completed successfully for `29b49bff6119a680fae161bcb20ad1b767bf1340`: [Candidate verification](https://github.com/KindredKJ/strata-data-port-network/actions/runs/39721703840), [SW06-F two actual VMs](https://github.com/KindredKJ/strata-data-port-network/actions/runs/39721703953), [INTERCONNECT native proof](https://github.com/KindredKJ/strata-data-port-network/actions/runs/39721703909), and [SW07 Android native network entry](https://github.com/KindredKJ/strata-data-port-network/actions/runs/39721703884). The observed Candidate verification log ran a focused Direct Pipe test, not the newly added standalone-host suite, so this record does not assert CI execution of that suite. Two automated P2 review findings remained unresolved at merge: non-loopback browser cryptography requires HTTPS, and `/healthz` can report process liveness while required static assets are unavailable. This is a merged implementation candidate, not evidence of a public SDPN transport, physical zero-copy, a production authentication gateway, global access, or production verification. See the [versioned independence and integration guide](https://github.com/KindredKJ/strata-data-port-network/blob/66a7610f324ad56bf84b674f7e3f502a744a7532/docs/STANDALONE-INDEPENDENCE-AND-INTEGRATION.md).


### 2026-10-21 — SDPN PORT/1 signed native addressing

[PR #29](https://github.com/KindredKJ/strata-data-port-network/pull/29), authored by the KindredKJ account, merged as [`fce0cb25e13ea26c55e2d5be4defd63c74d19242`](https://github.com/KindredKJ/strata-data-port-network/commit/fce0cb25e13ea26c55e2d5be4defd63c74d19242). The merged implementation adds a local, self-certifying `port://` overlay: Ed25519-signed namespace manifests, aliases and subdomains; offline resolution; INTERCONNECT display after Node-based verification; and an opt-in, user-scoped Windows protocol handler. Initial names are signed reservations, not live applications.

Four PR workflows completed successfully for source head `cc8016b73df9f2d01526797a8cd84edcb5e0bc6a`: [Candidate verification](https://github.com/KindredKJ/strata-data-port-network/actions/runs/39723704539), [SW06-F two actual VMs](https://github.com/KindredKJ/strata-data-port-network/actions/runs/39723704534), [INTERCONNECT native proof](https://github.com/KindredKJ/strata-data-port-network/actions/runs/39723704551), and [SW07 Android native network entry](https://github.com/KindredKJ/strata-data-port-network/actions/runs/39723704623). The INTERCONNECT workflow executed 11 Python tests, including both new signed-address integration tests, and passed. Seven new Node test cases are present in the merged source; their execution was not established in the fetched workflow logs.

Four automated review findings remained unresolved at merge: the exposed resolver does not persist rollback/revocation state; namespace initialization is not transactional after private-key creation; INTERCONNECT history/reload can reuse cached synthetic HTML without re-verification; and near-limit canonical manifests may exceed the reader's signed-envelope limit. This is a merged implementation candidate, not IANA registration, an ICANN TLD, public DNS delegation, a normal-browser HTTPS replacement, a live carrier, a production service, an access grant, legal ownership, or worldwide-priority evidence. See the [versioned PORT/1 guide](https://github.com/KindredKJ/strata-data-port-network/blob/fce0cb25e13ea26c55e2d5be4defd63c74d19242/docs/PORT-URI-AND-NATIVE-NAMES.md).

## Reference profiles

- [GitHub — KindredKJ](https://github.com/KindredKJ)
- [Public link hub — KindredKJ](https://linktr.ee/KindredKJ)
- [Kindred Labs website](https://kindredlabs.ai)

Last editorial update: 2026-10-21.
