import subprocess

def main():
    command = "uvicorn infra.http.server:app --reload"
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    main()
