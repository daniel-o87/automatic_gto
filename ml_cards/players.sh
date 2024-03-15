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

for item in 1.png 2.png 3.png 4.png 5.png 6.png 7.png; do
	python predict_client.py "$item"
done
