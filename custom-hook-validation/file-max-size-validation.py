#!/usr/bin/env python3
import sys
import os

# Constante para o número máximo de linhas padrão
DEFAULT_MAX_LINES = 500

# Função para validar o tamanho do arquivo
def validate_file_size(file_path, max_lines):
    # Abre o arquivo e lê todas as linhas
    with open(file_path, 'r') as file:
        lines = file.readlines()
        line_count = len(lines)
        # Verifica se o número de linhas excede o máximo permitido
        if line_count > max_lines:
            return (file_path, line_count, False)
        else:
            return (file_path, line_count, True)

# Função para processar os arquivos
def process_files(files, max_lines):
    # Valida o tamanho de cada arquivo na lista
    results = [validate_file_size(file_path, max_lines) for file_path in files if os.path.isfile(file_path)]
    return results

# Função principal do script
def main(args):
    max_lines = DEFAULT_MAX_LINES  # Valor padrão
    files = []

    # Processa os argumentos passados para o script
    for arg in args[1:]:
        if arg.startswith('--max-size='):
            max_lines = int(arg.split('=')[1])
        else:
            files.append(arg)

    # Verifica se há arquivos para processar
    if not files:
        print("Usage: validate_template_max_size.py [--max-size=<max_lines>] <files...>")
        return 0  # Não aborta o commit se nenhum arquivo for processado

    # Processa os arquivos e valida o tamanho
    results = process_files(files, max_lines)

    # Verifica se todos os arquivos são válidos
    all_valid = all(result[2] for result in results)
    for file_path, line_count, is_valid in results:
        if is_valid:
            print(f"File '{file_path}' is within the allowed size. It has {line_count} lines.")
        else:
            print(f"Error: File '{file_path}' exceeds the maximum allowed lines ({max_lines}). It has {line_count} lines.")

    # Retorna 0 se todos os arquivos forem válidos, caso contrário, retorna 1
    return 0 if all_valid else 1

# Bloco principal do script
if __name__ == "__main__":
    sys.exit(main(sys.argv))