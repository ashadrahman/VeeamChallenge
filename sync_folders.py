#!/usr/bin/env python3

import os
import shutil
import argparse
import time

def sync_folders(source_path, replica_path, log_file):
    # Ensure the replica folder exists
    if not os.path.exists(replica_path):
        os.makedirs(replica_path)

    # Iterate through the source folder
    for root, dirs, files in os.walk(source_path):
        for file in files:
            # Skip .DS_Store files
            if file == ".DS_Store":
                continue

            source_file_path = os.path.join(root, file)
            replica_file_path = os.path.join(replica_path, os.path.relpath(source_file_path, source_path))

            # Ensure the directory structure exists in the replica
            replica_dir = os.path.dirname(replica_file_path)
            if not os.path.exists(replica_dir):
                os.makedirs(replica_dir)

            # Copy or update files
            if not os.path.exists(replica_file_path) or os.path.getmtime(source_file_path) > os.path.getmtime(replica_file_path):
                shutil.copy2(source_file_path, replica_file_path)
                log(log_file, f"File Copied: {source_file_path} -> {replica_file_path}")

    # Remove files in replica that are not in source
    for root, dirs, files in os.walk(replica_path):
        for file in files:
            # Skip .DS_Store files
            if file == ".DS_Store":
                continue

            replica_file_path = os.path.join(root, file)
            source_file_path = os.path.join(source_path, os.path.relpath(replica_file_path, replica_path))

            if not os.path.exists(source_file_path):
                os.remove(replica_file_path)
                log(log_file, f"File Removed: {replica_file_path}")

def log(log_file, message):
    with open(log_file, 'a') as log_file:
        log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")
    print(message)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Synchronize two folders")
    parser.add_argument("source_path", help="Path to the source folder")
    parser.add_argument("replica_path", help="Path to the replica folder")
    parser.add_argument("interval", type=int, help="Synchronization interval in seconds")
    parser.add_argument("log_file", help="Path to the log file")

    args = parser.parse_args()

    source_path = args.source_path
    replica_path = args.replica_path
    interval = args.interval
    log_file = args.log_file

    while True:
        sync_folders(source_path, replica_path, log_file)
        time.sleep(interval)
