def clean_response(output: str, max_length: int = 1500):
    """
    Cleans and trims LLM output. Removes duplicate prompt echo, stray markdown, etc.
    """
    if not output:
        return "⚠️ No output returned."

    # Remove markdown artifacts
    if "```" in output:
        output = output.split("```")[-2] if len(output.split("```")) > 2 else output

    # Trim to safe length
    output = output.strip()
    if len(output) > max_length:
        output = output[:max_length] + "\n\n...(truncated)"
    return output
