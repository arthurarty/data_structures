from collections import Counter


def processLogs(logs, threshold):
    trans_counter = Counter()
    for log in logs:
        send_id, recipient_id, amount = log.split()
        if send_id != recipient_id:
            trans_counter[send_id] += 1
            trans_counter[recipient_id] += 1
        else:
            trans_counter[send_id] += 1
    result = [key for key, value in trans_counter.items() if value >= threshold]
    result.sort()
    return result


print(processLogs(
    [
        "1 2 50",
        "1 7 70",
        "1 3 20",
        "2 2 17",
    ], 2))
