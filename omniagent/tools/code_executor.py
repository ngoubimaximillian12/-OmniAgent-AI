import io
import sys
import contextlib
import traceback


def execute_python_code(code: str) -> str:
    """
    Executes a string of Python code and captures the stdout output.

    Args:
        code (str): Python code snippet to execute.

    Returns:
        str: Captured output or error trace.
    """
    output_stream = io.StringIO()

    try:
        with contextlib.redirect_stdout(output_stream):
            exec(code, {"__name__": "__main__"})  # Executes in isolated scope
        return output_stream.getvalue()
    except Exception as e:
        error_msg = traceback.format_exc()
        return f"❌ Error during execution:\n{error_msg}"
    finally:
        output_stream.close()
