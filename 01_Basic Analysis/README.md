# Análisis de Datos Básico con PyTorch y Apache Hadoop

## Preámbulo

Este proyecto tiene como objetivo introducirte a los conceptos básicos de PyTorch y Apache Hadoop mediante un análisis de datos simple. Utilizarás Hadoop para almacenar y procesar un pequeño conjunto de datos, y PyTorch para realizar un análisis básico.

## Introducción

En este proyecto, configurarás un entorno de desarrollo, prepararás un pequeño conjunto de datos utilizando Hadoop, y usarás PyTorch para realizar operaciones básicas de análisis de datos.

## Directrices Generales

- Este proyecto se debe realizar en un entorno de Python.
- Usa PyTorch para realizar operaciones básicas de análisis de datos.
- Usa Hadoop para el almacenamiento y procesamiento de los datos.
- Organiza tu proyecto en carpetas específicas para los datos y scripts.
- Documenta tu código y proporciona instrucciones claras sobre cómo ejecutarlo.

## Parte Obligatoria

### 1. Configuración del Entorno:

- Instala Hadoop y PyTorch en tu máquina.
- Configura un entorno virtual e instala las dependencias necesarias.

### 2. Preparación de Datos con Hadoop:

- Crea un pequeño conjunto de datos manualmente (por ejemplo, un archivo CSV con datos simples).
- Usa Hadoop para almacenar este conjunto de datos y realizar una operación simple de procesamiento, como una suma de columnas.

### 3. Análisis de Datos con PyTorch:

- Utiliza PyTorch para cargar los datos procesados por Hadoop.
- Realiza operaciones básicas de análisis, como la suma y el promedio de los valores.

## Parte Opcional (Bonus)

### 1. Visualización de Datos:

- Utiliza una biblioteca como Matplotlib para visualizar los datos procesados.

### 2. Automatización del Flujo de Trabajo:

- Escribe scripts para automatizar el flujo de trabajo de la carga, procesamiento y análisis de datos.

## Entrega y Evaluación

- Organiza tu proyecto en un repositorio de Git.
- Asegúrate de que todos los scripts se puedan ejecutar correctamente.
- Proporciona un README con instrucciones claras sobre cómo configurar el entorno y ejecutar el proyecto.

## Ejemplo de Estructura de Directorios

basic_data_analysis_project/
│
├── data/
│ ├── raw/
│ ├── processed/
│
├── scripts/
│ ├── process_data.py
│ ├── analyze_data.py
│ └── hadoop_utils.py
│
├── README.md
└── requirements.txt