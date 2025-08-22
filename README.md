# Sistema de Gestión de Documentos — Flask + MySQL (XAMPP)

Aplicación Flask con Jinja2 para gestionar documentos técnicos con autenticación y control de acceso por roles (administrador y trabajador).

## Requisitos
- Python 3.11+
- XAMPP (MySQL en 127.0.0.1:3306)

## Instalación
1) Crear entorno e instalar dependencias:
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2) Configurar variables (.env):
- Copiar `.env.example` a `.env` y editar:
```
SECRET_KEY=una-clave-segura
DATABASE_URL=mysql+pymysql://root:password@127.0.0.1:3306/hidrostal
UPLOAD_FOLDER=instance/uploads
```
Ajusta usuario/contraseña/host/puerto según tu XAMPP.

3) Crear base de datos y tablas en MySQL (XAMPP):
- Abre phpMyAdmin o una consola MySQL y ejecuta el contenido de:
`sql/schema.sql`
Esto creará la base `hidrostal`, tablas `users` y `documents`, e insertará un usuario admin.

4) Inicializar app y confirmar conexión:
```
python - <<'PY'
from app import create_app, db
app=create_app()
with app.app_context():
    db.engine.connect()
    print('Conexión MySQL OK')
PY
```

5) Ejecutar servidor:
```
python run.py
```
URL: `http://localhost:5000/login`

Credenciales admin iniciales (del SQL):
- usuario: `admin`
- contraseña: `Admin123!`

## Cómo funciona
- Autenticación: Flask-Login, formularios WTForms, contraseñas con hashing de Werkzeug.
- Roles: `admin` y `worker`.
  - admin: crear/editar/eliminar documentos y crear usuarios.
  - worker: ver y descargar documentos.
- Seguridad: CSRF, validación de PDFs, `secure_filename`, límite de tamaño, cabeceras CSP/anti-clickjacking.

## Estructura
```
app/
  __init__.py      # App factory, config, seguridad, blueprints
  models.py        # Modelos SQLAlchemy: User, Document
  auth.py          # Rutas de login/logout/registro (solo admin)
  main.py          # Dashboard y descargas
  admin.py         # CRUD de documentos (solo admin)
  static/
    img/           # Imágenes
    style/style.css
  templates/
    base.html
    auth/login.html
    auth/register.html
    dashboard/index.html
    admin/documents.html
instance/
  app.db (si usas SQLite por defecto) y uploads (si se configura)
run.py
requirements.txt
.env.example
sql/schema.sql
```

## Endpoints
- Auth: GET/POST `/login`, POST `/logout`, GET/POST `/register` (admin)
- Dashboard: GET `/`, GET `/docs/<id>/download`
- Admin: GET `/admin/documents`, POST `/admin/documents`, POST `/admin/documents/<id>`, POST `/admin/documents/<id>/delete`

## Migración y limpieza
- Se eliminaron directorios y archivos legacy (`src/templates/public`, `docs`, `index.html`), y se migraron los estáticos a `app/static`.

## Personalización
- Cambia el hash del admin en `sql/schema.sql` si deseas otra contraseña (usa Werkzeug para generar hash).
- Cambia `DATABASE_URL` para entornos productivos (usuario dedicado y contraseña segura).