readiness_status = "complete"
participant_count_text = "4"
participant_count = int(participant_count_text)
next_checkpoint = participant_count + 1

print(f"Readiness: {readiness_status}")
if participant_count >= 4:
    print(f"Participant count: {participant_count}")
    print(f"Next checkpoint: {next_checkpoint}")
