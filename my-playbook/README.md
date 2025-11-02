
![JarvisOS Logo](./logo.png)

JarvisOS (catgirl) Playbook — AME Beta compatible

Structure
---------

This folder is shaped for AME Beta:

- `playbook.conf` — XML metadata used by AME Beta
- `Configuration/main.yml` — playbook entry with task references
- `Configuration/Tasks/*.yml` — action files (registry, appx)
- `Executables/` — helper scripts or executables the playbook may run

Quick start
-----------

1. Replace the placeholder UniqueId in `playbook.conf` with a real UUID. On most systems you can generate one with `uuidgen`.

2. Place the `my-playbook` folder in the location AME Beta expects for playbooks, or import it via the AME Beta UI if available.

3. Run AME Beta and select this playbook. Review the actions carefully before running. These tasks modify system registry and remove/clear APPX packages on Windows.

Local validation
----------------
Run the included validator to check the minimal structure:

```bash
python3 validate_playbook.py
```

Notes
-----
- This repository contains example action files with catgirl-themed texts. The YAML files are structural examples and should be reviewed and tested in a safe environment before running on a production machine.
- Do not run these on systems you cannot recover. Back up registry/system first.
# README for My Playbook

## Overview
This playbook is designed to automate various system configurations, including registry modifications and management of APPX packages. It provides a structured approach to applying changes across multiple systems.

## Project Structure
The project is organized as follows:

```
my-playbook
├── playbook.conf          # Metadata for the playbook
├── README.md              # Documentation for the project
├── playbooks              # Directory containing playbook YAML files
│   ├── main.yml          # Entry point for the playbook
│   └── appx.yml          # APPX package management tasks
├── inventories            # Directory for inventory-related YAML files
│   └── registry.yml      # Inventory for registry modifications
├── roles                  # Directory for role-based tasks
│   └── appx              # Role for managing APPX packages
│       ├── tasks
│       │   └── main.yml  # Main tasks for the appx role
│       ├── defaults
│       │   └── main.yml  # Default variables for the appx role
│       └── handlers
│           └── main.yml  # Handlers for the appx role
├── group_vars             # Directory for group variable files
│   └── all.yml           # Variables applicable to all hosts
└── host_vars              # Directory for host-specific variable files
    └── host1.yml         # Variables specific to host1
```

## Usage
1. **Configuration**: Modify the `playbook.conf` file to set the metadata for your playbook.
2. **Execution**: Use the `main.yml` file in the `playbooks` directory as the entry point to execute the playbook.
3. **Registry Modifications**: The `registry.yml` file in the `inventories` directory contains tasks for modifying registry settings.
4. **APPX Management**: The `appx.yml` file in the `playbooks` directory manages APPX packages, including installation and removal.

## Requirements
- Ensure you have the necessary permissions to modify system settings.
- Review the tasks defined in the YAML files to understand their impact.

## Contributing
Feel free to contribute to this playbook by adding new tasks or improving existing ones. Please ensure that any changes are well-documented.

## License
This project is licensed under the MIT License. See the LICENSE file for details.