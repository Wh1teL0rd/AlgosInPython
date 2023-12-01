from src.lab6.naive_method import naive_method

haystack = "THIS IS A TEST TEXT"
needle = "TEST"
result, comparisons = naive_method(haystack, needle)

if result != -1:
    print(f"Знайдено за позначенням {result}. Кількість порівнянь: {comparisons}")
else:
    print("Підстрічка не знайдена.")
