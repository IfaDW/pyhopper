# PyHopper

> Black-box hyperparameter optimization for high-dimensional search spaces.

Maintenance fork of [pyhopper/pyhopper](https://github.com/pyhopper/pyhopper) (Mathias Lechner et al., MIT/IST Austria, Apache-2.0). The original upstream has been inactive since October 2021. This fork modernizes the package for current Python versions without altering the MCMC algorithm itself.

## Relationship to upstream

No algorithmic changes are made. The fork is limited to:

- Migration to `pyproject.toml` (PEP 621)
- Python ≥ 3.12, type hints throughout, `mypy --strict` clean
- Ruff replaces Black/isort/flake8
- Updated CI on GitHub Actions
- Dependency pinning for reproducible builds

If upstream becomes interested in re-integration, PRs are welcome.

## Installation

```bash
pip install git+https://github.com/IfaDW/pyhopper.git
```

For development:

```bash
git clone https://github.com/IfaDW/pyhopper.git
cd pyhopper
pip install -e ".[dev]"
```

## Quick start

```python
import pyhopper

def objective(params: dict) -> float:
    model = build_model(params["hidden_size"], params["dropout"])
    return validate(model)

search = pyhopper.Search(
    hidden_size=pyhopper.int(100, 500),
    dropout=pyhopper.float(0.0, 0.4, "0.1f"),
    lr=pyhopper.float(1e-5, 1e-2, "0.1g"),
    optimizer=pyhopper.choice(["adam", "rmsprop", "sgd"]),
)
best = search.run(objective, "maximize", "8h", n_jobs="per-gpu")
```

Full API documentation: see the [upstream docs](https://pyhopper.readthedocs.io/) — they apply unchanged.

## Verification

```bash
ruff check . && ruff format --check . && mypy --strict . && pytest --tb=short -q
```

## License

Apache License 2.0 (unchanged from upstream). See `LICENSE` and `NOTICE`.

## Citation

The original algorithm is described in:

> Lechner, M. et al. (2022). *PyHopper — Hyperparameter optimization*. NeurIPS Workshop "Has it Trained Yet?". [arXiv:2210.04728](https://arxiv.org/abs/2210.04728)

```bibtex
@inproceedings{lechner2022pyhopper,
  title={PyHopper -- Hyperparameter optimization},
  author={Lechner, Mathias and others},
  booktitle={NeurIPS 2022 Workshop on Has it Trained Yet?},
  year={2022}
}
```
