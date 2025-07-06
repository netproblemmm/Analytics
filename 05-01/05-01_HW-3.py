# Lesson_01: HW_3
from typing import List, Dict

def calc_income_by_year(dates: List[str], incomes: List[int]) -> Dict[str, int]:
    income_by_year = {}

    for date, income in zip(dates, incomes):
        year = date.split('-')[0]
        income_by_year[year] = income_by_year.get(year, 0) + income
    return income_by_year

print(calc_income_by_year(['2021-11-01', '2021-12-15', '2020-11-30'], [100, 200, 150]))