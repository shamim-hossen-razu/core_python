#!/bin/bash

# Running a command in the background
sleep 10 &

# Getting the PID of the last background process
bg_pid=$!
echo "Background process PID: $bg_pid"

# Waiting for a background process to finish
wait $bg_pid
echo "Background process finished"

# Using jobs command
sleep 5 &
jobs

# Bringing a job to the foreground
fg %1
