import shutil
import subprocess
import sys


def fetch_wget(url, output_file):
    # Get terminal width for proper progress bar sizing
    terminal_width = shutil.get_terminal_size().columns

    # Run wget with better progress formatting
    process = subprocess.Popen(
        ["wget", "--progress=bar:force", url, "-O", output_file],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1  # Line buffered for real-time output
    )

    print(f"Downloading: {url}")
    print("-" * terminal_width)

    for line in process.stdout:
        # Clean up the line
        clean_line = line.strip()

        # Only show progress lines (they contain % or data transfer info)
        if any(indicator in clean_line for indicator in ['%', 'K/s', 'M/s', 'KB/s', 'MB/s']):
            # Truncate if line is too long for terminal
            if len(clean_line) > terminal_width - 1:
                clean_line = clean_line[:terminal_width - 4] + "..."

            # Clear line and write progress
            sys.stdout.write("\r" + " " * (terminal_width - 1))
            sys.stdout.write("\r" + clean_line)
            sys.stdout.flush()

    process.wait()

    if process.returncode == 0:
        print("\n✓ Download complete!")
    else:
        print(f"\n✗ Download failed with exit code: {process.returncode}")

    return process.returncode == 0


fetch_wget(
    "https://huggingface.co/Phr00t/WAN2.2-14B-Rapid-AllInOne/resolve/main/v9/wan2.2-i2v-rapid-aio-nsfw-v9.2.safetensors",
    "test")
