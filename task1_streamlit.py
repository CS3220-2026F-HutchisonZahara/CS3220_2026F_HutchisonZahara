import streamlit as st
from src.CSPclass import CSP

colleagues = ["A", "B", "C", "D", "E"]
chairs = [1, 2, 3, 4, 5, 6]
conflicts = [("A", "B"), ("B", "E"), ("B", "C")]

dinnerDomains = {}
for person in colleagues:
    dinnerDomains[person] = list(chairs)

dinnerNeighbors = {}
for person in colleagues:
    others = []
    for other in colleagues:
        if other != person:
            others.append(other)
    dinnerNeighbors[person] = others

def adjacentChairs(x, y):
    difference = abs(x - y)
    if difference == 1:
        return True
    if difference == len(chairs) - 1:
        return True
    return False

def isConflict(X, Y):
    if (X, Y) in conflicts:
        return True
    if (Y, X) in conflicts:
        return True
    return False

def dinnerConstraints(X, x, Y, y):
    if x == y:
        return False
    conflict = isConflict(X, Y)
    if conflict:
        adjacent = adjacentChairs(x, y)
        if adjacent:
            return False
    return True

def firstUnassigned(assignment):
    for person in colleagues:
        if person not in assignment:
            return person
    return None

def backtrack(csp, assignment, steps):
    if len(assignment) == len(colleagues):
        return assignment
    person = firstUnassigned(assignment)
    for chair in chairs:
        conflictCount = csp.nconflicts(person, chair, assignment)
        if conflictCount == 0:
            csp.assign(person, chair, assignment)
            steps.append([dict(assignment), person + " sits in chair " + str(chair), "seat"])
            result = backtrack(csp, assignment, steps)
            if result is not None:
                return result
            csp.unassign(person, assignment)
            steps.append([dict(assignment), person + " leaves chair " + str(chair) + " (dead end)", "remove"])
        else:
            steps.append([dict(assignment), person + " can't sit in chair " + str(chair), "reject"])
    return None

def recordSteps():
    dinnerCSP = CSP(colleagues, dinnerDomains, dinnerNeighbors, dinnerConstraints)
    steps = []
    backtrack(dinnerCSP, {}, steps)
    return steps

def personInChair(chair, assignment):
    for person in assignment:
        if assignment[person] == chair:
            return person
    return None

def main():
    st.title("Dinner Accommodation Problem")
    st.write("Backtracking search seating A, B, C, D, E around a table with 6 chairs.")
    st.write("A despises B, B argues with E, and C is B's manager, so B can't sit next to A, E or C.")

    steps = recordSteps()
    stepNumber = st.slider("Step", 1, len(steps), 1)
    step = steps[stepNumber - 1]
    assignment = step[0]
    message = step[1]
    kind = step[2]

    if kind == "seat":
        st.success("Step " + str(stepNumber) + ": " + message)
    elif kind == "reject":
        st.error("Step " + str(stepNumber) + ": " + message)
    else:
        st.warning("Step " + str(stepNumber) + ": " + message)

    layout = [[None, 1, None], [6, "table", 2], [5, "table", 3], [None, 4, None]]
    for row in layout:
        cols = st.columns(3)
        for i in range(3):
            cell = row[i]
            with cols[i]:
                if cell == "table":
                    st.info("TABLE")
                elif cell is not None:
                    person = personInChair(cell, assignment)
                    if person is None:
                        st.write("Chair " + str(cell) + ": empty")
                    else:
                        st.success("Chair " + str(cell) + ": " + person)

    st.write("Current assignment:", assignment)
    if stepNumber == len(steps):
        st.write("All 5 colleagues are seated with no conflicts.")

main()
