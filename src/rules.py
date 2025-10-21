# Palabras clave relevantes
KEYWORDS = [
    "Código Urbanístico",
    "Código de Edificación",
    "Código de Habilitaciones",
    "compendio normativo",
    "Reglamentos Técnicos",
    "Reglamento Técnico",
    "Autorización de actividad económica",
    "Autorización de actividades económicas",
    "Autorizaciones de actividades económicas",
    "Impacto ambiental",
    "Ley Marco de Regulación de Actividades Económicas de la Ciudad Autónoma de Buenos Aires",
    "Ley Tarifaria",
    "publicidad exterior",
    "Unidad Tarifaria",
    "Sistema de Autoprotección",
    "Sistemas de Autoprotección",
    "Catastro",
    "Derecho para el Desarrollo Urbano y el Hábitat Sustentable",
    "Código Fiscal",
    "Área Céntrica",
    "planos de mensura",
    "planos de obra",
    "planos de instalaciones",
    "obras en contravención",
    "UERESGP",
    "accesibilidad",
    "digesto",
    "reurbanización",
    "uso del espacio público",
    r"[Dd]isposici[oó]n(?: [Nn]°?)? ?3\.?500(?:[-/]?GCABA)?[-/]?DGOEP[-/]?16",
    r"[Dd]isposici[oó]n(?: [Nn]°?)? ?331(?:[-/]?GCABA)?[-/]?DGDCIV[-/]?25",
    r"[Dd]isposici[oó]n(?: [Nn]°?)? ?89(?:[-/]?GCABA)?[-/]?DGROC[-/]?24",
    r"[Dd]isposici[oó]n(?: [Nn]°?)? ?526(?:[-/]?GCABA)?[-/]?DGFYCO[-/]?24",
    r"[Rr]esoluci[oó]n(?: [Nn]°?)? ?275(?:[-/]?GCABA)?[-/]?APRA[-/]?23",
    r"[Rr]esoluci[oó]n(?: [Nn]°?)? ?188(?:[-/]?GCABA)?[-/]?SSGU[-/]?24",
    r"[Rr]esoluci[oó]n(?: [Nn]°?)? ?160(?:[-/]?GCABA)?[-/]?SSHA[-/]?24",
    r"[Rr]esoluci[oó]n(?: [Nn]°?)? ?96(?:[-/]?GCABA)?[-/]?AGC[-/]?25",
    r"[Rr]esoluci[oó]n(?: [Nn]°?)? ?345(?:[-/]?GCABA)?[-/]?AGC[-/]?21",
    r"[Rr]esoluci[oó]n(?: [Nn]°?)? ?103(?:[-/]?GCABA)?[-/]?APRA[-/]?25",
    r"[Rr]esoluci[oó]n(?: [Nn]°?)? ?1(?:[-/]?GCABA)?[-/]?MEPHUGC[-/]?25",
    r"[Dd]ecreto(?: [Nn]°?)? ?51/18",
    r"[Dd]ecreto(?: [Nn]°?)? ?86/19",
    r"[Dd]ecreto(?: [Nn]°?)? ?87/19",
    r"[Dd]ecreto(?: [Nn]°?)? ?99/19",
    r"[Dd]ecreto(?: [Nn]°?)? ?105/19",
    r"[Dd]ecreto(?: [Nn]°?)? ?475/20",
    r"[Dd]ecreto(?: [Nn]°?)? ?129/25",
    r"[Dd]decreto(?: [Nn]°?)? ?116/25",
    r"[Dd]ecreto(?: [Nn]°?)? ?164/25",
    r"[Dd]ecreto(?: [Nn]°?)? ?189/25",
    r"[Ll]ey(?: [Nn]°?)? ?123",
    r"[Ll]ey(?: [Nn]°?)? ?2\.?936",
    r"[Ll]ey(?: [Nn]°?)? ?5\.?920",
    r"[Ll]ey(?: [Nn]°?)? ?6\.101",
    r"[Ll]ey(?: [Nn]°?)? ?6\.776",
    r"[Ll]ey(?: [Nn]°?)? ?6\.779",
    r"[Ll]ey(?: [Nn]°?)? ?6\.099",
    r"[Ll]ey(?: [Nn]°?)? ?6\.100",
    r"[Ll]ey(?: [Nn]°?)? ?6\.438",
    r"[Ll]ey(?: [Nn]°?)? ?6\.806",
    r"[Ll]ey(?: [Nn]°?)? ?6\.508",
    r"[Ll]ey(?: [Nn]°?)? ?6\.769"
  ]


# Verbos de acción normativa

ACTION_VERBS = [
    # Modificar
    r"regex:\bmodifica\b",
    r"regex:\bmodificar\b",
    r"regex:\bmodificase\b",
    r"regex:\bmodifiquese\b",
    r"regex:\bmodificaciones\b",

    # Derogar
    r"regex:\bderoga\b",
    r"regex:\bderogar\b",
    r"regex:\bderogase\b",
    r"regex:\bderoguese\b",

    # Aprobar (ambas formulas)
    r"regex:\baprueba\b",
    r"regex:\baprobar\b",
    r"regex:\bapruebese\b",
    r"regex:\bapruebase\b",

    # Dejar sin efecto (multi-palabra)
    r"regex:\bdeja sin efecto\b",
    r"regex:\bdejar sin efecto\b",
    r"regex:\bdejase sin efecto\b",
    r"regex:\bdejese sin efecto\b",

    # Sustituir
    r"regex:\bsustituye\b",
    r"regex:\bsustituir\b",
    r"regex:\bsustituyase\b",
    r"regex:\bsustituyese\b",

    # Establecer
    r"regex:\bestablece\b",
    r"regex:\bestablecer\b",
    r"regex:\bestablezcase\b",   # establezcase (forma imperativa oficial)
    r"regex:\bestablecese\b",

    # Fijar
    r"regex:\bfija\b",
    r"regex:\bfijar\b",
    r"regex:\bfijese\b",
    r"regex:\bfijase\b",

    # Determinar
    r"regex:\bdetermina\b",
    r"regex:\bdeterminar\b",
    r"regex:\bdeterminese\b",
    r"regex:\bdeterminase\b",

    # Reglamentar
    r"regex:\breglamenta\b",
    r"regex:\breglamentar\b",
    r"regex:\breglamentese\b",
    r"regex:\breglamentase\b",
    r"regex:\breglamentacion\b",

    # Prorrogar
    r"regex:\bprorroga\b",
    r"regex:\bprorrogar\b",
    r"regex:\bprorrogase\b",
    r"regex:\bprorrogese\b",

    # Incorporar / Crear
    r"regex:\bincorpora\b",
    r"regex:\bincorporar\b",
    r"regex:\bincorporase\b",
    r"regex:\bincorpor ese\b",   # por si hubiese error tipográfico con espacio
    r"regex:\bincorpor ese\b",
    r"regex:\bincorpor ese\b",
    r"regex:\bincorpor ese\b",   # puedes eliminar estas si no las necesitas
    r"regex:\bcrea\b",
    r"regex:\bcrear\b",
    r"regex:\bcrease\b",
    r"regex:\bcreese\b",

    # Declarar / Otorgar / Rectificar
    r"regex:\bdeclara\b",
    r"regex:\bdeclarar\b",
    r"regex:\bdeclarese\b",
    r"regex:\bdeclarase\b",

    r"regex:\botorga\b",
    r"regex:\botorgar\b",
    r"regex:\botorguese\b",
    r"regex:\botorgase\b",

    r"regex:\brectifica\b",
    r"regex:\brectificar\b",
    r"regex:\brectifiquese\b",
    r"regex:\brectificase\b",
]
