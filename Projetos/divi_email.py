import email

def dividir_email(mensagem):
    """
    Divide um email em suas partes principais.

    Args:
        mensagem: O email em formato de string.

    Returns:
        Um dicionário contendo o corpo, cabeçalho e anexos do email.
    """

    msg = email.message_from_string(mensagem)

    corpo = ""
    if msg.is_multipart():
        for parte in msg.walk():
            if parte.get_content_type() == "text/plain":
                corpo += parte.get_payload(decode=True).decode()
    else:
        corpo = msg.get_payload(decode=True).decode()

    cabecalho = {}
    for chave, valor in msg.items():
        cabecalho[chave] = valor

    anexos = []
    for parte in msg.walk():
        if parte.get("Content-Disposition") and parte.get_content_maintype() != "multipart":
            anexos.append({
                "nome": parte.get_filename(),
                "conteudo": parte.get_payload(decode=True),
                "tipo": parte.get_content_type()
            })

    return {
        "corpo": corpo,
        "cabecalho": cabecalho,
        "anexos": anexos
    }

# Exemplo de uso
mensagem = """
From: remetente@exemplo.com
To: destinatario@exemplo.com
Subject: Teste de email
Content-Type: multipart/mixed; boundary="--boundary--"

Este é o corpo do email.

--boundary--
Content-Type: text/plain
Content-Disposition: attachment; filename="arquivo1.txt"

Conteúdo do arquivo1.txt

--boundary--
Content-Type: application/pdf
Content-Disposition: attachment; filename="arquivo2.pdf"

Conteúdo do arquivo2.pdf

--boundary--
"""

partes = dividir_email(mensagem)
print(partes["corpo"])
print(partes["cabecalho"])
print(partes["anexos"])