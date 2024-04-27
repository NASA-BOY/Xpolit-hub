
def create_proper_msg(command: str, params: list):
    params.insert(0, command)
    return params

