# ПРИМЕРЫ (FEW-SHOT)

Пример 1 (Плохо - это делает линтер, игнорируй):
Input: "x = 1 " (лишний пробел)
Output: []

Пример 2 (Хорошо - Логическая ошибка):
Input Code:
def get_user(id):
  return db.execute(f"SELECT * FROM users WHERE id = {id}")

Output JSON:
{
  "reviews": [
    {
      "file_path": "api/users.py",
      "line_number": 12,
      "severity": "CRITICAL",
      "message": "Обнаружена SQL-инъекция. Использование f-строк в SQL запросах небезопасно.",
      "code_suggestion": "return db.execute('SELECT * FROM users WHERE id = ?', (id,))"
    }
  ]
}
