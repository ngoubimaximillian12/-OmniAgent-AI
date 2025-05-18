def build_prompt(agent_name, task, context=None, memory=None):
    """
    Creates a standard prompt for any agent using consistent structure.
    """
    base = f"You are {agent_name.replace('Agent', '').lower()} assistant.\n"
    base += f"Task:\n{task.strip()}\n\n"

    if context:
        base += f"Context:\n{context.strip()}\n\n"

    if memory:
        if isinstance(memory, list):
            memory_block = "\n".join(memory)
        else:
            memory_block = memory
        base += f"Relevant Memory:\n{memory_block.strip()}\n\n"

    base += "Please respond with precision and clarity."
    return base
