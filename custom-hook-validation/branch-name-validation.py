#!/usr/bin/env python3
import re
import sys
import subprocess

# Função para obter o nome da branch atual
def get_current_branch_name():
    # Executa o comando git para obter o nome da branch atual
    result = subprocess.run(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # Verifica se o comando foi executado com sucesso
    if result.returncode != 0:
        print("Error: Unable to get current branch name")
        sys.exit(1)
    # Retorna o nome da branch atual, removendo espaços em branco extras
    return result.stdout.decode('utf-8').strip()

# Função para validar o nome da branch
def validate_branch_name(branch_name):
    # Define o padrão de expressão regular para validar o nome da branch
    pattern = r'^(feature|bugfix|hotfix|release|docs|chore)/[a-z0-9._-]+$'
    # Verifica se o nome da branch corresponde ao padrão
    if not re.match(pattern, branch_name):
        print(f"Error: Branch name '{branch_name}' is invalid. It must follow the pattern (feature|bugfix|hotfix|release|docs|chore) 'type/description'. Use git branch -M to rename the branch.")
        sys.exit(1)

# Bloco principal do script
if __name__ == "__main__":
    # Obtém o nome da branch atual
    branch_name = get_current_branch_name()
    # Valida o nome da branch
    validate_branch_name(branch_name)
    # Se o nome da branch for válido, o script termina sem erros