"""Helper utilities for phial."""
import re
from typing import Dict, List, Optional

from phial.wrappers import Message


def parse_help_text(help_text: str) -> str:
    """Parse help text."""
    NEW_LINE_SEPERATOR = "<__NEW_LINE_SEPERATOR__>"

    # Strip excess whitespace
    help_text = help_text.strip()

    # Remove single new lines
    help_text = help_text.replace("\n", NEW_LINE_SEPERATOR)
    help_text = help_text.replace(NEW_LINE_SEPERATOR * 2, "\n")
    help_text = help_text.replace(NEW_LINE_SEPERATOR, "")

    # Remove extra spaces
    help_text = re.sub(r'(^[ \t]+|[ \t]+)', ' ', help_text, flags=re.M)

    return help_text


def parse_slack_output(slack_rtm_output: List[Dict]) -> Optional['Message']:
    """Parse Slack output."""
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if(output and 'text' in output):
                bot_id = None
                team = None
                if 'team' in output:
                    team = output['team']
                if 'bot_id' in output:
                    bot_id = output['bot_id']

                return Message(output['text'],
                               output['channel'],
                               output['user'],
                               output['ts'],
                               team,
                               bot_id)
    return None
