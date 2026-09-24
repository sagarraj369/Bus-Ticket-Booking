import subprocess
import sys

print("1.py")
subprocess.run([sys.executable, "1.py"])
print("=========================================================================================")
print("demo.py")

subprocess.run([sys.executable, "2.py"])

print("Both programs completed!")