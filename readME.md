# Run commands
brew install uv
uv init
uv add playwright pytest
.venv/bin/playwright install
.venv/bin/pytest test_task1.py

git status
