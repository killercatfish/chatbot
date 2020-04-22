
log_length = 0
previous_length = 0
with open('/Applications/tmp/mylog.txt', 'r') as file:
    lines = file.readlines()
    log_length = len(lines)
    previous_length = log_length
    # print("length: " + str(log_length))
    # print("last line: " + lines[len(lines)-1])

while True:
    with open('/Applications/tmp/mylog.txt', 'r') as file:
        lines = file.readlines()
        log_length = len(lines)
        if log_length > previous_length:
            lines_to_check = log_length - previous_length
            previous_length = log_length
            print("**** " + str(lines_to_check) + " lines added: ")
            for i in range(lines_to_check):
                print(lines[len(lines)-i-1])
 