import os
import shutil

def sort_files_by_extension(source_directory, target_directory):
    """
    Sorts files from the source_directory into subdirectories in the target_directory
    based on their file extensions.

    :param source_directory: Directory containing files to be sorted.
    :param target_directory: Directory where sorted files will be placed.
    """
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    for filename in os.listdir(source_directory):
        file_path = os.path.join(source_directory, filename)
        
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1][1:]  # Get extension without dot
            if not file_extension:  # Handle files without extension
                file_extension = 'no_extension'
            
            extension_directory = os.path.join(target_directory, file_extension)
            if not os.path.exists(extension_directory):
                os.makedirs(extension_directory)
            try:
                shutil.move(file_path, os.path.join(extension_directory, filename))
            except Exception as e:
                print(f"Error moving {filename}: {e}")

            moved_count = 0
            destination_path = os.path.join(extension_directory, filename)

            if os.path.exists(destination_path):
                base, ext = os.path.splitext(filename)
                new_filename = f"{base}_copy{ext}"
                destination_path = os.path.join(extension_directory, new_filename)
                shutil.move(file_path, destination_path)

    for filename in os.listdir(source_directory):
        moved_count += 1
        
    return f"{moved_count} files sorted successfully {target_directory}." 

