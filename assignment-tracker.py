import json
def save_assignments(Assignments):
    file =  open("Assignments.json","w")
    
    json.dump(Assignments,file)
    file.close()

    print("save")

def load_assignments():
    try:
        file = open("Assignments.json",'r')

        Assignments = json.load(file)

        file.close()

        return Assignments
    except:
        return []
    
def add_assignment(Assignments:list):
    subject = input("Subject Name: ")
    title = input("Assignment Title: ")
    due = input("Due Date: ")

    assignment = {
        "subject":subject,
        "title":title,
        "due":due,
        "done": False
    }

    Assignments.append(assignment)

    return Assignments



def view_assignments(Assignments: list[dict]):
    for i, assignment in enumerate(Assignments):
        print(f"{i+1}. [{assignment['subject']}] {assignment['title']} - Due: {assignment['due']} - Status: {'Done' if assignment['done'] else 'Pending'}")


def mark_as_done(Assignments):
    view_assignments(Assignments)
    choice = int(input("Enter the Assigment Number to be marked done "))

    Assignments[choice - 1]["done"] = True
    return f"Marked as done"

Assignments = load_assignments()

while True:
    print("\n----------------Assignment Tracker---------------")
    print("1. Add Assignment")
    print("2. View Assignments")
    print("3. Mark as Done")
    print("4. Quit")
    choice = input("Enter choice")

    if choice == "1":
        Assignments = add_assignment(Assignments)
    elif choice == "2":
        view_assignments(Assignments)
    elif choice == "3":
        mark_as_done(Assignments)
        save_assignments(Assignments)
    elif choice == "4":
        save_assignments(Assignments)
        break
    else:
        print("Invalid choice!")

