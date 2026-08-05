# Pull request package

## Exact title

```text
Track 2, Physics-First AI, NuclidePath
```

## Body

### Project

**NuclidePath** is a private, physics-first AI agent for traceable Cs-137
groundwater screening. A local Qwen3.5-9B model may plan an allow-listed
workflow, while deterministic versioned tools remain authoritative for
physics, uncertainty, reporting and artifact hashes.

### Track 2 capabilities

- local knowledge retrieval with cited bundled sources;
- local multi-turn memory with redaction and SHA-256 provenance;
- multi-step planning constrained to an allow list;
- explicit permission and privacy control;
- deterministic tool invocation with auditable outputs.

All five listed capabilities are implemented and exercised. Core inference
requires no remote API.

### Current source state

The current private `main` includes an opt-in PHREEQC chemistry bridge with
schema `nuclidepath-phreeqc-chemistry-2`. It compiles an explicitly declared
Cs chemistry block with any non-empty subset of K, Na, Ca and Mg into
SOLUTION/EXCHANGE/SELECTED_OUTPUT/TRANSPORT input, supports K-free
Central Oklahoma brine/recharge fixtures, and adds deterministic per-ion
diagnostics to the report.

The canonical `transport-prototype-0.3` path remains the authoritative
screening calculation. PHREEQC is **PROCESS-QUALIFIED ONLY**: Example 2 has a
process qualification record; the new multicomponent fixtures have passed the
compiler, parser, independent arithmetic oracle and local replay checks, but
still await a trusted real run and calibrated Cs chemistry. No regulatory,
dose, operational or site-safety claim is made.

The repository also includes a separately validated EPA/Fuller/Dubus external Cs benchmark registry with source digests, CSV integrity checks and `calibration_eligible: false`. It remains outside scientific promotion.

The repository also includes a dependency-free traceable Cs exchange
calibration/hold-out gate. It validates explicit units and provenance, enforces
group-disjoint calibration and hold-out data, records hold-out metrics and a
canonical report digest, and fails closed for synthetic or unverified data. No
experimental dataset is bundled and no promotion claim is made.

### AMD deployment evidence

The AMD evidence is a dated core-platform snapshot from 28 July 2026:
ROCm 7.2.1, HIP `llama.cpp`, Qwen3.5-9B-Q8_0, all model layers offloaded,
and 231 tests passed on the recorded AMD workspace. The exact FP64
device-resident primary-GCS → transport → receptor pipeline evaluated 147,456
concentrations in a 1.784 ms median, 137.09× faster than scalar, with
maximum relative concentration error `7.94e-14`.

The preceding merged-bridge integration checkpoint is PR #15 CI run
[30928408962](https://github.com/anakinsuper/NuclidePath/actions/runs/30928408962):
Python 3.11.15, 364 passed, 15 skipped, workflow policy/wheel/whitespace PASS.
The latest code-bearing registry checkpoint is PR #24 CI run
[30993946602](https://github.com/anakinsuper/NuclidePath/actions/runs/30993946602):
373 passed, 15 skipped, with workflow policy/wheel/whitespace PASS. The preceding
calibration-gate checkpoint is PR #22 CI run
[30936374478](https://github.com/anakinsuper/NuclidePath/actions/runs/30936374478):
370 passed, 15 skipped. These are
GitHub-hosted integration checkpoints, not a fresh post-merge AMD rerun or a
trusted self-hosted PHREEQC run.

### Demo video

`VIDEO_URL_PENDING_UPLOAD`

The private core-path master is 4:36 at 1920×1080 and 30 fps with H.264/AAC
narration and embedded English subtitles. It demonstrates the canonical
agent/transport workflow; it does not show the later PHREEQC bridge. A public
URL must be uploaded and verified by the participant before it is inserted
into an official PR.

The contest branch now stores the editorial package and a complete copied source tree under `submissions/Track2-Physics-First-AI-NuclidePath/source/`, synchronized from private `main` at `2b256e3`. The public video URL remains the only missing submission link.

### Reproduce locally

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -e '.[test]'
pytest -q
nuclear-emergency-demo --samples 128 --output results/demo
nuclear-emergency-dashboard --host 127.0.0.1 --port 8080 --samples 128
```

For the optional bridge:

```bash
nuclear-phreeqc-scenario \
  scenarios/central_oklahoma_brine_multicomponent.json \
  --output results/phreeqc-brine
```

The full pipeline writes the deterministic report and manifest; the PHREEQC
path remains compile-only unless the trusted manual workflow is explicitly
run on `refs/heads/main`.

### Submission artifacts

- `README.md` — project narrative and reproduction;
- `submission/NuclidePath_Track2_Deck.pptx` — nine-slide core Track 2 deck;
- `submission/NuclidePath_Project_Specification.pdf` — current specification;
- `submission/ARTIFACT_MANIFEST.json` — sixteen tracked visual, editorial and AMD evidence hashes;
- `docs/RELEASE_STATE.md` — source/evidence/submission boundary;
- `docs/SCIENTIFIC_VALIDATION_GATE.md` — offline calibration/hold-out contract;
- `docs/SUBMISSION_CHECKLIST.md` — release gates.

### Pre-open gates

- [ ] Replace `VIDEO_URL_PENDING_UPLOAD` with a public judge-accessible URL.
- [ ] Confirm Luma registration and AMD Developer Program eligibility.
- [ ] Make the complete current source public or copy it into the contest
      submission.
- [ ] Regenerate/synchronize the contest package from the selected current
      source snapshot.
- [ ] Open the official PR only after the participant authorizes publication.
