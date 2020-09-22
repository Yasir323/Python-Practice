# To run another script
import subprocess

completed = subprocess.run(
    ["python", "subprocess/hello.py"], capture_output=True, text=True, shell=True)
print("args", completed.args)
# Returns non zero value in case of an error
print("returncode", completed.returncode)
print("stderr", completed.stderr)   # Returns the errors
print("stdout", completed.stdout)   # If we're captutring any output
