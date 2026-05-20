#!/usr/bin/env python3
import datetime
import os


def get_log_file():
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    date_str = datetime.datetime.now().strftime("%Y-%m-%d")
    return os.path.join(log_dir, f"workspace_{date_str}.log")


def log(message, level="INFO"):
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    formatted_message = f"[{timestamp}] [{level}] {message}"
    print(formatted_message)

    with open(get_log_file(), "a") as f:
        f.write(formatted_message + "\n")


def info(message):
    log(message, "INFO")


def error(message):
    log(message, "ERROR")


def success(message):
    log(message, "SUCCESS")


def warn(message):
    log(message, "WARNING")
