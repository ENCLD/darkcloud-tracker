# FPV_AI

YOLO26 detector for FPV drones and payloads, trained with [Ultralytics](https://docs.ultralytics.com/).

Classes: `0: payload`, `1: drone`

## Quick start (Windows)

Requirements: [Python 3.12](https://www.python.org/downloads/) and an NVIDIA GPU with an up-to-date driver (CPU works, but is slow).

```powershell
git clone <this repo>
cd FPV_AI
powershell -ExecutionPolicy Bypass -File setup.ps1   # one time: creates .venv and installs everything
.venv\Scripts\python.exe train.py                    # train (50 epochs)
```

Results are written to `runs/detect/train-N/`. The trained model is `runs/detect/train-N/weights/best.pt`.

`train.py` options: `--epochs`, `--batch` (lower it if you run out of GPU memory), `--imgsz`, `--model`.

## Using the trained model

The current trained model is included in the repo: `runs/detect/train-3/weights/best.pt`.

```powershell
.venv\Scripts\yolo.exe predict model=runs/detect/train-3/weights/best.pt source=path\to\image_or_video
```

## Dataset

`dronetraining/` holds the training images and YOLO-format labels (`images/train`, `labels/train`).
To add data, put new images in `images/train` with a matching `.txt` label file in `labels/train`.
