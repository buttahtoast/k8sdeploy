#!/usr/bin/env python3
"""Returns a ansible inventory with groups defined in ENV("STAGES")"""
import json
import os
import sys

## -- Default Variables
HOST="localhost"
DEFAULT={
    "_meta": {
        "hostvars": {
            str(HOST): {
                "ansible_connection": "local"
            }
        }
    },
    "all": {
        "children": [
        ]
    }
}

## -- Check Evnironment Stages
if os.getenv("STAGES"):
    for stage in os.getenv("STAGES").split(","):
        # Add children
        DEFAULT["all"]["children"].append(stage.strip())
        # Add group
        DEFAULT.update({str(stage.strip()): { str("hosts"): [str(HOST)]}})
else:
    print("'STAGES' not defined in your Environment")
    sys.exit(1)

print(json.dumps(DEFAULT))
