# Sistema de Gestión de Documentos Hidrostal

## Descripción
Sistema web para la gestión, almacenamiento y control de documentos técnicos de Hidrostal. Permite administrar planos, documentos técnicos y usuarios del sistema con diferentes niveles de acceso.

## Características Principales
- Sistema de autenticación de usuarios
- Gestión de documentos técnicos
- Panel de administración de usuarios
- Historial de actividades
- Visualización y descarga de documentos
- Sistema de solicitud de acceso

## Estructura del Proyecto
```
BD_H/
├── public/
│   ├── img/
│   ├── style/
│   ├── index.html
│   └── prueba.html
├── pages/
│   ├── admin/
│   │   └── interac_admin.html
│   └── dashboard/
├── src/
│   └── components/
│       ├── modal_agregar_archivo/
│       ├── modal_email/
│       ├── modal_eliminar_archivo/
│       └── modal_create_user/
└── README.md
```

## Tecnologías Utilizadas
- HTML5
- JavaScript
- Tailwind CSS

## Funcionalidades

### 1. Sistema de Autenticación
- Login de usuarios
- Solicitud de acceso para nuevos usuarios

### 2. Panel de Administración
- Creación de nuevos usuarios
- Gestión de permisos
- Administración de documentos
- Visualización de historial

### 3. Gestión de Documentos
- Subida de nuevos documentos
- Búsqueda avanzada con múltiples filtros
- Visualización y descarga de archivos
- Control de versiones

### 4. Características de los Documentos
- Año
- Mes
- Descripción
- Número de plano
- Tamaño (A0-A4)
- Versión
- Dibujante
- Software utilizado

## Modales del Sistema
1. **Modal de Agregar Archivo**
   - Subida de nuevos documentos
   - Formulario con validación

2. **Modal de Email**
   - Solicitud de acceso
   - Formulario de contacto

3. **Modal de Eliminar**
   - Confirmación de eliminación
   - Prevención de eliminaciones accidentales

4. **Modal de Crear Usuario**
   - Registro de nuevos usuarios
   - Asignación de roles

## Roles de Usuario
1. **Administrador**
   - Acceso total al sistema
   - Gestión de usuarios
   - Control de documentos

2. **Personal de planta**
   - Acceso limitado
   - Visualización de documentos

## Seguridad
- Autenticación de usuarios
- Control de acceso basado en roles
- Validación de formularios
- Protección contra accesos no autorizados

## Instalación y Uso
1. Clonar el repositorio
2. Abrir index.html en un navegador web moderno
3. Para desarrollo, asegurarse de tener instalado:
   - Navegador web moderno
   - Editor de código (recomendado: VS Code)
   - Conexión a internet (para CDN de Tailwind y Alpine.js)

## Contribución
Para contribuir al proyecto:
1. Fork del repositorio
2. Crear una rama para nuevas características
3. Realizar commits con mensajes descriptivos
4. Push a la rama
5. Crear un Pull Request

## Estado del Proyecto
En desarrollo activo