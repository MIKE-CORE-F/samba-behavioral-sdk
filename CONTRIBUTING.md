# Contributing to S.A.N.B.A. Behavioral SDK

Thank you for your interest in the **S.A.N.B.A. Behavioral SDK**. Improvements to the adapters, the core engine interfaces and the C++ headers are welcome.

## Scope & security

- **Public scope:** this repository contains only the public SDK layer, the adapters and the C++ interface headers.
- **Proprietary core:** internal kernels, daemons and confidential libraries are not part of this repository. Pull requests that target them will not be accepted.
- **Security issues:** do not open a public issue for a vulnerability. Use GitHub's private vulnerability reporting (the **Security** tab of this repository) if it is enabled, or contact the maintainer directly.

## How to contribute

1. **Fork** the repository on GitHub.
2. **Clone** your fork:
   ```bash
   git clone https://github.com/<your-username>/samba-behavioral-sdk.git
   cd samba-behavioral-sdk
   ```
3. **Create a branch** for your change:
   ```bash
   git checkout -b my-change
   ```
4. **Make your change** and check it locally:
   ```bash
   python test_sdk_run.py
   pip install pylint
   pylint --errors-only $(git ls-files '*.py')
   ```
   For C++ changes, make sure the sources still compile, for example:
   ```bash
   g++ -std=c++11 -Wall -Wextra -Icpp_src/headers -c cpp_src/adapters/*.cpp
   ```
5. **Commit** with a clear message and **push** your branch to your fork.
6. **Open a pull request** against `main` and describe what you changed and why.

## Guidelines

- Keep pull requests small and focused on one change.
- Do not commit licence keys, credentials or customer data. The `licensing/` folder is ignored on purpose.
- Update the documentation when behaviour changes.
