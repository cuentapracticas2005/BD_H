# Reestructuración a Flask + Jinja2

Este proyecto fue migrado desde HTML estático a una aplicación Flask con Jinja2, autenticación y control de acceso por roles.

## Objetivos
- Separar responsabilidades: rutas, modelos, plantillas y estáticos.
- Añadir autenticación segura con hashing y CSRF.
- Implementar roles: administrador y trabajador.
- Gestionar documentos con CRUD (solo admin) y descargas.
- Endurecer seguridad: limitación de subida, CSP y cabeceras.

## Estructura
```
app/
  __init__.py          # App factory, configuración, seguridad
  admin.py             # Rutas de administración (CRUD documentos)
  auth.py              # Login/Logout y registro (solo admin)
  main.py              # Dashboard y descargas
  models.py            # Modelos SQLAlchemy (User, Document)
  static/
    img/               # Imágenes migradas
    style/style.css    # CSS base
  templates/
    base.html          # Layout base
    auth/login.html    # Login
    auth/register.html # Crear usuario (admin)
    dashboard/index.html
    admin/documents.html
run.py                 # Entry point y utilidades CLI
requirements.txt
.env.example
```

## Instalación
1. Crear entorno e instalar dependencias:
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
2. Variables de entorno (copiar `.env.example` a `.env` y ajustar si es necesario):
- SECRET_KEY: clave secreta de Flask
- DATABASE_URL: opcional (por defecto SQLite en `instance/app.db`)
- UPLOAD_FOLDER: opcional (por defecto `instance/uploads`)

3. Inicializar base de datos y crear admin:
```
python -c "from app import create_app, db; app=create_app(); app.app_context().push(); db.create_all()"
python - <<'PY'
from app import create_app, db
from app.models import User, RoleEnum
app=create_app()
with app.app_context():
    u=User(username='admin', role=RoleEnum.ADMIN)
    u.set_password('Admin123!')
    db.session.add(u); db.session.commit()
print('Admin creado: admin / Admin123!')
PY
```

4. Ejecutar la app:
```
python run.py
```
Abrir `http://localhost:5000/login`.

## Roles y seguridad
- User.role: `admin` o `worker`.
- admin: CRUD de documentos y creación de usuarios.
- worker: solo ver y descargar documentos.
- Hash de contraseñas con Werkzeug, CSRF con Flask-WTF.
- Validación de archivos (solo .pdf), `secure_filename` y `MAX_CONTENT_LENGTH`.
- Cabeceras: CSP, X-Frame-Options, X-Content-Type-Options, Referrer-Policy.

## Migración de UI
- `index.html` → `templates/auth/login.html` (Jinja2)
- `interac_admin.html` → `templates/admin/documents.html` y `templates/dashboard/index.html`.
- Modales convertidos a formularios nativos con CSRF y rutas protegidas.
- Recursos estáticos movidos a `app/static` y referenciados con `url_for('static', ...)`.

## Endpoints clave
- Autenticación:
  - GET /login, POST /login, POST /logout
  - GET/POST /register (solo admin)
- Dashboard:
  - GET /
  - GET /docs/<id>/download
- Administración (solo admin, prefijo /admin):
  - GET /admin/documents
  - POST /admin/documents (crear)
  - POST /admin/documents/<id> (editar)
  - POST /admin/documents/<id>/delete (eliminar)

## Próximos pasos sugeridos
- Persistir sesiones con `Flask-Session` si se despliega multi-instancia.
- Añadir paginación y búsqueda avanzada de documentos.
- Registrar auditoría (quién creó/actualizó documentos).
- Integrar subida a almacenamiento externo (S3/minio) y antivirus.