def retry(action, retries=3):

    for _ in range(retries):
        try:
            return action()
        except Exception:
            pass

    raise Exception("Action failed")