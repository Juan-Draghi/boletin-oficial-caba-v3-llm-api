> ⚠️ Este repositorio corresponde a una versión **anterior** del proyecto de relevamiento del Boletín Oficial de CABA.
> La versión actual, basada en modelos de Machine Learning supervisado, se encuentra en: [https://github.com/tu-usuario/boletin-oficial-caba-ml](https://github.com/Juan-Draghi/boletin-oficial-caba-ml.)

# Análisis automatizado del Boletín Oficial con filtrado semántico

Este proyecto permite detectar automáticamente normativa de interés publicada en el Boletín Oficial de la Ciudad Autónoma de Buenos Aires, utilizando un enfoque mixto basado en búsqueda por palabras clave y evaluación semántica asistida por un modelo de lenguaje (LLM).

## 🧩 Funcionalidad

- Extrae texto de ejemplares en PDF del Boletín Oficial.
- Busca coincidencias con una lista de términos clave.
- Evalúa si el contexto indica una acción normativa real (modificación, aprobación, derogación, etc.).
- Exporta los resultados pertinentes en un archivo Excel, listo para revisión o archivo.

## 📚 Requisitos

- Google Colab
- Cuenta en Google Cloud con acceso a Gemini API (API Key)
- Archivo Excel con términos clave (opcional)
- Archivo PDF del Boletín (subido o accedido desde Drive o URL)

## 🚀 Cómo usarlo

1. Abrir el script en Google Colab.
2. Cargar el PDF del Boletín (o configurá para usar Drive o una URL fija).
3. El script generará un Excel con los resultados pertinentes, listos para descargar.

## 🔒 Licencia

Este proyecto está disponible bajo la [Licencia MIT](LICENSE).  
Se permite su uso, copia, modificación y redistribución con o sin fines comerciales, siempre que se mantenga la atribución correspondiente.


## Autor:
Juan Draghi — Biblioteca del Consejo Profesional de Arquitectura y Urbanismo (con la asistencia de ChatGPT)


Este proyecto se distribuye bajo la licencia MIT. Puede ser reutilizado, adaptado o modificado libremente, citando al autor original.

