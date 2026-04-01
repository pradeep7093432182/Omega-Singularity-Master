import os
import subprocess
import sys
import json

class TricoreBridge:
      def __init__(self, adb_path="D:\\Android\\Sdk\\platform-tools\\adb.exe"):
                self.adb_path = adb_path
                self._check_adb()

      def _check_adb(self):
                if not os.path.exists(self.adb_path):
                              print(f"Error: adb not found at {self.adb_path}")
                              sys.exit(1)

            def run_adb_command(self, args):
                      cmd = [self.adb_path] + args
                      try:
                                    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
                                    return result.stdout.strip()
except subprocess.CalledProcessError as e:
            print(f"ADB Error: {e.stderr}")
            return None

    def get_devices(self):
              output = self.run_adb_command(["devices"])
              devices = []
              if output:
                            lines = output.splitlines()[1:]  # skip header
            for line in lines:
                              if line.strip():
                                                    parts = line.split()
                                                    devices.append({'id': parts[0], 'status': parts[1]})
                                        return devices

    def pull_termux_cli(self, destination):
              # Assumes the user has copied the files to a shared location like /sdcard/Download
              target = "/sdcard/Download/gemini_cli"
        print(f"Attempting to pull Gemini CLI from {target} on Android device...")
        return self.run_adb_command(["pull", target, destination])

if __name__ == "__main__":
      print("Initializing Tri-Core Network Bridge...")
    bridge = TricoreBridge()
    devices = bridge.get_devices()
    print("Connected Devices:", json.dumps(devices, indent=2))

    # Initialize workspace
    workspace = "D:\\antigravity"
    if not os.path.exists(workspace):
              os.makedirs(workspace)
        print(f"Created workspace at {workspace}")

    print("Awaiting sync command for Termux Gemini CLI...")
