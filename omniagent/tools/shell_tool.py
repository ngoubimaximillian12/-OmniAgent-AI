import subprocess

def run_shell_command(command: str, timeout: int = 10) -> str:
    """
    Runs a shell command in a subprocess and returns output.

    Args:
        command (str): The shell command to execute
        timeout (int): Seconds before auto-kill

    Returns:
        str: Captured stdout and stderr
    """
    try:
        result = subprocess.run(
            command,
            shell=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout
        )

        output = result.stdout.strip()
        error = result.stderr.strip()

        if result.returncode != 0:
            return f"❌ Error:\n{error or 'Command failed'}"
        return output or "✅ Command executed successfully (no output)."

    except subprocess.TimeoutExpired:
        return "⏰ Timeout: Command took too long to execute."
    except Exception as e:
        return f"🚫 Exception: {str(e)}"
