import os
from openai import OpenAI
import json

# --- НАСТРОЙКИ ---
API_KEY = "sk-..."  # Вставьте сюда ваш ключ OpenAI
# Если используете Gemini, код инициализации будет чуть другим, но логика та же.

client = OpenAI(api_key=API_KEY)

# --- НАШ СИСТЕМНЫЙ ПРОМПТ (из предыдущего шага) ---
SYSTEM_PROMPT = """
# РОЛЬ
Ты — Senior Software Engineer. Твоя специализация: поиск архитектурных ошибок, уязвимостей безопасности и проблем с производительностью.

# ТВОИ ЗАДАЧИ
Найти ПОТЕНЦИАЛЬНЫЕ баги. ИГНОРИРУЙ форматирование (пробелы, отступы).

# КАТЕГОРИИ ПОИСКА
1. Security: SQL Injection, Secrets, IDOR.
2. Performance: Memory leaks, N+1, O(n^2).
3. Robustness: Empty try/except.

# ФОРМАТ ОТВЕТА (JSON)
{
  "reviews": [
    {
      "line_number": integer, 
      "severity": "CRITICAL" | "WARNING",
      "message": "Описание проблемы (RU)",
      "code_suggestion": "Исправленный код"
    }
  ],
  "general_summary": "Вердикт"
}
"""

def test_code_review():
    # 1. Читаем плохой код
    with open("bad_code.py", "r") as f:
        code_content = f.read()

    print("⏳ Отправляем код на анализ...")

    # 2. Формируем запрос
    user_prompt = f"""
    TITLE: Fix logging and user fetch
    DESCRIPTION: Added function to get user and process logs.
    DIFF:
    {code_content}
    """

    # 3. Вызов API
    response = client.chat.completions.create(
        model="gpt-4o", # Или gpt-3.5-turbo / gpt-4-turbo
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.1
    )

    # 4. Вывод результата
    result = response.choices[0].message.content
    parsed = json.loads(result)
    
    print("\n--- 🤖 РЕЗУЛЬТАТ РЕВЬЮ ---")
    print(json.dumps(parsed, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    test_code_review()
