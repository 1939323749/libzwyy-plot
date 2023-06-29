from mitmproxy import http
from datetime import datetime
def request(flow: http.HTTPFlow) -> None:
    token_header = "token"
    Cookie = "Cookie"
    token = flow.request.headers.get(token_header)
    cookie=flow.request.headers.get(Cookie)

    if token:
        with open("tokens.txt", "w") as token_file:
            token_file.write(f"{cookie} : token:{token}\n")