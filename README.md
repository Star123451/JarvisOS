![JarvisOS Logo](./jarvislogo.png)

# jarvisuwu — JarvisOS Playbook

A packaged, AME Beta–compatible playbook called JarvisOS (catgirl theme). This repository contains the playbook sources, a lightweight validator, and a ready-to-upload release archive.

Quick links
- Playbook folder: `my-playbook/`
- Playbook archive (release): `jarvisos_v1.0.0.apbx` (also published to Releases)
- Local validator: `my-playbook/validate_playbook.py`

What’s inside
- `my-playbook/playbook.conf` — XML metadata used by AME Beta (includes Logo and UniqueId).
- `my-playbook/Configuration/main.yml` — entry point for the playbook actions.
- `my-playbook/Configuration/Tasks/` — action files (`registry.yml`, `appx.yml`).
- `my-playbook/Executables/` — example helper scripts (placeholder `hello.bat`).
- `my-playbook/logo.png` — included logo for the playbook UI.
- `jarvisos_v1.0.0.apbx` — packaged playbook archive (ready for upload).

Usage

1. Validate locally

	Run the included structural validator to confirm required files exist:

	```bash
	python3 my-playbook/validate_playbook.py
	```

	Expected output: `VALIDATION PASSED: playbook structure looks good for AME Beta.`

2. Inspect contents

	You can browse the `my-playbook/` folder to review the YAML tasks and `playbook.conf` before deploying.

3. Upload to AME Beta

	- Use the AME Beta UI or import mechanism and choose `jarvisos_v1.0.0.apbx`.
	- Review the playbook details (Title, Description, Logo) and verify UniqueId.

Developer notes

- The validator is intentionally lightweight: it checks structure but does NOT execute any actions.
- Backup Windows systems before running any playbook that modifies the registry or removes packages.
- To rebuild the APBX locally:

  ```bash
  zip -r jarvisos_v1.0.0.apbx my-playbook
  sha256sum jarvisos_v1.0.0.apbx
  ```

Publishing releases

- A release `v1.0.0` was created and the archive uploaded. To recreate or add assets, you can use the GitHub CLI:

  ```bash
  gh release upload v1.0.0 jarvisos_v1.0.0.apbx --clobber
  ```

Safety & license

- This repository contains example actions that may modify Windows registry and APPX packages. Use in a test environment first.
- No license file is included — add one if you intend to publish.

Need help?

If you want changes (tweaked tasks, different packages, version bump, or more release notes/screenshots), tell me what to change and I’ll update it and rebuild the archive.
