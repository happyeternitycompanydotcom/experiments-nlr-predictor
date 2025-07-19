# llm/idea_transformer.py

import subprocess

def run_ollama_prompt(prompt, model="mistral"):
    """
    Запускает локальную модель Ollama с заданным промптом.
    Требует установленного Ollama: https://ollama.com
    """
    try:
        result = subprocess.run(
            ["ollama", "run", model],
            input=prompt.encode("utf-8"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=20
        )
        output = result.stdout.decode("utf-8")
        return output
    except Exception as e:
        return f"⚠️ Ошибка вызова LLM: {e}"
