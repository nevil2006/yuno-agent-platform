import datetime


execution_logs = []


def save_log(query, result):

    log = {
        "query": query,
        "timestamp": str(
            datetime.datetime.now()
        ),
        "tokens_estimated": len(result.split()),
        "result_preview": result[:200]
    }

    execution_logs.append(log)


def get_logs():
    return execution_logs