from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]

REQUIRED_FILES = [
    "README_5_MINUTES.md",
    "docs/context/repository_context_index.json",
    "docs/context/rcc_nexus_index.json",
    "docs/software_architecture/geniusrouter_sa_v0_4_rcc_n_injection.md",
    "rcc/nexus/README.md",
    "rcc/nexus/rcc_nexus_protocol.md",
    "rcc/nexus/route_map.json",
    "scripts/rcc/check_rcc_nexus.py",
]

MINI_READMES = [
    "docs/README.md",
    "docs/context/README.md",
    "docs/software_architecture/README.md",
    "docs/architecture_changes/README.md",
    "docs/release_notes/README.md",
    "docs/protocols/README.md",
    "docs/validation/README.md",
    "docs/roadmap/README.md",
    "rcc/README.md",
    "rcc/nexus/README.md",
    "scripts/README.md",
    "scripts/rcc/README.md",
    "scripts/release/README.md",
    "src/README.md",
    "src/geniusrouter/README.md",
    "tests/README.md",
    "reports/README.md",
    "reports/validation/README.md",
    "reports/smoke/README.md",
    "artifacts/README.md",
    "artifacts/routing_decisions/README.md",
]

REQUIRED_MARKERS = [
    "RCC Nexus Echo Location",
    "Sphere Position:",
    "Evidence Surface:",
    "Validation Surface:",
    "Claim Boundary:",
    "Non-Claim Locks:",
    "Agent Route:",
    "Update Obligation:",
]


def main() -> int:
    missing = []
    bad_readmes = []

    for rel in REQUIRED_FILES:
        if not (ROOT / rel).exists():
            missing.append(rel)

    for rel in MINI_READMES:
        path = ROOT / rel
        if not path.exists():
            missing.append(rel)
            continue
        text = path.read_text(encoding="utf-8")
        absent = [marker for marker in REQUIRED_MARKERS if marker not in text]
        if absent:
            bad_readmes.append({"path": rel, "missing": absent})

    try:
        context = json.loads((ROOT / "docs/context/rcc_nexus_index.json").read_text(encoding="utf-8"))
    except Exception as exc:
        context = {"error": str(exc)}

    passed = not missing and not bad_readmes and context.get("schema") == "GeniusRouter-RCC-N-v0.4-nexus-index"

    report = {
        "schema": "GeniusRouter-RCC-N-v0.4-check-report",
        "passed": passed,
        "required_files_checked": len(REQUIRED_FILES),
        "mini_readmes_checked": len(MINI_READMES),
        "missing": missing,
        "bad_readmes": bad_readmes,
        "nci_mode": context.get("nci_mode"),
        "nci_target": context.get("nci_target"),
        "boundary": "RCC-N checker validates navigation surfaces only. It does not prove routing correctness, production readiness, security, patch safety, cost savings, provider reliability, or AI understanding.",
    }

    out_dir = ROOT / "reports" / "rcc_nexus"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "latest_rcc_nexus_check.json").write_text(json.dumps(report, indent=2), encoding="utf-8")

    md = [
        "# GeniusRouter RCC-N Check Report",
        "",
        f"- Passed: {passed}",
        f"- Required files checked: {len(REQUIRED_FILES)}",
        f"- Mini READMEs checked: {len(MINI_READMES)}",
        f"- Missing: {len(missing)}",
        f"- Bad mini READMEs: {len(bad_readmes)}",
        "",
        f"Boundary: {report['boundary']}",
        "",
    ]
    (out_dir / "latest_rcc_nexus_check.md").write_text("\n".join(md), encoding="utf-8")

    print(json.dumps(report, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())