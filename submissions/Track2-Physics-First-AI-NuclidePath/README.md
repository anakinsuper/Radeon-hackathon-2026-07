# Track 2, Physics-First AI, NuclidePath

**Track:** 2 — Development & Local Deployment of Private AI Agents

**Team:** Physics-First AI (Stefano Rigante, GitHub [@anakinsuper](https://github.com/anakinsuper))

**Application:** NuclidePath

NuclidePath is a private, physics-first AI agent for traceable Cs-137 groundwater screening. A local Qwen3.5-9B planner proposes a constrained six-step workflow, while deterministic, versioned tools remain authoritative for every physical value, uncertainty result, warning, report and artifact hash.

## Links

| Item | URL |
|---|---|
| Source code | <https://github.com/anakinsuper/NuclidePath> |
| Demo video | `VIDEO_URL_PENDING_UPLOAD` |
| Project specification | [`NuclidePath_Project_Specification.pdf`](./NuclidePath_Project_Specification.pdf) |
| Presentation deck | [`NuclidePath_Track2_Deck.pptx`](./NuclidePath_Track2_Deck.pptx) |
| Artifact manifest | [`ARTIFACT_MANIFEST.json`](./ARTIFACT_MANIFEST.json) |

> The public video URL and final contest PR remain human approval gates. This branch must not be opened as the official PR while the placeholder remains.

## Track 2 capabilities — 5/5

- **Local knowledge retrieval:** bundled Markdown corpus with cited workflow evidence.
- **Tool invocation:** allow-listed deterministic transport, GCS and uncertainty tools.
- **Multi-step planning:** local Qwen planner constrained to a validated six-step workflow, with deterministic fallback.
- **Local multi-turn memory:** private redacted JSONL session store with mode `0600` and deletion support.
- **Permission and privacy controls:** loopback-only HTTP/LLM endpoints, action allow list and denied-action evidence.

## Current AMD Radeon / ROCm evidence

- AMD Radeon `gfx1100`, ROCm 7.2.1;
- Qwen3.5-9B Q8 through a local `llama.cpp` HIP endpoint;
- 231 tests passed on AMD ROCm;
- exact FP64 primary-GCS → transport → receptor pipeline;
- 147,456 concentration evaluations in a 1.784 ms median;
- 137.09× versus the canonical scalar reference;
- maximum relative concentration error `7.94e-14`;
- controller gates: 216 passed/13 optional-PyTorch skips dependency-light and 231 passed with PyTorch.

Raw benchmark metadata, timings and hashes are retained in the source repository under `artifacts/amd-2026-07-28/platform-current/`.

## Reproduce

```bash
git clone https://github.com/anakinsuper/NuclidePath.git
cd NuclidePath
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -e '.[test]'
pytest -q
nuclear-emergency-demo --samples 128 --output results/demo
nuclear-emergency-dashboard --host 127.0.0.1 --port 8080 --samples 128
```

The submission manifest verifies ten current editorial, screenshot and AMD evidence artifacts. The clean wheel includes the primary-paper rock validation dataset used by the dashboard.

## Scientific scope

NuclidePath is a transparent research screening demonstration—not an operational emergency-response system, dose model or site-validated digital twin. The primary Cs GCS covers K/Na competition on three illite site types and NH4 only on frayed-edge sites. Sr-90 remains a provenance-bearing linear-Kd path; unsupported Sr/Ca/Mg coefficients are not invented. The rock reconstructions are paper-input predictions, not digitized experimental validation. The local LLM never generates or modifies physical values.
