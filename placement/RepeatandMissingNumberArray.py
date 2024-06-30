class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        n = len(A)
        sum_of_numbers = 0
        sum_of_squares = 0
        
        for i in range(n):
            sum_of_numbers += A[i]
            sum_of_squares += A[i] * A[i]
        
        # Calculate the expected sums
        expected_sum = n * (n + 1) // 2
        expected_sum_of_squares = (n * (n + 1) * (2*n + 1)) // 6
        
        # Calculate the differences
        diff_sum = sum_of_numbers - expected_sum
        diff_sum_of_squares = sum_of_squares - expected_sum_of_squares
        
        # Calculate A and B
        B = (diff_sum_of_squares - diff_sum * diff_sum) // (2 * diff_sum)
        A = diff_sum + B
        
        return [A, B]