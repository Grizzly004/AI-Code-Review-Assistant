import json
from openai import OpenAI # Или Google GenerativeAI

client = OpenAI(api_key="sk-...")

def analyze_chunk(diff_text, mr_title, mr_desc):
    system_prompt = "...(Текст из пункта 2 выше)..."
    
    user_content = f"""
    TITLE: {mr_title}
    DESCRIPTION: {mr_desc}
    DIFF:
    {diff_text}
    """

    response = client.chat.completions.create(
        model="gpt-4o", # Или gemini-1.5-pro (у Gemini больше контекстное окно)
        response_format={"type": "json_object"}, # Гарантирует валидный JSON
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content}
        ],
        temperature=0.2 # Низкая температура для строгости и детерминированности
    )

    try:
        return json.loads(response.choices[0].message.content)
    except json.JSONDecodeError:
        return {"reviews": [], "general_summary": "Ошибка парсинга ответа AI"}
