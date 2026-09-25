---
title: "Packaging, project layout & monorepos"
track: python
slug: packaging-project-structure
priority: P1
complexity: 2
est_hours: 2
phase: 2
tags: [python, P1]
last_reviewed: 2026-09-25
---

# Packaging, project layout & monorepos

!!! abstract "At a glance"
    **Priority:** P1 · **Complexity:** 2/5 · **Est. time:** 2 h · **Phase:** 2 · **Prereqs:** [Modern tooling](modern-tooling.md)
    **You're done when:** you can lay out an installable `src/` project with a correct `pyproject.toml`, build and inspect a wheel, structure a uv-workspace monorepo with enforced boundaries, and publish to a private index safely.

## Why it matters

Packaging is where "works on my machine" is born. Correct layout and metadata give you reproducible installs, importable-only-when-installed tests (catching missing files), clean Docker builds, internal libraries shared across services (domain models, LLM client wrappers, eval harnesses), and supply-chain safety. Monorepos with shared Pydantic contracts are common in AI platforms, so the workspace and dependency-boundary story matters for Staff-level platform design.

## Core concepts

### The standards stack

| Standard | What it fixes |
|---|---|
| PEP 517/518 (`[build-system]`) | Build backend declared in `pyproject.toml`, no more `setup.py` execution |
| PEP 621 (`[project]`) | Standard metadata: name, version, dependencies, `requires-python`, scripts |
| PEP 735 (`[dependency-groups]`) | Non-published dev/test/docs groups (replaces ad-hoc requirements-dev.txt) |
| PEP 723 | Inline script metadata |
| PEP 751 (`pylock.toml`) | Standard lock file format |
| Wheels (PEP 427) + platform tags | Prebuilt distribution, including `cp314t` tags for free-threaded builds |

### Layout: src/ vs flat

```
llm-platform/
├── pyproject.toml
├── uv.lock
├── src/
│   └── llm_platform/
│       ├── __init__.py
│       ├── py.typed              # ship type information (PEP 561)
│       ├── domain/
│       └── adapters/
├── tests/
└── README.md
```

**Why `src/`:** with a flat layout, `pytest` run from the repo root imports your working tree, not the installed package, so a missing package-data file or wrong `packages` config passes locally and fails in production. With `src/`, tests can only import the *installed* package (editable install in dev), which surfaces packaging errors early. Hynek's "testing and packaging" article is the canonical argument.

### A production `pyproject.toml`

```toml
[project]
name = "llm-platform"
version = "0.4.0"
description = "Shared LLM client, tools and contracts"
requires-python = ">=3.13"
dependencies = [
  "pydantic>=2.11,<3",
  "httpx>=0.27",
]

[project.optional-dependencies]
otel = ["opentelemetry-sdk>=1.30"]

[project.scripts]
llm-eval = "llm_platform.cli:main"

[dependency-groups]
dev = ["pytest>=9", "ruff", "ty"]

[build-system]
requires = ["uv_build>=0.9,<0.13"]
build-backend = "uv_build"
```

- **Applications** pin via the lock and can be loose in `pyproject.toml`. **Libraries** must declare *ranges* (lower bound tested, upper bound only when known-broken. Avoid blanket `<3` caps for stable packages because they cause resolver conflicts downstream) and test the lower bounds (`--resolution lowest-direct`).
- Backends: `uv_build` (fast, simple, pure-Python), `hatchling` (plugins, dynamic versions from VCS), `setuptools` (legacy/C-ext), `maturin` (Rust extensions), `scikit-build-core` (CMake). Publishing a library and worried about backend lock-in? Choose a mainstream neutral backend such as hatchling.
- Version: single-source it (`hatch-vcs`/`setuptools-scm` from git tags, or explicit bumps). Never hand-edit in two places.
- Build and inspect: `uv build` then `unzip -l dist/*.whl` and `uvx twine check dist/*`. Verify `py.typed`, data files and the entry points are inside.

### Monorepo with uv workspaces

```toml
# root pyproject.toml
[tool.uv.workspace]
members = ["libs/*", "services/*"]

[tool.uv.sources]
contracts = { workspace = true }
```

```
repo/
├── libs/contracts/       # Pydantic models shared across services
├── libs/llm_client/
├── services/gateway/     # depends on contracts, llm_client
├── services/ingest/
└── uv.lock               # one lock for all members
```

- `uv sync --package gateway` installs only that member's closure. `uv run --package ingest pytest`.
- Docker per service: copy the workspace lock and only needed members, sync `--package gateway --locked --no-dev`.
- **Boundary enforcement is your job**: nothing stops `services/gateway` importing `services/ingest` if it's installed in the same venv. Use `import-linter` contracts or per-member venvs (`--package` sync) to make illegal imports fail. Declare dependencies explicitly in each member's `pyproject.toml`.
- Affected-only CI: compute changed members plus reverse dependencies (`uv tree --invert`, or Pants/Bazel/Nx for big repos), and test only those.
- Pants/Bazel: consider only when >~100 engineers and cross-language builds justify the ops load. uv workspace plus path-filtered CI covers most Python-centric orgs.

### Dependency hygiene

- Private index: `[[tool.uv.index]] name="internal" url=... explicit=true` and pin specific packages to it via `[tool.uv.sources]`. This prevents dependency confusion attacks.
- Trusted publishing (OIDC, no long-lived tokens) for PyPI or your registry, sign or attest artifacts, and generate SBOMs from the lock ([tooling](modern-tooling.md)).
- Import name vs distribution name differ (`pip install pillow` gives `import PIL`). Use `importlib.metadata` for version lookup: `importlib.metadata.version("llm-platform")`.
- Extras for optional heavy deps (`[otel]`, `[torch]`), and lazy-import them with a clear error message.
- Free-threaded and platform wheels: check for `cp314t` availability of native deps before promising 3.14t support.
- Entry points (`[project.entry-points."llm_platform.tools"]`) let out-of-tree plugins register without import-time global side effects ([registry pattern](decorators-descriptors-metaclasses.md)).

### Senior nuance

- Namespace packages (PEP 420) let teams share a top-level (`acme.billing`, `acme.llm`), but forgetting that no `__init__.py` means no implicit regular package causes confusing import behaviour. Prefer distinct top-level names unless you truly need a namespace.
- `python -m package` needs `__main__.py`. Console scripts are generated shims that import your entry function.
- Editable installs (`uv sync` default for the project) use `.pth`/finders, so they can hide packaging bugs (missing data files). Always run one CI job that installs the *built wheel* and runs the smoke tests.
- Circular imports usually indicate layering mistakes. Fix with dependency inversion, not import-time hacks.
- Version pins in Docker: base image digest pin plus lock-file install gives byte-reproducible-ish builds.

## Resources

| Resource | Type | Why this one | Level | Cost |
|---|---|---|---|---|
| [Python Packaging User Guide](https://packaging.python.org/en/latest/) | docs | Canonical tutorials and specifications | intermediate | free |
| [Writing your pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/) | docs | Field-by-field reference | intermediate | free |
| [src layout vs flat layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/) | docs | The official comparison | intermediate | free |
| [uv: workspaces](https://docs.astral.sh/uv/concepts/projects/workspaces/) | docs | Monorepo mechanics and limits | intermediate | free |
| [uv: project layout and build backend](https://docs.astral.sh/uv/concepts/build-backend/) | docs | `uv_build` config and build/publish flow | intermediate | free |
| [Hynek: Testing & packaging](https://hynek.me/articles/testing-packaging/) :gem: | article | Why src layout + testing installed code | advanced | free |
| [PEP 751 / pylock.toml](https://packaging.python.org/en/latest/specifications/pylock-toml/) | spec | Standard lock format | advanced | free |
| [Hynek: Production-ready Docker with uv](https://hynek.me/articles/docker-uv/) :gem: | article | Packaging meets deployment | advanced | free |
| [Boring Python: dependency management](https://www.b-list.org/weblog/2022/may/13/boring-python-dependencies/) :gem: | article | Principles for durable dependency choices | intermediate | free |

## Hands-on lab

**Goal (60-90 min):** a two-service workspace with a shared contracts library.

1. `mkdir platform && cd platform`, create root `pyproject.toml` with `[tool.uv.workspace] members=["libs/*","services/*"]`.
2. `uv init --lib libs/contracts` (Pydantic models `Message`, `ToolCall`), `uv init --package services/gateway`, `uv init --package services/ingest`.
3. `cd services/gateway && uv add contracts` (resolves via workspace source). Confirm `[tool.uv.sources] contracts = { workspace = true }`.
4. From the root: `uv sync --all-packages`, then `uv run --package gateway python -c "import contracts; print(contracts.__file__)"`.
5. Add an `import-linter` config forbidding `gateway` to import `ingest` and vice versa. Add an illegal import and run `uv run lint-imports`: **Expected:** the contract is reported broken.
6. `uv build --package contracts` then `unzip -l dist/*.whl`. **Expected:** `contracts/py.typed` and no `tests/` in the wheel.
7. In a clean temp venv: `uv pip install dist/*.whl` and run an import smoke test (this is the "installed wheel" CI job).
8. Change `contracts` and use `uv tree --invert --package contracts` to list who is affected (your affected-only CI input).

## Questions

### L1 - Recall

??? question "Q1. Why use a `src/` layout?"
    ??? success "Answer"
        Tests and tools can't accidentally import the working tree from CWD, so they exercise the *installed* package. Packaging errors (missing files, wrong package discovery) surface in development instead of after release.

??? question "Q2. Difference between `[project.optional-dependencies]` and `[dependency-groups]`?"
    ??? success "Answer"
        Optional dependencies (extras) are published metadata users can install (`pkg[otel]`). Dependency groups (PEP 735) are local development groups (dev, test, docs) that aren't part of the distributed metadata.

??? question "Q3. What is `py.typed` for?"
    ??? success "Answer"
        A marker file (PEP 561) telling type checkers that the package ships inline type hints, so consumers' checkers use your annotations instead of treating the package as untyped.

??? question "Q4. Library vs application dependency specification?"
    ??? success "Answer"
        Applications pin exact resolved versions via a lock for reproducible deploys. Libraries publish compatible ranges (tested lower bound, no unnecessary upper caps) so they compose with other packages' constraints.

### L2 - Apply

??? question "Q5. Tests pass locally, but the deployed wheel fails with `FileNotFoundError` for `prompts/system.txt`. Why and how do you prevent it?"
    ??? success "Answer"
        The data file wasn't included in the wheel (backend config or `package-data` missed it), and flat layout/editable install let tests read it from the working tree. Fix: include the data via backend config, load with `importlib.resources.files("pkg") / "prompts/system.txt"`, and add a CI job that builds the wheel, installs into a clean venv and runs smoke tests. Use src layout.

??? question "Q6. Two services in your workspace need different versions of `numpy`. What do you do?"
    ??? success "Answer"
        A uv workspace has one lock and one resolution, so conflicting requirements fail to resolve. Options: align versions (preferred, and a sign to schedule an upgrade), split the outlier into its own project/lock (outside the workspace or a separate workspace), or use uv's conflicting-extras/groups declarations if the conflict is between optional sets rather than services.

??? question "Q7. How do you stop a `services/gateway` from importing `services/ingest` code?"
    ??? success "Answer"
        Declare only real dependencies in each member's pyproject, sync per member (`uv sync --package gateway`) so unlisted members aren't installed in its environment, and add `import-linter` contracts as a CI gate for the shared dev venv. Move shared code to a `libs/` member both may depend on.

??? question "Q8. A private package name `acme-llm` exists on your internal index, and a build suddenly pulls a malicious `acme-llm` from PyPI. What happened and what's the fix?"
    ??? success "Answer"
        Dependency confusion: the resolver searched multiple indexes and picked the higher version from the public one. Fix: pin the package to the internal index with `[tool.uv.sources]` and mark it `explicit = true`, so only named packages come from it. Also reserve the name on PyPI, verify hashes via the lock, and use an index proxy allow-list.

### L3 - Design & trade-offs

??? question "Q9. Monorepo (uv workspace) vs polyrepo for 8 services sharing contracts and an LLM client library."
    ??? success "Answer"
        Monorepo: atomic cross-cutting changes, one lock/upgrade, easy refactors and shared tooling, at the cost of CI scaling (need affected-only builds), permissions/ownership granularity, and version coupling (everyone upgrades together). Polyrepo: independent release cadence and clear ownership, but version drift, painful cross-repo changes, and contract skew. With shared, fast-moving contracts (Pydantic models) I'd choose the monorepo with CODEOWNERS and affected-only CI. Publish libs to an index only when non-monorepo consumers appear.

??? question "Q10. Publish shared libs to an internal index vs consume from the monorepo directly?"
    ??? success "Answer"
        Direct workspace consumption gives immediate integration but forces synchronised upgrades and can't serve outside repos. Publishing gives semantic versioning, independent upgrades and external consumption but adds release process, compatibility burden (deprecation policy) and drift. Hybrid: workspace for in-repo services, publish tagged releases for external consumers, with contract tests guarding compatibility.

??? question "Q11. Which build backend do you standardise on for internal libraries, and why?"
    ??? success "Answer"
        Criteria: pure-Python vs native extensions, dynamic versioning from git, plugin needs, build speed, team familiarity, and lock-in. Pure-Python internal libs: `uv_build` (fast, minimal) or hatchling (mature, VCS versioning, wide adoption). Native: maturin (Rust) or scikit-build-core (C/C++). Standardise on one default in the template, allow documented exceptions, and keep `pyproject.toml` standard so switching backends is a one-file change.

### L4 - Staff-level ambiguity

??? question "Q12. Design the release and versioning strategy for a shared `contracts` library consumed by 15 services, some Java consumers reading its JSON Schema."
    ??? success "Answer"
        Treat contracts as a product: semver with an explicit compatibility policy (additive changes are minor; removals/renames are major after a deprecation window), schema snapshots in CI that fail on breaking diffs (JSON Schema diff tool), generated schemas published as versioned artifacts for non-Python consumers, and consumer-driven contract tests. Release train: monthly with automation from conventional commits, changelog, and Renovate PRs to consumers. Provide migration codemods for majors. Metrics: number of services on latest-1, breaking-change incidents, and time to roll out a schema change.

??? question "Q13. A CTO asks whether to adopt Bazel/Pants for the Python monorepo. Provide a decision framework."
    ??? success "Answer"
        Evidence-based triggers: CI time dominated by unnecessary rebuilds/tests, multi-language dependency graphs (Python + Java + protobuf) needing hermetic builds, or > ~100 engineers with strict ownership. Alternatives first: uv workspace + affected-only CI + caching may deliver 80% of the benefit. Costs of Bazel/Pants: BUILD files, learning curve, custom rules for Python edge cases, IDE friction, dedicated platform engineers. Pilot on one slice with measured CI-time and developer-satisfaction metrics, then decide with a rollback plan. Don't adopt for prestige.

## Real-world use cases

- **AI platform monorepo:** `contracts` (Pydantic), `llm_client`, `evals` libs and 6 services in one uv workspace and one lock.
- **Published SDK:** a src-layout package with `py.typed`, trusted publishing and a wheel smoke-test job.
- **Plugin ecosystem:** entry points allow partner teams to ship carrier connectors without touching core.
- **Docker builds:** per-service images from the workspace lock, with layer caching by member closure.

## Pitfalls & anti-patterns

- Flat layout with tests importing the working tree.
- Unpinned applications; over-pinned libraries (`==`) or reflexive upper caps.
- Publishing without inspecting the wheel contents.
- Shared "utils" package growing into a dependency hairball.
- Workspace members implicitly depending on each other through the shared venv.
- Multiple indexes without `explicit`, leaving dependency-confusion exposure.
- Long-lived PyPI tokens in CI instead of trusted publishing.

## Checklist

- [ ] I can explain src layout, PEP 621/735, and library vs app pinning without notes
- [ ] I built a uv workspace with a shared library and verified the wheel contents
- [ ] I enforced a boundary with import-linter
- [ ] I answered all L3 questions out loud in < 3 min each
