import paramiko

# Function to check sudo access on servers
def check_sudo_access(hostname, username, password):
    try:
        # Initialize SSH client
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Connect to server
        client.connect(hostname, username=username, password=password)
        
        # Execute sudo
        stdin, stdout, stderr = client.exec_command('sudo -l')

        # Input password
        stdin.write(f'{password}\n')
        stdin.flush()

        # Printoutput
        output = stdout.read().decode('utf-8')
        error = stderr.read().decode('utf-8')
        
        if output:
            print(f'SUDO access on {hostname}:\n{output}')
        if error:
            print(f'Error on {hostname}:\n{error}')
        
        client.close()
        
    except Exception as e:
        print(f"Failed to connect to {hostname}: {str(e)}")

# Function to load server IPs from a file
def load_servers(file_path):
    with open(file_path, 'r') as f:
        servers = [line.strip() for line in f if line.strip()]
    return servers

# Function to load credentials from a file
def load_credentials(cred_file):
    credentials = {}
    with open(cred_file, 'r') as f:
        for line in f:
            if line.strip():
                key, value = line.strip().split('=', 1)
                credentials[key.strip()] = value.strip()
    return credentials

# Main function
def main():
    # Get path to the server list and credentials file
    server_file = input("Enter the path to the server list file: ")
    cred_file = input("Enter the path to the credentials file: ")

    # Load servers and credentials
    servers = load_servers(server_file)
    credentials = load_credentials(cred_file)
    
    # Get login credentials from the loaded data
    username = credentials.get('username')
    password = credentials.get('password')

    if not username or not password:
        print("Error: Username or password not found in the credentials file.")
        return

    # Iterate over each server and check sudo access
    for server in servers:
        print(f"Checking sudo access on {server}...")
        check_sudo_access(server, username, password)

if __name__ == "__main__":
    main()