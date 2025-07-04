import os
import time
import subprocess

# === Configuration ===
ENABLE_TRACE = False  # True to enable TRACE defense; False to run without defense

# Paths and filenames
SERVER_EXEC = "../libmodbus-2.9.3/tests/.libs/unit-test-server"
CLIENT_SCRIPT = "../exp.py"
GDB_SCRIPT = "../TRACE_CFI.py" if ENABLE_TRACE else "../baseline.py"
GDB_COMMAND = "tracecfi" if ENABLE_TRACE else "baseline"
GDB_SIGNAL = "gdb_ready.signal"
SUCCESS_KEYWORD = "success"


def clean_up():
    """Remove old signal files if any."""
    if os.path.exists(GDB_SIGNAL):
        os.remove(GDB_SIGNAL)


def launch_gdb_server():
    """Launch the target server under GDB."""
    print("🚀 Launching GDB with TRACE_CFI..." if ENABLE_TRACE else "🚀 Launching GDB without TRACE...")

    gdb_cmd = [
        "gdb", "-q", SERVER_EXEC,
        "-ex", f"source {GDB_SCRIPT}",
        "-ex", GDB_COMMAND
    ]
    return subprocess.Popen(gdb_cmd)

def main():
    clean_up()

    gdb_proc = launch_gdb_server()
    gdb_proc.wait()

    print("✅ Experiment completed.")


if __name__ == "__main__":
    main()


