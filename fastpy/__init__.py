import sys

def numseqs(file_name, qora):
    qora = qora.lower()
    if qora == "a":
        header = ">"
    elif qora == "q":
        header = "@"
    else:
        sys.exit("must be q or a, you put %s" % qora)

    with open(file_name, "r") as f:
        count = 0

        for line in f:
            if line.strip()[0] == ">":
                count += 1

    return count

def headers(file_name, qora):
    qora = qora.lower()
    if qora == "a":
        header = ">"
    elif qora = "q":
        header = "@"
    else:
        sys.exit("must be q or a, you put %s" % qora)

    with open(file_name, "r") as f:
        headers = []

        for line in f:
            line = line.strip()

            if line[0] == header:
                headers.append(line)

    return headers

def detect(file_name):
    with open(file_name, "r") as f:
        first = f.readline().strip()

        if first[0] == ">":
            return "a"
        elif first[0] == "@":
            return "q"
        else:
            return None



