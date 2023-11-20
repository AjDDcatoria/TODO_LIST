from datetime import datetime
class DeadlineTracker:
    def __init__(self, task):
        self.task = task

    def calculate_days_left(self):
        """
        Calculate the days left for each task's deadline and update the array.
        """
        for t in self.task:
            deadline_str = t[2]
            deadline = datetime.strptime(deadline_str, "%m-%d-%Y").date()
            current_date = datetime.now().date()
            days_left = (deadline - current_date).days
            t[2] = days_left
    
    def merge_sort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            self.merge_sort(left_half)
            self.merge_sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i][2] < right_half[j][2]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1

    def sort_by_days_left(self):
        """
        Sort the task array based on remaining days left.
        """
        self.calculate_days_left()
        self.merge_sort(self.task)

    def get_task(self):
        """
        Get the current state of the task array.
        """
        return self.task
