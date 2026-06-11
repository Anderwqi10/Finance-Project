#  Finance Project

Sistema de gestión financiera desarrollado con Django para la administración de usuarios, cuentas bancarias, tarjetas, bancos, países y monedas.

---

##  Descripción

Finance Project es una aplicación web orientada a la gestión de información financiera, permitiendo registrar usuarios, administrar cuentas bancarias, asociar tarjetas y gestionar entidades financieras de diferentes países y monedas.

---

##  Capturas de Pantalla

### Página Principal

[AGREGAR IMAGEN AQUÍ]

Descripción de la interfaz principal del sistema y acceso a las funcionalidades financieras.

---

### Gestión de Usuarios

[AGREGAR IMAGEN AQUÍ]

Módulo encargado de la administración de usuarios, roles y datos personales.

---

### Gestión de Cuentas

[AGREGAR IMAGEN AQUÍ]

Permite crear y administrar cuentas de ahorro y corriente asociadas a los usuarios.

---

### Gestión de Tarjetas

[AGREGAR IMAGEN AQUÍ]

Administración de tarjetas bancarias vinculadas a las cuentas registradas en el sistema.

---

##  Características

- Gestión de usuarios.
- Administración de cuentas bancarias.
- Gestión de tarjetas financieras.
- Administración de bancos.
- Gestión de países y monedas.
- Relación entre entidades financieras y usuarios.
- Persistencia de datos mediante SQLite.
- Panel administrativo de Django.

---

##  Tecnologías Utilizadas

- Python
- Django 5.2
- SQLite
- HTML
- CSS
- JavaScript

---

##  Arquitectura

[AGREGAR DIAGRAMA AQUÍ]

```text
Usuario
   │
   ├── Cuenta
   │      │
   │      └── Tarjeta
   │
   ├── País
   │      │
   │      └── Moneda
   │
   └── Banco
```

---

##  Estructura del Proyecto

```text
Finance-Project/
│
├── FinancesWeb/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── usuario/
│   ├── models.py
│   ├── views.py
│   └── migrations/
│
├── cuenta/
│   ├── models.py
│   ├── views.py
│   └── migrations/
│
├── db.sqlite3
├── manage.py
└── requirements.txt
```

---

##  Modelo de Datos

### Usuario

```text
- Username
- Rol
- Teléfono
- Aceptación de términos
```

### Cuenta

```text
- Usuario
- Banco
- Saldo
- Tipo de cuenta
- Moneda
```

### Tarjeta

```text
- Cuenta
- Banco
- Número
- Marca
- Fecha de expiración
- Límite de crédito
```

### Banco

```text
- Nombre
- País asociado
```

### País

```text
- Nombre
- Moneda
```

### Moneda

```text
- Nombre
```

---

##  Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/usuario/Finance-Project.git
```

### 2. Acceder al proyecto

```bash
cd Finance-Project
```

### 3. Crear entorno virtual

```bash
python -m venv venv
```

### 4. Activar entorno virtual

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

### 5. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 6. Ejecutar migraciones

```bash
python manage.py migrate
```

### 7. Iniciar servidor

```bash
python manage.py runserver
```

### 8. Abrir en navegador

```text
http://127.0.0.1:8000/
```

---

##  Equipo de Desarrollo

Proyecto académico orientado al aprendizaje de desarrollo web con Django y modelado de bases de datos financieras.

---
