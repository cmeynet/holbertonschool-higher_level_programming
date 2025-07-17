"""
Function that generates personalized invitation files
from a template with placeholders and a list of objects.
"""
import os


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        raise TypeError("Template must be a string")
    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        raise TypeError("Attendees must be a list of dictionnaries")
    if not template.strip():
        raise ValueError("Template is empty, no output files generated.")
    if not attendees:
        raise ValueError("No data provided, no output files generated.")

    # Fields required
    placeholders = ["name", "event_title", "event_date", "event_location"]

    # Treatment of each participant
    for i, person in enumerate(attendees, start=1):
        try:
            message = template
            message = message.replace("{name}", str(person.get("name", "N/A") or "N/A"))
            message = message.replace("{event_title}", str(person.get("event_title", "N/A") or "N/A"))
            message = message.replace("{event_date}", str(person.get("event_date", "N/A") or "N/A"))
            message = message.replace("{event_location}", str(person.get("event_location", "N/A") or "N/A"))

            # Output file name
            filename = f"output_{i}.txt"

            # Avoid overwriting an existing file
            if os.path.exists(filename):
                print(f"File {filename} already exists.")
                continue

            # Write the message to the file
            with open(filename, "w", encoding="utf-8") as f:
                f.write(message)

        except Exception as e:
            return {'error': str(e)}
