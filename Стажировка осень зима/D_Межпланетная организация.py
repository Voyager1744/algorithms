def calculate_language_barriers(N, languages, hierarchy):
    barriers = [0] * N  # Initialize language barriers to zero for all employees

    for i in range(N - 1, -1, -1):
        current_employee = i + 1
        language = languages[i]
        superior = hierarchy[i]

        if language != languages[superior]:
            barriers[current_employee - 1] = barriers[superior] + 1

    return barriers


# Read input
N = int(input())
languages = input().split()
hierarchy = list(map(int, input().split()))

# Calculate language barriers
barriers = calculate_language_barriers(N, languages, hierarchy)

# Print the result
print(*barriers)

# Не решена
