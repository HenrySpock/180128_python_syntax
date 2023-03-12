def in_range(nums, lowest, highest):
    """Print numbers inside range.

    - nums: list of numbers
    - lowest: lowest number to print
    - highest: highest number to print

    For example:

      in_range([10, 20, 30, 40], 15, 30)

    should print:

      20 fits
      30 fits
    """
    for num in nums:
        if lowest <= num <= highest:
            print(f"{num} fits")


in_range([10, 20, 30, 40, 50], 15, 30)            
in_range([3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39], 15, 25)            
