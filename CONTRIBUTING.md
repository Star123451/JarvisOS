Thank you for your interest in contributing to this project! The JarvisOS playbook is intended to be a small, safe example for AME Beta usage. Please follow these guidelines when contributing.

1. Reporting issues
- Create a clear, minimal issue describing the problem or enhancement.
- Include reproduction steps and any relevant files or error messages.

2. Contributing code
- Fork the repository and open a feature branch named descriptively (e.g., `fix/registry-action` or `feat/appx-cleanup`).
- Keep changes small and focused. One logical change per pull request helps reviewers.

3. Style & tests
- YAML files should be valid YAML. Run a YAML linter before submitting.
- If you add programmatic scripts (Python/PowerShell/etc.), include simple tests or usage notes.

4. Validation
- Use `python3 my-playbook/validate_playbook.py` to verify the playbook structure.
- If you change `playbook.conf`, make sure `UniqueId` remains a valid UUID and the `<Logo>` path is correct.

5. Pull requests
- Provide a concise description of what the change does and why.
- Link related issues if applicable.
- Maintainers may request small changes before merging.

6. Safety
- This project includes example actions that may modify Windows registry and APPX packages. Do not run the playbook on production systems without reviewing and backing up.

7. License
- By contributing, you agree that your contributions will be licensed under the project's MIT License.

Thanks — contributions and feedback welcome!
