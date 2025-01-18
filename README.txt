Task Manager Application

Purpose:
The -Task Manager Application- is a simple desktop-based tool designed to help users manage their tasks efficiently. The application uses a graphical user interface (GUI) built with Python's tkinter library, making it user-friendly and accessible.

Features:
- Add Task: Create new tasks by specifying the task name, due date, status, and priority.
- Modify Task: Edit the details of any existing task.
- Delete Task: Remove any task from the list permanently.
- Sort Tasks: Sorting and filtering the tasks by task name, due date, priority or status.
- Task List: View all tasks in a tabular format with columns for name, due date, status, and priority.
- Persistent Storage: Save tasks to a local 'tasks.json' file, ensuring tasks are retained between application sessions.
- Interactive Calendar: Select due dates easily using a calendar widget.

Setup Instructions:

Prerequisites:
1. Python Installation: Ensure Python 3.7 or higher is installed on your system, you can download Python from Python official website.
2. Dependencies:
- Install the required Python libraries using pip: pip install tkcalendar.
- The 'tasks.json' file must exist in the application directory, if it is deleted or corrupted, the application will create a new empty file.

Running the Application:
1. Download the Source Code: Download the project folder into a local directory, then extract it.
2. Run the Application: Navigate to the directory containing the source code and execute the following command: python main.py
3. Using the GUI: The Task Manager window will appear. Use the input fields and buttons to manage tasks.
