# Python
Python specific recommendations and tools.

# Setup Python

## Python Version
Current recommended Python version is 3.9.13

Windows 64-bit Installer: https://www.python.org/ftp/python/3.9.13/python-3.9.13-amd64.exe

Download Location for Other OS: https://www.python.org/downloads/release/python-3913/

## Python Installation Option
Recommended to use user specific Python installation instead of global Python installation, unless its really needed. This is to avoid messing other folks default Python version that they may use.

You can check if you have a default Python installation by using below command in command prompt:
`python --version`

If you don't have a default Python version in your system, enable "Add Python to Path" checkbox. If you already have a default Python version installed in your system, skip adding the path.

# IDE
Recommended IDE is VS Code.

Download Link: https://code.visualstudio.com/download​

## Recommended VS Code Extensions
Recommended vscode extensions are available in the file [.vscode/extensions.json](.vscode/extensions.json)

To view the recommended extensions in vscode:

    1. Open current folder in vscode.
    2. Type '@recommended' in the search bar.
    3. The recommended extensions will be listed under 'Workspace Recommendations'

# Dependency Management
Recommended dependency management tool for Python is Poetry.

Refer to [Poetry Getting Started docs](getting_started_docs/poetry_getting_started.md).

# Unit Testing
Recommended unit testing library for Python is pytest. 