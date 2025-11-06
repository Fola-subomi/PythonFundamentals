from tkinter import Tk, filedialog, messagebox
import tkinter as tk
# --- ASSUMPTION: This is the actual function you want to call ---
from Filesorter import sort_files_by_extension 
# ---------------------------------------------------------------

# Initialize directory variables
source_dir = ""
target_dir = ""

def select_source_folder():
    """Opens the file dialog to select the source folder."""
    global source_dir
    selected_path = filedialog.askdirectory(title="Select Source Folder (Files to be sorted)")
    if selected_path:
        source_dir = selected_path
        # Update the label to show the selected path (showing only the last folder name)
        source_label.config(text=f"Source: .../{source_dir.split('/')[-1]}", fg="blue")
    
def select_target_folder():
    """Opens the file dialog to select the target folder."""
    global target_dir
    selected_path = filedialog.askdirectory(title="Select Target Folder (Where sorted files will go)")
    if selected_path:
        target_dir = selected_path
        # Update the label to show the selected path (showing only the last folder name)
        target_label.config(text=f"Target: .../{target_dir.split('/')[-1]}", fg="blue")

def run_sort_operation():
    """Checks if directories are selected and runs the actual sorting logic."""
    if source_dir and target_dir:
        try:
            # --- The actual function call, replacing the placeholder ---
            result = sort_files_by_extension(source_dir, target_dir) 
            # -----------------------------------------------------------

            # Display the result using a message box and update the status label
            messagebox.showinfo("Sort Complete", result)
            result_label.config(text="✅ Sorting finished successfully!", fg="green")
            
        except Exception as e:
            # Catch any errors during the sorting process (e.g., permission issues)
            messagebox.showerror("Error", f"An error occurred during sorting: {e}")
            result_label.config(text="❌ Error during sort operation.", fg="red")
            
    else:
        # Prompt the user if one or both folders haven't been selected
        messagebox.showwarning("Missing Folder", "Please select both the Source and Target folders.")
        result_label.config(text="⚠️ Select both folders to start.", fg="orange")


# --- GUI Setup ---
root = tk.Tk()
root.title("Simple File Sorter")
root.geometry("350x270")
root.resizable(False, False)

# 1. Source Folder Selection
tk.Button(root, text="Select SOURCE Folder", command=select_source_folder).pack(pady=(10, 2))
source_label = tk.Label(root, text="Source: Not selected", fg="gray")
source_label.pack()

# 2. Target Folder Selection
tk.Button(root, text="Select TARGET Folder", command=select_target_folder).pack(pady=(10, 2))
target_label = tk.Label(root, text="Target: Not selected", fg="gray")
target_label.pack()

# Separator
tk.Frame(root, height=1, bg="lightgray").pack(fill='x', padx=10, pady=10)

# 3. Run Button
tk.Button(root, text="🚀 START SORTING", command=run_sort_operation, 
          bg="#4CAF50", fg="white", activebackground="#45a049",
          font=('Arial', 10, 'bold')).pack(pady=5)

# 4. Result/Status Label
result_label = tk.Label(root, text="")
result_label.pack(pady=5)


# Run the main event loop
root.mainloop()