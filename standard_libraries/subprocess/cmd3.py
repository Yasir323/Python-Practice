import subprocess

try:
    completed = subprocess.run(["false"],
                                capture_output=True,
                                text=True, shell=True,
                                check=True) # With this we don't have to explicitly check for error codes.

    print("args", completed.args)
    print("returncode", completed.returncode)
    print("stderr", completed.stderr)   # Returns the errors
    print("stdout", completed.stdout)   # If we're captutring any output
except subprocess.CalledProcessError as ex:
    print(ex)
