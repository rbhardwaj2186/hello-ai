# hello-ai
A small Python system-check tool for my AI workstation (**Marine-AI**).

## What it shows
- Python version and CPU architecture
- CPU core count and Windows version
- Free space on the AI data drive

## Built with
- Python 3.15 and [uv] (https://docs.astral.sh/uv/)
- [rich] (https://github.com/Textualize/rich) for terminal tables
- Runs natively on **Windows 11 Arm64** (Nvidia RTX Spark)

## Run it
    uv sync
    uv run hello-ai
