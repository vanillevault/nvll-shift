# 🕵️‍♂️ NVLL-SHIFT — Sistema de Cifrado NodeSpectre

**NVLL-SHIFT** es un sistema de cifrado ligero, táctico y personalizable, creado por Vanille para proteger comunicaciones sensibles dentro del entorno operativo de **NodeSpectre**.  
Inspirado en cifrados tipo César, pero adaptado con lógica de alfabeto dinámico y desplazamientos inteligentes.

---

## 🔐 Características

- 🔑 Cifrado por desplazamiento con alfabeto generado a partir de una clave base
- 🧩 Compatible con letras y números (modo operativo/logístico)
- 🛡️ Ideal para ocultar órdenes, tokens, claves y rutas en texto plano
- 📎 Dos scripts: `nvll_encrypt.py` y `nvll_decrypt.py`

---

## ⚙️ Instalación

Solo necesitas Python 3:

bash
git clone https://github.com/vanillevault/nvll-shift.git
cd nvll-shift


---

🧪 Uso

➤ Cifrado

python nvll_encrypt.py "FASE 1 INICIA" NODESPECTRE2025 7

Salida:

Mensaje cifrado: MCZL 8 VSPJHR


---

➤ Descifrado

python nvll_decrypt.py "MCZL 8 VSPJHR" NODESPECTRE2025 7

Salida:

Mensaje descifrado: FASE 1 INICIA


---

🧠 Lógica Interna

El alfabeto se genera con la clave base eliminando duplicados y completando con el resto del alfabeto y números:

VANILLE2025 → VANILE2025BCDFGHJKMOQRTSUXYZ01346789

Luego se aplica un desplazamiento circular sobre ese alfabeto:

Cifrado → índice + shift

Descifrado → índice - shift




---

🚨 Advertencia

Este sistema no reemplaza cifrados modernos como AES o GPG, pero es ideal para camuflaje táctico en textos abiertos o públicos. Se puede usar para:

Enviar órdenes a través de cartas, headers HTTP, scripts o notas

Activar módulos secretos por palabra clave

Verificar autenticidad de mensajes camuflados



---

🔥 Ejemplo real (mensaje interceptado):

Mensaje cifrado: BYK4VB3YK
Clave: NODESPECTRE2025
Shift: 7
→ Resultado: CLAVICULA


---

🧩 Autor

Desarrollado por Vanille para operaciones de nodo oculto, defensa, evasión y mensajería segura en entornos observados.


---

NVLL-SHIFT
"El cifrado de los que no necesitan ocultarse… solo ser entendidos por quien debe."
