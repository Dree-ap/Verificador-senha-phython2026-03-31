import re

def avaliar_forca_senha(senha):
    """
    Avalia a força de uma senha e retorna o status, cor e dicas de melhoria.
    """
    forca = 0
    resumo = []

    # Validações independentes
    if len(senha) >= 8:
        forca += 1
    else:
        resumo.append("- Mínimo de 8 caracteres")

    if re.search(r"[A-Z]", senha):
        forca += 1
    else:
        resumo.append("- Pelo menos uma letra maiúscula")

    if re.search(r"[a-z]", senha):
        forca += 1
    else:
        resumo.append("- Pelo menos uma letra minúscula")

    if re.search(r"\d", senha):
        forca += 1
    else:
        resumo.append("- Pelo menos um número")

    if re.search(r"[!@#$%&*()_+=\-]", senha):
        forca += 1
    else:
        resumo.append("- Pelo menos um símbolo (!@#$%&*)")

    # Retorno das avaliações
    if forca == 5:
        return "Resultado: MUITO FORTE", "green", resumo
    elif forca >= 3:
        return "Resultado: MÉDIA", "orange", resumo
    else:
        return "Resultado: FRACA", "red", resumo