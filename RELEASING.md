# Releasing

Bump `synoptiko.__version__` in the PR. Run `./lint.sh`, `./test.sh`, and the
Python 3.11–3.14 CI matrix, including the real annotation test. After review and
green CI, merge to `master` and release from its clean, current checkout:

```sh
python -m build
python -m twine check dist/*
python -m twine upload dist/*
```

Create and push the matching annotated `v<version>` Git tag, then verify the
published version and wheel dependencies on PyPI. Build/upload tooling belongs
in the release environment. Travis no longer publishes releases.
