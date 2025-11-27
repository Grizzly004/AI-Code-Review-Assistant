user_message = f"""
ВОТ ДАННЫЕ MERGE REQUEST:

---
TITLE: {mr_title}
DESCRIPTION: {mr_description}
---

ВОТ ИЗМЕНЕНИЯ (GIT DIFF):
{diff_content}

Проанализируй этот код. Если замечаний нет, верни пустой список "reviews": [].
"""
