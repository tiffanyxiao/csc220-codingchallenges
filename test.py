
"""
A pythonic example of solving the subset sum problem in pseudo polynomial time
via dynamic programming.
"""

def positiveSubsetSum( A, x ):
    # preliminary
    if x < 0 or x > sum( A ): # T = sum(A)
      return False

    # algorithm
    sub_sum = [False] * ( x + 1 )
    sub_sum[0] = True
    p = 0
    while not sub_sum[x] and p < len( A ):
      a = A[p]
      q = x
      while not sub_sum[x] and q >= a:
        if not sub_sum[q] and sub_sum[q - a]:
          sub_sum[q] = True
        q -= 1
      p += 1
    return sub_sum[x]

def main():
    """
    A simple test demonstrating the application of the subset_sum function
    to a list of integers.
    """
    values = [1,2,3]
    target_sum = 100
    result = positiveSubsetSum(values, target_sum)
    print ('The set %s %s a subset sum of %d.' % \
          (str(values), 'has' if result else 'does not have', target_sum))

if __name__ == '__main__':
    main()
