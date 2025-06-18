import sys

print(sys.version)
print(sys.version_info)

if sys.version_info.major == 3 and sys.version_info.minor >= 14:
    print('This version of Python is OK.')
else:
    print('Please update your Python version.')

print(sys.executable)

for item in sys.path:
    print(item)