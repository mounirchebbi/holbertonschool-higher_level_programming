import os

def generate_invitations(template, attendees):
    # Check input types
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Handle empty template
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # Handle empty attendees list
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        # Get values or 'N/A' if missing or None
        name = attendee.get("name") or "N/A"
        event_title = attendee.get("event_title") or "N/A"
        event_date = attendee.get("event_date") or "N/A"
        event_location = attendee.get("event_location") or "N/A"

        # Replace placeholders in template
        personalized = template.replace("{name}", name)\
                               .replace("{event_title}", event_title)\
                               .replace("{event_date}", event_date)\
                               .replace("{event_location}", event_location)

        # Write to output file
        try:
            filename = f"output_{index}.txt"
            with open(filename, 'w') as file:
                file.write(personalized)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
