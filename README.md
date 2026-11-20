# ple-harness

Agent harness for the Kaggle competition "Google - Agent Harness on Physical-Engineering's Last Exam".

- `serve.py`: WebSocket entry point (serve protocol v1, via `taskbridge.py`)
- `harness.py`: the agent (started from the `custom-openai` reference harness in google-research/ple)
- `submission.yaml`: model, build and serve commands, and per-task caps (`BUDGET_USD` estimated spend, `TOKEN_BUDGET` tokens; 0 = off)
- `artifacts/`: dev-set outputs exported by `ple/eval/run.py` (do not edit by hand)

See `../PLAN.md` for the strategy, evaluation loop and submission checklist.

License: Apache-2.0 (see LICENSE).
