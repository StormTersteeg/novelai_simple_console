context = ""
context_base = ""

def get_context(context_file):
    try:
        with open("context/" + context_file, "r") as f:
            return f.read()
    except FileNotFoundError:
        return ""

def save_context(context_file):
    global context

    with open("context/" + context_file, "w") as f:
        f.write(context)

def add_to_context(prompt, max_context_size):
    global context
    
    context += prompt + "\n"
    context = context[-max_context_size:]