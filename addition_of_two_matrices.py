# Program to add two matrices
import sys
import logging

log_format = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="addition_of_two_matrices.log",
                    level=logging.INFO,
                    format=log_format,
                    datefmt="%d/%m/%y %I:%M:%S:%p")


class AddingTwoMatrices:
    """
    This class for addition of Two Matrices
    """
    def __init__(self, first_matrix, second_matrix):
        """
        defind Constructor method to initialize instance variables
        """
        self.first_matrix = first_matrix
        self.second_matrix = second_matrix

    def adding_two_matrices(self):
        result_matrix = []
        for rows in range(len(self.first_matrix)):
            row = []
            for colm in range(len(self.first_matrix[0])):
                row.append(self.first_matrix[rows][colm]
                           + self.second_matrix[rows][colm])
            result_matrix.append(row)
        print("Addition of two Matrix is: ")
        logging.info("Request processing completed !")
        print(*result_matrix, sep='\n')


logging.info("A new request came !")
try:
    first_matrix_rows = int(
        input("Enter the Number of rows you need in First Matrix : "))
    first_matrix_colums = int(
        input("Enter the Number of Columns you need in First Matrix : "))

except Exception as massage:
    print("Please enter correct rows and colums 'It Must Be Number' onlys")
    logging.exception(massage)
    sys.exit()

else:
    print("Enter the elements of First Matrix:")
    # using list comprehension
    first_matrix = [[int(
        input()) for matrix_colum in range(
        first_matrix_colums)] for matrix_row in range(first_matrix_rows)]
    print("First Matrix is :")
    for element in first_matrix:
        print(element)
try:
    second_matrix_rows = int(
        input("Enter the Number of rows you need in Second Matrix : "))
    second_matrix_colums = int(
        input("Enter the Number of Columns you need in Second Matrix : "))

    if (first_matrix_rows != second_matrix_rows) and (
            first_matrix_colums != second_matrix_colums):
        print(
            "Sorry! addition of two matrices is not possible only if two matrices have same order! ")
        logging.warning("addition of two matrices is not possible !..")
        sys.exit()

except Exception as massage:
    print("Please enter correct rows and colums 'It Must Be Number' onlys")
    logging.exception(massage)
    sys.exit()

else:
    print("Enter the elements of Second Matrix:")
    second_matrix = [[int(input()) for matrix_colum in range(
        second_matrix_colums)] for matrix_row in range(second_matrix_rows)]
    print("Second Matrix is: ")
    for element in second_matrix:
        print(element)


# first_matrix = [[12,7,3],
#                 [4,5,6],
#                 [7,8,9]]
# second_matrix = [[5,8,1],
#                  [6,7,3],
#                  [4,5,9]]

reference = AddingTwoMatrices(first_matrix, second_matrix)
reference.adding_two_matrices()

#
