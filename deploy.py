import subprocess
import sys

def run_interactive_command(command):
    process = subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        bufsize=1,
        universal_newlines=True
    )
    
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output.strip())
            sys.stdout.flush()
    
    rc = process.poll()
    return rc

if __name__ == '__main__':
    COMMAND="rsync -avzuP /Users/yishai/Documents/direct-a.cn/public/ tencent-app:/var/www/hugo/"
    run_interactive_command(COMMAND)
