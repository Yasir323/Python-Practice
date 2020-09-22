import subprocess

# subprocess.call
# subprocess.check_call
# subprocess.check_output
# The above 3 are old methods to create an instance of
# subprocess.Popen() class. A newer and better way is to use
# subprocess.run

completed = subprocess.run(["dir"],capture_output=True, text=True, shell=True)
# print(type(completed))
print("args", completed.args)
print("returncode", completed.returncode)   # Returns non zero value in case of an error
print("stderr", completed.stderr)   # Returns the errors
print("stdout", completed.stdout)   # If we're captutring any output

