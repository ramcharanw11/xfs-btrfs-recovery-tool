# dummy_generator.py
import random
from datetime import datetime, timedelta

file_types = [ "doc", "docx", "rtf", "pdf", "txt", "odt", "html", "xml", "ppt", "odp", "xls", "ods",
    "log", "csv", "tsv", "conf", "ini", "cfg", "zip", "tar", "rar", "iso", "rpm", "deb",
    "jpg", "jpeg", "png", "gif", "tif", "elf", "so", "a", "exe", "dll", "bat", "cmd",
    "ps", "ps1", "sh", "bash", "zsh", "py", "db" ]
statuses = ["Recovered", "Partially Recovered", "Corrupted"]
file_systems = ["xfs", "btrfs"]

def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

def generate_dummy_file(index):
    created = random_date(datetime(2023, 1, 1), datetime(2023, 6, 1))
    deleted = created + timedelta(days=random.randint(1, 90))
    file_type = random.choice(file_types)
    size = f"{random.randint(1, 12000)} KB" if random.random() < 0.8 else f"{round(random.uniform(0.5, 10.0), 1)} MB"
    return {
        "name": f"file_{index}.{file_type}",
        "type": file_type,
        "size": size,
        "created": created.strftime("%Y-%m-%d"),
        "deleted": deleted.strftime("%Y-%m-%d"),
        "status": random.choice(statuses),
        "fileSystem": random.choice(file_systems)
    }

def get_dummy_data(count=100):
    return [generate_dummy_file(i) for i in range(1, count + 1)]
