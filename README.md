# VeeamChallenge

# Folder Synchronization Program

This program is designed to synchronize two folders: source and replica. The goal is to maintain a full, identical copy of the source folder in the replica folder.

## Implementation

The solution to this task should be implemented using Python. Ensure that the synchronization is one-way, with the content of the replica folder modified to exactly match the content of the source folder. Synchronization should be performed periodically.

## Requirements

- **One-Way Synchronization:** The synchronization is one-way, ensuring that the replica folder's content is modified to exactly match the content of the source folder.

- **Periodic Synchronization:** Synchronization should be performed periodically to keep the replica folder up-to-date with the source folder.

- **Logging:** All file creation, copying, and removal operations must be logged. The logs should be directed to both a file and the console output.

- **Command Line Arguments:** The program should accept command line arguments for the following parameters:
  - Source folder path
  - Replica folder path
  - Synchronization interval
  - Log file path

- **Dependency Usage:** While it is undesirable to use third-party libraries specifically for folder synchronization, the use of external libraries implementing other well-known algorithms is allowed and recommended. For example, using third-party or built-in libraries for MD5 calculations is acceptable.

## Usage

To run the program, use the following command line arguments:

```bash
python3 sync_folders.py --source_folder /path/to/source --replica_folder /path/to/replica --interval 60 --log_file /path/to/log.txt
```

This script will synchronize the source and replica folders every 60 seconds and log file operations to the specified log file.
