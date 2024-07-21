"""Sort module"""


class BubbleSort:
    """Class for performing a bubble sort on a list"""

    # The Big O of this is O(N^2) - Time complexity
    # The Big O of this is O(1) - Space complexity

    def sort(self, sortable):
        """Sort list"""
        # Store length of the sortable list
        length = len(sortable)
        # Loop from 0 to length of list - 1 (highest index)
        for i in range(length):
            # Loop from 0 to length of list - 1 (highest index)
            for j in range(length):
                # Now have two different indexes into spots in the sortable list.
                # If the thing in the j spot is greater than the thing in the i spot,
                # we want to swap the elements.
                # NOTE: If we wanted descending order, we would use: sortable[i] > sortable[j]
                if sortable[i] < sortable[j]:
                    # Store the j item in a temp swap var
                    temp = sortable[j]
                    # Move the i item to the j spot
                    sortable[j] = sortable[i]
                    # Move the temp to the i spot now that its contents have been moved.
                    sortable[i] = temp
