#!/bin/bash

# Subshell
(
    cd /tmp
    echo "Current directory in subshell: $(pwd)"
)
echo "Current directory in main shell: $(pwd)"

# Here document
cat << EOF > output.txt
This is a multi-line
text block that will be
written to output.txt
EOF

# Traps
cleanup() {
    echo "Cleaning up..."
    # Add cleanup code here
}
trap cleanup EXIT

# Intentional exit to trigger cleanup
exit 0
