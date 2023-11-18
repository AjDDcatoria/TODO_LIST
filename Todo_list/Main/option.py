def add_task():
    # TODO : Code to add Task from the database 🔨
    print('\t - Add Tasks -\n')
    task_name = input(' Title       : ')
    description = input(' Description : ')
    deadline = input(' Deadline    : ')
    return '\n\t  Task Added ✔️'


def remove_task():
    # TODO : Code to remove the task from the database 🔨
    print('\t- Remove Tasks -\n')
    return '\t  Task Remove ✔️'


def display_task():
    # TODO : Code to display the task from the database 🔨
    return 'displayTask'


def mark_task():
    # TODO :Code to mark the task from the database / edit 🔨
    return 'markTask'


def update_task():
    # TODO :Code to update or change the value of a task in the database 🔨
    return 'updateTask'


def default():
    return 'Not in the options. Please try again!'
