#### there are M students and N mango bags having P numbers of mangoes in each bag need to 
### distribute mangoes evenly to the students  using python program

def distribute_mangoes(M, N, P):
    total_mangoes = N * P  # Calculate total number of mangoes
    mangoes_per_student = total_mangoes // M  # Calculate mangoes per student

    if mangoes_per_student == 0:
        print("Not enough mangoes to distribute evenly.")
    else:
        remaining_mangoes = total_mangoes % M  # Calculate remaining mangoes
        print("Each student gets", mangoes_per_student, "mangoes.")

        if remaining_mangoes > 0:
            print("There are", remaining_mangoes, "mangoes left.")
        else:
            print("All mangoes are distributed evenly.")

# Input values
M = int(input("Enter the number of students: "))
N = int(input("Enter the number of mango bags: "))
P = int(input("Enter the number of mangoes in each bag: "))

# Distribute mangoes
distribute_mangoes(M, N, P)
