import os

def get_files_info(working_directory, directory="."):
    try:
        full_path = os.path.join(working_directory, directory)
        abs_full = os.path.abspath(full_path)
        abs_work = os.path.abspath(working_directory)

        if not abs_full.startswith(abs_work):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(abs_full):
            return f'Error: "{directory}" is not a directory'

        entries = os.listdir(abs_full)
        lines = []
        for entry in entries:
            entry_path = os.path.join(abs_full, entry)
            is_dir = os.path.isdir(entry_path)
            size = os.path.getsize(entry_path)
            lines.append(f"- {entry}: file_size={size} bytes, is_dir={is_dir}")

        return "\n".join(lines)

    except Exception as e:
        return f"Error: {str(e)}"

