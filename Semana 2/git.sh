# Comandos para iniciar un repositorio Git y clonar uno existente.

# Inicializa un nuevo repositorio.
git init

# Clona un repositorio remoto.
git clone https://github.com/usuario/repositorio.git

# Verifica que Git este instaado.
git --version


# comandos para la movilización y manipulación de archivos.

# Lista archivos en el directorio.
ls

# Cambiar al directorio del repositorio.
cd nombre-del-repositorio

# Crear un nuevo archivo.
touch archivo.html

# Abrir VS Code en este directorio.
code .

# comandos de tracking y control de versiones.

# Añadir archivo específico.
git add archivo.html

# Añadir todos los cambios.
git add .

# Añadir todos los cambios excepto un archivo específico.
# (Nota: los espacios en el nombre del archivo deben ser escapados o entre comillas.
git add --all -- ":!/ruta/con espacios/nombre archivo.txt"

# Hacer commit con mensaje.
git commit -m "Agrego archivo inicial con HTML base"

# Hacer commit directo de cambios a archivos ya registrados.
git commit -am "Actualizo contenido del archivo principal"

# Ver estado del repositorio.
git status

# Ver historial de commits.
git log

# Subir y sincronizar cambios con el repositorio remoto.

# Enviar cambios a GitHub.
git push origin main

# Obtener cambios del repositorio remoto.
git pull origin main


# Comandos para crear y gestionar ramas.

# Ver rama actual.
git branch

# Crear y moverse a una nueva rama.
git checkout -b nueva-funcionalidad

# Cambiar de rama.
git checkout main

# Fusionar otra rama a la actual.
git merge nueva-funcionalidad


# comandos para gestionar conflictos y resolverlos.

# Ver conflictos después de merge
# (El conflicto se mostrará en el archivo editado con <<<<<<<, =======, >>>>>>>)

# Aceptar versión actual en VS Code (ejemplo)
# Clic en "Accept Current Change" o "Accept Incoming Change"

# Resetear a commit anterior (cuidado: elimina cambios)
git reset --hard <hash-del-commit>

# Resetear a la última versión del servidor
git reset --hard origin/main
