import subprocess as sub

def NMAP():
    # Get IP address from the user
    IP = input("Enter IP address: ")

    # Run the WSL command
    try:
        sub.run(
            ["wsl", "sudo", "nmap", IP, "-sV", "-O", "-p1-65535", "-Pn"], 
            check=True,
            text=True
        )
    except sub.CalledProcessError as e:
        print(f"An error occurred: {e}")
