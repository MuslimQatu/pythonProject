# std_name: Muslim Ismail Al-Qatu
# std_id: XXXXXX

import tkinter as tk
from task_manager import TaskManager

def main():
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()

if __name__ == "__main__":
    main()
