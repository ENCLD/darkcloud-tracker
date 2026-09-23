# One-time setup: creates .venv with Python 3.12 and installs the training dependencies.
# Usage (from the repo folder):  powershell -ExecutionPolicy Bypass -File setup.ps1
$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

if (-not (Test-Path ".venv")) {
    Write-Host "Creating virtual environment (.venv) with Python 3.12..."
    py -3.12 -m venv .venv
    if ($LASTEXITCODE -ne 0) { throw "Python 3.12 not found. Install it from https://www.python.org/downloads/ and re-run." }
}

$python = ".venv\Scripts\python.exe"
& $python -m pip install --upgrade pip
& $python -m pip install -r requirements.txt
if ($LASTEXITCODE -ne 0) { throw "Installing requirements failed." }

& $python -c "import torch; print('PyTorch', torch.__version__, '| CUDA GPU available:', torch.cuda.is_available())"
Write-Host ""
Write-Host "Setup done. Start training with:  .venv\Scripts\python.exe train.py"
