def check(process_output, judge_output, data):
    for process_line, judge_line in zip(process_output.split('\n'), judge_output.split('\n')):
        process_line = process_line.split()
        judge_line = judge_line.split()
        if process_line != judge_line:
            return False
    return True
