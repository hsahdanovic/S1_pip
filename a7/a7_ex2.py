import os
import shutil

def organize_directory(src_path: str):
    organized = f"{src_path}_organized"
    log = os.path.join(organized, "move.log")

    try:
        if not os.path.isdir(src_path):
            os.makedirs(organized, exist_ok=True)
            with open(log, "w", encoding="utf-8") as log:
                log.write(f"Error: '{src_path}' is not a valid directory.\n")
            return

        os.makedirs(organized, exist_ok=True)

        with open(log, "w", encoding="utf-8") as l:
            for root, _, files in os.walk(src_path):
                for file in files:
                    path = os.path.join(root, file)
                    extention = os.path.splitext(file)[1].lstrip(".").lower()

                    if extention == "":
                        extention = "no_extension"

                    ext = os.path.join(organized, extention)
                    os.makedirs(ext, exist_ok=True)
                    newPath = os.path.join(ext, file)
                    shutil.move(path, newPath)
                    l.write(f"Copied '{path}' to '{newPath}'\n")


    except Exception as e:
        os.makedirs(organized, exist_ok=True)
        with open(log, "w", encoding="utf-8") as log:
            log.write(f"Error: {str(e)}\n")

organize_directory("a7_ex2_dir")
organize_directory("missing_dir")
