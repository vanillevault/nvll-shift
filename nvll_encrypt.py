
def generar_alfabeto(clave_base: str) -> str:
    base = ''.join(sorted(set(clave_base.upper()), key=clave_base.index))
    resto = ''.join([c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789' if c not in base])
    return base + resto

def cifrar_nvll(texto, clave_base, desplazamiento):
    abc = generar_alfabeto(clave_base)
    texto = texto.upper()
    resultado = ''
    for char in texto:
        if char in abc:
            idx = (abc.index(char) + desplazamiento) % len(abc)
            resultado += abc[idx]
        else:
            resultado += char
    return resultado

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Uso: python nvll_encrypt.py <mensaje> <clave_base> <desplazamiento>")
    else:
        mensaje = sys.argv[1]
        clave_base = sys.argv[2]
        desplazamiento = int(sys.argv[3])
        cifrado = cifrar_nvll(mensaje, clave_base, desplazamiento)
        print("Mensaje cifrado:", cifrado)
