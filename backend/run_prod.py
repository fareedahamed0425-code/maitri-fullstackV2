import importlib.util
import os
import subprocess
import sys
from pathlib import Path

import uvicorn


def ensure_runtime_dependencies() -> None:
    """Install the production requirement set automatically if critical imports are missing."""
    base_dir = Path(__file__).resolve().parent
    req_file = base_dir / "requirements.render.txt"
    if not req_file.exists():
        return

    required_modules = ["fastapi", "uvicorn", "sqlalchemy", "numpy", "soundfile", "openai", "dotenv"]
    missing = [name for name in required_modules if importlib.util.find_spec(name) is None]

    if not missing:
        return

    print(f"[RUNNER] Missing runtime dependencies detected: {', '.join(missing)}")
    print("[RUNNER] Attempting automatic dependency bootstrap...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--no-cache-dir", "-r", str(req_file)])
        print("[RUNNER] Dependency bootstrap completed successfully.")
    except Exception as exc:
        print(f"[RUNNER] Dependency bootstrap failed: {exc}")


if __name__ == "__main__":
    print("=============================================")
    print("   MindBridge Production Backend Runner      ")
    print("=============================================")

    ensure_runtime_dependencies()

    port = int(os.getenv("PORT", "8000"))
    workers = 1

    print(f"[RUNNER] Starting single Uvicorn worker on port {port}.")
    print("[RUNNER] Using conservative settings to stay within Render memory limits.")

    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=port,
        workers=workers,
        timeout_keep_alive=60,
        log_level="info"
    )
