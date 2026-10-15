# Automação de Mensagens no WhatsApp com Python

Este é um mini projeto em Python desenvolvido para automatizar o envio de mensagens em massa (ou para uma lista de contatos) através do WhatsApp Web, utilizando as bibliotecas `pywhatkit` e `pyautogui`.

---

## 🚀 Tecnologias Utilizadas

* **Python 3.x**
* [PyWhatKit](https://pypi.org/project/pywhatkit/) - Biblioteca para automatizar interações com o WhatsApp Web.
* [PyAutoGUI](https://pypi.org/project/PyAutoGUI/) - Biblioteca para automação de interface gráfica (controlar o teclado e o mouse).

---

## ⚙️ Pré-requisitos

Antes de executar o script, certifique-se de que você possui:

1. **Python** instalado em sua máquina.
2. O navegador **Google Chrome** (ou outro navegador padrão) instalado.
3. Estar com o **WhatsApp Web** conectado no seu navegador padrão (a sessão precisa estar ativa para que o script consiga enviar as mensagens).

---

## 📦 Instalação

Abra o seu terminal ou prompt de comando e instale as bibliotecas necessárias executando o seguinte comando:

```bash
pip install pywhatkit pyautogui
```

---

## 📝 Como Usar

1. Baixe ou copie o código do arquivo `mensagem.py`.
2. Abra o arquivo em um editor de código (como VS Code).
3. Adicione os números de telefone desejados na lista `numbers`, utilizando o formato internacional (com o sinal de mais `+`, código do país, DDD e número). Exemplo:
   ```python
   numbers = ["+5511999999999", "+5521888888888"]
   ```
4. Altere o texto `"Mensagem a ser enviada"` para o conteúdo que deseja transmitir.
5. Execute o script no terminal:
   ```bash
   python mensagem.py
   ```

---

## ⚠️ Avisos Importantes

* **Uso consciente:** O WhatsApp possui políticas rígidas contra spam. O envio automatizado em massa para números desconhecidos pode resultar no banimento temporário ou permanente da sua conta. Use com responsabilidade.
* **Foco na tela:** Durante a execução, o `pyautogui` simulará o pressionamento da tecla `Enter`. Evite mexer no mouse ou no teclado enquanto o script estiver rodando para não interferir no envio.
* **Tempo de espera (`time.sleep`):** O tempo de 15 segundos entre as mensagens serve para dar tempo de carregar o WhatsApp Web e enviar a mensagem corretamente. Dependendo da velocidade da sua conexão, pode ser necessário aumentar esse valor.

---

## 📄 Licença

Este projeto é de código aberto e está sob a licença MIT. Sinta-se à vontade para modificar e melhorar!
