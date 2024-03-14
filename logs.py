import re
def processar_logs(log_file: str)-> None:
    with open(log_file, "r") as file:
        log_data = file.read()
        
    sucesso = len(re.findall(r'200', log_data))
    
    falhas = len(re.findall(r'500', log_data))
    print(f"Solicitações bem-sucedidas: {sucesso}")
    print(f"Solicitações falhas: {falhas}")
    
if __name__ == "__main__":
    log_file = "server_logs.txt"
    processar_logs(log_file)
