#!/bin/bash

# A simple system information script

print_system_info() {
    echo "System Information:"
    echo "==================="
    echo "Hostname: $(hostname)"
    echo "OS: $(uname -s)"
    echo "Kernel Version: $(uname -r)"
    echo "Uptime: $(uptime -p)"
    echo "CPU: $(lscpu | grep 'Model name' | cut -f 2 -d ":")"
    echo "Memory: $(free -h | awk '/^Mem:/ {print $2}')"
    echo "Disk Usage: $(df -h / | awk '/\// {print $5}')"
}

print_system_info > system_info.txt
echo "System information has been saved to system_info.txt"
