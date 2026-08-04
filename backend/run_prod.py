import os
import uvicorn

if __name__ == "__main__":
    print("=============================================")
    print("   MindBridge Production Backend Runner      ")
    print("=============================================")

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
