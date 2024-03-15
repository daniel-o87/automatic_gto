#!/bin/bash

sleep 0.5
# Save the current workspace name
current_workspace=$(i3-msg -t get_workspaces | jq -r '.[] | select(.focused==true).name')

# Switch to workspace 6, adjust the sleep as needed
i3-msg workspace 6
#sleep 1 # Wait for the workspace to be fully visible

python pot_size.py

# Switch back to the original workspace
i3-msg workspace "$current_workspace"

python predict_client.py river.png
