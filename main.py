from datetime import date, timedelta

def get_birthdays_per_week(users):
    today = date.today()
    current_weekday = today.weekday()  # День тижня, де 0 - понеділок, 6 - неділя
    next_week = today + timedelta(days=(7 - current_weekday))  # Початок наступного тижня

    birthdays_per_week = {}  # Словник для зберігання днів народження

    for user in users:
        birthday = user["birthday"]
        if birthday < today:  # Якщо день народження вже минув у цьому році, враховуємо його наступного року
            birthday = birthday.replace(year=today.year + 1)

        days_until_birthday = (birthday - today).days
        if 0 <= days_until_birthday <= 6:  # День народження у цьому тижні
            day_of_week = (today + timedelta(days=days_until_birthday)).strftime('%A')
            if day_of_week not in birthdays_per_week:
                birthdays_per_week[day_of_week] = []
            birthdays_per_week[day_of_week].append(user["name"])

    # Переносимо дні народження з вихідними на наступний робочий день (понеділок)
    for day in ["Saturday", "Sunday"]:
        if day in birthdays_per_week:
            next_monday = next_week + timedelta(days=1)  # Наступний понеділок
            if "Monday" not in birthdays_per_week:
                birthdays_per_week["Monday"] = []
            birthdays_per_week["Monday"].insert(0, *birthdays_per_week.pop(day))
            print(next_monday)

    return birthdays_per_week

# Приклад використання функції
if __name__ == "__main__":
    today = date.today()
    users = [
        {
            "name": "John",
            "birthday": (today + timedelta(days=5)),
        },
        {
            "name": "Doe",
            "birthday": (today + timedelta(days=6)),
        },
        {"name": "Alice", "birthday": (today + timedelta(days=3))},
    ]

    birthdays = get_birthdays_per_week(users)
    print(birthdays)
