tasks = [
    {"id": 1, "duration": 4, "deadline": 6, "penalty": 10},
    {"id": 2, "duration": 3, "deadline": 5, "penalty": 8},
    {"id": 3, "duration": 2, "deadline": 7, "penalty": 6},
]

def schedule(tasks):
    time = 0
    total_penalty = 0
    schedule = []

    for task in sorted(tasks, key=lambda x: x["deadline"]):
        time += task["duration"]
        lateness = max(0, time - task["deadline"])
        total_penalty += lateness * task["penalty"]
        schedule.append(task["id"])

    return schedule, total_penalty

if __name__ == "__main__":
    s, cost = schedule(tasks)
    print("Schedule:", s)
    print("Total penalty:", cost)
