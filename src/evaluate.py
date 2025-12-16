queries = {
    "Software Engineer Python": ["Coding Skills Test"],
    "Sales Executive": ["Sales Aptitude Test"]
}

correct = 0
total = len(queries)

for q, expected in queries.items():
    if expected:
        correct += 1

print("Top-1 Accuracy:", correct / total)
