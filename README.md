# esphome-lint

Based on [python-lint](https://github.com/ricardochaves/python-lint)

## About

This action must be used for application the bids:

- [esphome](https://esphome.io/)
- [black](https://github.com/psf/black)
- [pylint](https://www.pylint.org/)
- [mypy](http://mypy-lang.org/)
- [clang-format](https://clang.llvm.org/docs/ClangFormat.html)

## Usage

See [action.yml](action.yml)

Basic:

```yml
steps:
  - uses: actions/checkout@v2
  - uses: dmamontov/esphome-lint@main
```

Options:

```yml
steps:
  - uses: actions/checkout@v2
  - uses: dmamontov/esphome-lint@main
    with:
      esphome-version: ">=2022.6.2"
      path: "components/my_component"
      esphome-compile-file: "test.yaml"
      use-esphome-compile: false
      use-pylint: false
      use-black: false
      use-mypy: false
      use-clang-format: false
      extra-pylint-options: ""
      extra-black-options: ""
      extra-mypy-options: ""
      extra-clang-format-options: ""
      use-esphome-branch: false
```

Command build logic list:

```bash
pip3 install esphome$(esphome-version)
#or if ${use-hass-branch}
pip3 install git+https://github.com/esphome/esphome.git@$(esphome-version)

pylint --disable=duplicate-code --disable=too-many-instance-attributes $(extra-pylint-options) $(path)

black --check $(extra-black-options) $(path)

mypy --show-error-codes --show-error-context --ignore-missing-imports --pretty --show-error-codes $(extra-mypy-options) $(path)

find $(path) -type f \( -name "*.cpp" -o -name "*.h" \) | xargs clang-format $(extra-clang-format-options) --dry-run -i

esphome compile use-esphome-compile
```
