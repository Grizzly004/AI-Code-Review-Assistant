{
  "reviews": [
    {
      "line_number": 5,
      "severity": "CRITICAL",
      "message": "Обнаружен хардкод секретного ключа (AWS_SECRET_KEY). Это серьезная уязвимость безопасности.",
      "code_suggestion": "AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')"
    },
    {
      "line_number": 13,
      "severity": "CRITICAL",
      "message": "Уязвимость SQL Injection. Использование f-строк для формирования SQL-запросов небезопасно.",
      "code_suggestion": "cursor.execute(\"SELECT * FROM users WHERE id = ?\", (user_id,))"
    },
    {
      "line_number": 23,
      "severity": "WARNING",
      "message": "Чтение всего файла в память (f.read()) может привести к OOM (Out Of Memory) на больших файлах.",
      "code_suggestion": "for line in f:  # Итерируйтесь по файлу построчно"
    },
    {
      "line_number": 31,
      "severity": "WARNING",
      "message": "Пустой блок except подавляет все ошибки, что затрудняет отладку.",
      "code_suggestion": "except Exception as e:\n    logger.error(f'Error processing logs: {e}')"
    }
  ],
  "general_summary": "Код содержит критические уязвимости безопасности (SQLi, Hardcoded secrets) и проблемы с производительностью. Требуется серьезная доработка перед мержем."
}
