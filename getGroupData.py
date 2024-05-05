import json
import csv


def process_whatsapp_data(json_file, output_csv):
    # Load JSON data from a file
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Prepare to write to CSV
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['subject', 'subjectTime', 'user', 'isAdmin']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Process each record in the JSON data
        for record in data:
            if 'groupMetadata' in record:
                # Extract needed information
                subject = record['groupMetadata'].get('subject', '')
                subject_time = record['groupMetadata'].get('subjectTime', '')
                participants = record['groupMetadata'].get('participants', [])

                # Write each participant's data
                for participant in participants:
                    user = participant['id'].get('user', '')
                    is_admin = participant.get('isAdmin', False)
                    writer.writerow({
                        'subject': subject,
                        'subjectTime': subject_time,
                        'user': user,
                        'isAdmin': is_admin
                    })


# Usage of the function
# Replace 'path_to_your_json_file.json' with the actual path to your JSON file
# Replace 'output.csv' with the desired output CSV file name
process_whatsapp_data('whatsAppChatData.json', 'output.csv')
