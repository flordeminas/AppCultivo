import os
import time
import subprocess
import datetime

# CONFIGURAÇÕES
file_to_watch = r"c:\Projetos\ZHC\App\strains_database.xlsx"
script_to_run = r"c:\Projetos\ZHC\App\update_all.py"

def get_mtime():
    try:
        if "~$" in file_to_watch: return 0
        return os.path.getmtime(file_to_watch)
    except OSError:
        return 0

def start_watch():
    print(f"👀 VIGILANTE PRO V3 ATIVO: Monitorando '{os.path.basename(file_to_watch)}'...")
    last_mtime = get_mtime()
    
    while True:
        current_mtime = get_mtime()
        
        # Se detetarmos mudança (planilha salva)
        if current_mtime != last_mtime and current_mtime > 0:
            now = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"[{now}] 📝 Mudança detectada! Dando tempo para o Excel terminar de salvar...")
            
            # ESPERAR 5 SEGUNDOS (Diferença fundamental!)
            # Isso garante que o Excel solte o arquivo completamente.
            time.sleep(5)
            
            success = False
            for attempt in range(3):
                try:
                    # Roda o sincronismo
                    subprocess.run(["python", script_to_run], check=True, capture_output=True, text=True)
                    print(f"[{now}] ✅ App atualizado com sucesso!")
                    success = True
                    break
                except Exception as e:
                    print(f"[{now}] ⚠️ Tentativa {attempt+1} - Excel ocupado. Retentando em breve...")
                    time.sleep(3)
            
            if not success:
                print(f"[{now}] ❌ Erro Crítico: Sincronismo falhou (Planilha travada).")
            
            last_mtime = current_mtime
            
        time.sleep(3) # Verificação menos frenética

if __name__ == "__main__":
    start_watch()
