
# Forward Chaining in Artificial Intelligence

# Initial facts
facts = {"A", "B"}

# Rules: IF conditions THEN conclusion
rules = [
    ({"A", "B"}, "C"),
    ({"C"}, "D"),
    ({"D"}, "E"),
    ({"A", "E"}, "F")
]

def forward_chaining(facts, rules):
    facts = set(facts)

    while True:
        new_fact_added = False

        for conditions, conclusion in rules:
            if conditions.issubset(facts) and conclusion not in facts:
                facts.add(conclusion)
                print("New fact derived:", conclusion)
                new_fact_added = True

        if not new_fact_added:
            break

    return facts


# Execute
result = forward_chaining(facts, rules)

print("\nFinal Facts:", result)
