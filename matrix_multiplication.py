# Program to multiplication two matrices
import sys
import logging

log_format = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="multiplication_of_two_matrices.log",
                    level=logging.INFO,
                    format=log_format,
                    datefmt="%d/%m/%y %I:%M:%S:%p")


class MatricesMultiplication:

    """
    This class for multiplication of Two Matrices
    """
    def __init__(self, first_matrix, second_matrix):
        """
        defind Constructor method to initialize instance variables
        """
        self.first_matrix = first_matrix
        self.second_matrix = second_matrix

    def multiplication_of_two_matrice(self):

        responce = []
        result_matrix = []
        for element_a in range(len(self.first_matrix)):
            for element_b in range(len(self.second_matrix[0])):
                sums = 0
                for element_c in range(len(self.second_matrix)):
                    sums = sums+(self.first_matrix[element_a][element_c]
                                 * self.second_matrix[element_c][element_b])
                responce.append(sums)
            result_matrix.append(responce)
        responce = []
        print("Multiplication of two Matrix is: ")
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

    if first_matrix_colums != second_matrix_rows:
        print(
             '''Sorry! multiplication of two matrices is not 
            possible please enter correct input ''')
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

reference = MatricesMultiplication(first_matrix, second_matrix)
reference.multiplication_of_two_matrice()

#
