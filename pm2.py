import subprocess
flag = input("Enter 1 for stop, 2 for reload: ").strip()
dirs = ["brahamand","subvivah","foodfly","customerzone","tutorbuddy","connectflow"]

if flag == "1":
    action = "delete"
elif flag == "2":
    action = "reload"
else:
    raise SystemExit("Invalid choice")

for d in dirs:
    subprocess.run(f"cd /home/ubuntu/htdocs/{d} && pm2 {action} ecosystem.config.js", shell=True, check=True)