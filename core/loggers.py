def engineLog(msg: str):
    log("Engine", "+", message=msg)

def engineInfo(msg: str):
    log("Engine", "*", message=msg)

def engineErro(msg: str):
    log("Engine", "-", message=msg)

def bridgeLog(msg: str):
    log("Bridge", "+", message=msg)
    

def log(intanceName: str, market: str, message: str):
    print(f"[{intanceName}] ({market}) {message}")