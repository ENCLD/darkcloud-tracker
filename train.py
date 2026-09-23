"""Train the drone/payload detector with the same settings as runs/detect/train-3.

Usage:
    .venv\\Scripts\\python.exe train.py              # 50 epochs, like the original run
    .venv\\Scripts\\python.exe train.py --epochs 10  # quicker test run
"""

import argparse
from pathlib import Path

import torch
from ultralytics import YOLO

ROOT = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--epochs", type=int, default=50)
    parser.add_argument("--batch", type=int, default=16, help="lower this if you run out of GPU memory")
    parser.add_argument("--imgsz", type=int, default=640)
    parser.add_argument("--model", default="yolo26n.pt", help="base model, downloaded automatically")
    args = parser.parse_args()

    device = 0 if torch.cuda.is_available() else "cpu"
    if device == "cpu":
        print("WARNING: no CUDA GPU found, training on CPU will be slow.")

    model = YOLO(args.model)
    model.train(
        data=str(ROOT / "dronetraining" / "data.yaml"),
        epochs=args.epochs,
        batch=args.batch,
        imgsz=args.imgsz,
        device=device,
        project=str(ROOT / "runs" / "detect"),
    )


if __name__ == "__main__":
    main()
