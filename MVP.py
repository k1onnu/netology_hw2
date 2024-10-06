def create_pairs(boys,girls):
    if len(boys) != len(girls):
        return "Someone will be without a partner"

    boys.sort()
    girls.sort()

    pairs = []

    for boy, girl in zip(boys, girls):
        pairs.append(f"{boy} and {girl}")
    return "Perfect pairs:\n" + "\n".join(pairs)

boys1 = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls1 = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

result_1 = create_pairs(boys1,girls1)
print(result_1+"\n")


boys2 = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael']
girls2 = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

result_2 = create_pairs(boys2, girls2)
print(result_2 + "\n")
