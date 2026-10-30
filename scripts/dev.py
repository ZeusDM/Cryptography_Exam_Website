#!/usr/bin/env python3
"""
Zero-setup dev server for UW Cryptography Comprehensive Exam Site.
Watches problems/**/*.tex for changes, automatically updates Hugo content
in ~80ms, and live-reloads the browser via Hugo server.
"""

import sys
import time
import signal
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SITE_DIR = REPO_ROOT / "site"
import argparse
parser = argparse.ArgumentParser(description="Live dev server for Cryptography Exam Website")
parser.add_argument("--math-dir", default=None, help="Path to math repository or problems directory")
cli_args, remaining = parser.parse_known_args()
PROBLEMS_DIR = generate_site.resolve_problems_dir(cli_args.math_dir)

# Import generate_site module
sys.path.insert(0, str(REPO_ROOT / "scripts"))
import socket
import generate_site

def find_available_port(start_port=1313):
    port = start_port
    while port < start_port + 20:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(("127.0.0.1", port)) != 0:
                return port
        port += 1
    return start_port

def main():
    print("=" * 60)
    print(" UW Cryptography Comprehensive Exam - Live Dev Server")
    print("=" * 60)

    # 1. Initial build with cache
    print("[1/2] Generating site content from LaTeX...")
    cache = generate_site.load_cache()
    t0 = time.time()
    generate_site.main(cache=cache, quiet=False, problems_dir=PROBLEMS_DIR)
    print(f"      Initial build ready in {time.time() - t0:.2f}s\n")

    # 2. Start Hugo server
    port = find_available_port(1313)
    print(f"[2/2] Starting Hugo live development server on http://localhost:{port}/...")
    hugo_cmd = [
        "hugo", "server",
        "--source", str(SITE_DIR),
        "--bind", "0.0.0.0",
        "--port", str(port),
        "--navigateToChanged"
    ]
    
    hugo_proc = subprocess.Popen(hugo_cmd)

    def cleanup(sig=None, frame=None):
        print("\nStopping Hugo server and watcher...")
        hugo_proc.terminate()
        try:
            hugo_proc.wait(timeout=2)
        except subprocess.TimeoutExpired:
            hugo_proc.kill()
        sys.exit(0)

    signal.signal(signal.SIGINT, cleanup)
    signal.signal(signal.SIGTERM, cleanup)

    print("\nWatching problems/ for changes...")
    print("Edit any .tex file, and Hugo will automatically live-reload your browser!\n")

    # 3. File Watcher loop
    mtimes = {}
    for p in PROBLEMS_DIR.rglob("*.tex"):
        try:
            mtimes[p] = p.stat().st_mtime
        except Exception:
            pass

    try:
        while True:
            time.sleep(0.3)
            # Check if Hugo server crashed
            if hugo_proc.poll() is not None:
                print(f"[Error] Hugo server exited with code {hugo_proc.returncode}")
                break

            changed = False
            current_files = set(PROBLEMS_DIR.rglob("*.tex"))
            if set(mtimes.keys()) != current_files:
                changed = True
                mtimes = {p: p.stat().st_mtime for p in current_files}
            else:
                for p in current_files:
                    try:
                        mtime = p.stat().st_mtime
                        if mtime != mtimes.get(p):
                            mtimes[p] = mtime
                            changed = True
                            print(f"\n[Watcher] Detected edit: {p.relative_to(REPO_ROOT)}")
                    except Exception:
                        pass

            if changed:
                t_rebuild = time.time()
                generate_site.main(cache=cache, quiet=True, problems_dir=PROBLEMS_DIR)
                generate_site.save_cache(cache)
                elapsed = time.time() - t_rebuild
                print(f"[Watcher] Regenerated in {elapsed:.3f}s -> Hugo live-reloading browser...")
    except KeyboardInterrupt:
        cleanup()

if __name__ == "__main__":
    main()
