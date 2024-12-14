#!/bin/bash

echo "Liberando espaço no Linux..."

# Etapa 1: Identificar arquivos grandes
echo "Procurando arquivos grandes na partição /..."
find / -xdev -type f -size +100M 2>/dev/null | tee arquivos_grandes.txt
echo "Arquivos grandes encontrados foram salvos em 'arquivos_grandes.txt'. Avalie antes de excluir!"

# Etapa 2: Limpar caches do sistema
echo "Limpando caches do sistema..."
sudo sync
sudo sh -c "echo 3 > /proc/sys/vm/drop_caches"
echo "Caches limpos."

# Etapa 3: Limpar logs antigos
echo "Limpando logs antigos..."
sudo journalctl --vacuum-size=100M
sudo rm -rf /var/log/*.gz /var/log/*.1 /var/log/*.old
echo "Logs antigos removidos."

# Etapa 4: Limpar pacotes e dependências não utilizados
echo "Limpando pacotes não utilizados..."
sudo apt autoremove -y
sudo apt clean
echo "Pacotes e caches de pacotes limpos."

# Etapa 5: Verificar diretórios de lixo eletrônico
echo "Limpando diretórios de lixo eletrônico..."
rm -rf ~/.local/share/Trash/* ~/.cache/thumbnails/*
echo "Lixo eletrônico removido."

# Etapa 6: Opcional - Remover Snap antigo (se Snap estiver instalado)
if command -v snap &>/dev/null; then
  echo "Removendo versões antigas de pacotes Snap..."
  sudo snap list --all | awk '/disabled/{print $1, $3}' | while read -r snapname revision; do
    sudo snap remove "$snapname" --revision="$revision"
  done
  echo "Snaps antigos removidos."
fi

# Etapa 7: Relatório de uso de disco
echo "Relatório final do uso de disco:"
df -h /

echo "Processo concluído. Avalie as mudanças!"
