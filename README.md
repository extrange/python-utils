# Project Template

My personal project template, for my Python/TS projects.

With this project template, you get:

- Automated testing on commit and when PRs are opened targeting the main branch (via pytest)
- `.env` validation via Pydantic Settings
- Devcontainer features, in particular:
  - Run tests and formatting on commit (via pre-commit)
  - Python linting with Ruff
  - Dockerfile linting with Hadolint
  - Non-root user setup
- Python package management with Poetry
- [`src/` project layout][src-layout]
- Production `compose.yml` file

## Getting Started

To start using this template, click 'Use this template' on the top right.

Create a root `env/` folder, and add `local.env` and `prod.env` inside for your local and production environment variables respectively.

Then, open the project in a Devcontainer.

Run your project with `python -m my_project.main`.

If you found this template useful, feel free to contribute back!

## Useful Info

Skip pre-commit hooks:

`git commit --no-verify -m 'my commit'`

## Opinions

Linting: While it is possible to lint every file, in practice simply linting the files that matter is sufficient. We don't want commits or actions to fail simply because of whitespace or format issues.

[src-layout]: https://docs.pytest.org/en/7.1.x/explanation/goodpractices.html#src-layout
