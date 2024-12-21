### uv stater project
https://docs.astral.sh/uv/

#### 0. Install uv
```bash
# See pack-uv.py for more
 tdp i plugin/uv_0.5.11_linux_amd64.tar.gz
```
#### 1. Init
```bash
uv init uv-starter
cd uv-starter
```

#### 2. Add Dependency
```bash
uv add ruff
```

#### 3. Declaring script dependencies
https://docs.astral.sh/uv/guides/scripts/#declaring-script-dependencies

See example.py
```bash
uv run example.py
```


#### 4. Add tools globally
https://docs.astral.sh/uv/getting-started/features/#tools
```bash
uv tool add ruff
```
#### 4.1 Add tools locally
```bash
uv add --dev ruff
```

https://docs.astral.sh/uv/guides/integration/pytorch/

#### 5.1 Use PyTorch with CPU
```bash
uv sync --extra cpu
uv run main.py
```

#### 5.2 Use PyTorch with GPU
```bash
uv sync --extra cuda124
uv run main.py
```

#### 6. Install Different Python versions
https://docs.astral.sh/uv/getting-started/features/#python-versions
```bash
uv python install 3.8. 3.9 3.10 3.11 3.11 3.12 3.13
```

https://github.com/astral-sh/ruff

#### 7. Lint
```bash
ruff check
# or with fix
ruff check --fix
```

### 8. Format
```bash
ruff format
```