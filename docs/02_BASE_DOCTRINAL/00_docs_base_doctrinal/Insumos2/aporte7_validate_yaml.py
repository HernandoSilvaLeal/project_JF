#!/usr/bin/env python3
"""
validate_yaml.py - Validador de Servilletas Doctrinales RFJ 2026
Versión: 1.0.0
Propósito: Validar estructura, integridad y calidad de archivos YAML de servilletas

Uso:
    python validate_yaml.py <archivo.yaml>
    python validate_yaml.py --all  # Valida todas las servilletas
"""

import sys
import yaml
import re
import json
from pathlib import Path
from typing import Dict, List, Tuple, Any
from jsonschema import validate, ValidationError, Draft7Validator


# ============================================
# CONFIGURACIÓN
# ============================================

# Niveles de trazabilidad
TRAZABILIDAD_NIVELES = {
    "BRONCE": {"min_versiculos": 2, "min_libros": 1},
    "PLATA": {"min_versiculos": 5, "min_libros": 3},
    "ORO": {"min_versiculos": 10, "min_libros": 5},
    "DIAMANTE": {"min_versiculos": 20, "min_libros": 10}
}

# Requisitos por tier
TIER_REQUISITOS = {
    "KERNEL_PURO": {
        "convergencia_min": 100,
        "trazabilidad_min": "ORO"
    },
    "KERNEL": {
        "convergencia_min": 80,
        "trazabilidad_min": "ORO"
    },
    "CAPA": {
        "convergencia_min": 50,
        "trazabilidad_min": "PLATA"
    },
    "PERIFERIA": {
        "convergencia_min": 0,
        "trazabilidad_min": "BRONCE"
    }
}

# Tipos de relación válidos
RELACION_TIPOS = [
    "FUNDAMENTA",
    "IMPLICA",
    "CONTRASTA",
    "REQUIERE",
    "EJEMPLIFICA",
    "CUMPLE",
    "REFUERZA"
]

# Categorías bíblicas válidas
CATEGORIAS_BIBLICAS = [
    "Pentateuco",
    "Históricos",
    "Poesía/Sabiduría",
    "Profetas Mayores",
    "Profetas Menores",
    "Evangelios",
    "Hechos",
    "Epístolas Paulinas",
    "Epístolas Generales",
    "Epístola a los Hebreos",
    "Apocalipsis"
]

# Regex para referencias bíblicas
REGEX_REFERENCIA_BIBLICA = r"^[1-3]?\s?[A-Za-zéÉíÍóÓúÚñÑ\s]+\s[0-9]+:[0-9]+([-,][0-9]+)*$"


# ============================================
# CLASES Y FUNCIONES
# ============================================

class ColoresTerminal:
    """Colores ANSI para output en terminal"""
    VERDE = '\033[92m'
    AMARILLO = '\033[93m'
    ROJO = '\033[91m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    RESET = '\033[0m'
    BOLD = '\033[1m'


def log_info(mensaje: str):
    """Log de información"""
    print(f"{ColoresTerminal.CYAN}ℹ️  {mensaje}{ColoresTerminal.RESET}")


def log_exito(mensaje: str):
    """Log de éxito"""
    print(f"{ColoresTerminal.VERDE}✅ {mensaje}{ColoresTerminal.RESET}")


def log_advertencia(mensaje: str):
    """Log de advertencia"""
    print(f"{ColoresTerminal.AMARILLO}⚠️  {mensaje}{ColoresTerminal.RESET}")


def log_error(mensaje: str):
    """Log de error"""
    print(f"{ColoresTerminal.ROJO}❌ {mensaje}{ColoresTerminal.RESET}")


def log_seccion(titulo: str):
    """Log de sección"""
    print(f"\n{ColoresTerminal.BOLD}{ColoresTerminal.AZUL}{'='*60}{ColoresTerminal.RESET}")
    print(f"{ColoresTerminal.BOLD}{ColoresTerminal.AZUL}{titulo}{ColoresTerminal.RESET}")
    print(f"{ColoresTerminal.BOLD}{ColoresTerminal.AZUL}{'='*60}{ColoresTerminal.RESET}\n")


def cargar_yaml(ruta: Path) -> Dict[str, Any]:
    """Carga y parsea archivo YAML"""
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except yaml.YAMLError as e:
        raise ValueError(f"Error al parsear YAML: {e}")
    except FileNotFoundError:
        raise FileNotFoundError(f"Archivo no encontrado: {ruta}")


def cargar_schema(ruta: Path) -> Dict[str, Any]:
    """Carga schema JSON"""
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Error al parsear JSON schema: {e}")
    except FileNotFoundError:
        raise FileNotFoundError(f"Schema no encontrado: {ruta}")


def validar_estructura_basica(data: Dict) -> List[str]:
    """Valida campos obligatorios de nivel superior"""
    errores = []
    campos_requeridos = [
        'metadata', 'claims', 'relaciones', 'guardarrailes',
        'tests', 'salidas', 'diagrama_mermaid', 'produccion'
    ]
    
    for campo in campos_requeridos:
        if campo not in data:
            errores.append(f"Falta campo obligatorio de nivel superior: {campo}")
    
    return errores


def validar_metadata(metadata: Dict) -> List[str]:
    """Valida metadata de la servilleta"""
    errores = []
    
    # ID
    if 'id' not in metadata:
        errores.append("Falta metadata.id")
    elif not re.match(r'^S[0-9]{3}$', metadata['id']):
        errores.append(f"ID inválido: {metadata['id']} (debe ser S001-S099)")
    
    # Tesis
    if 'tesis' not in metadata:
        errores.append("Falta metadata.tesis")
    elif len(metadata['tesis']) > 300:
        errores.append(f"Tesis demasiado larga: {len(metadata['tesis'])} caracteres (máx 300)")
    
    # Tier
    if 'tier' not in metadata:
        errores.append("Falta metadata.tier")
    elif metadata['tier'] not in TIER_REQUISITOS:
        errores.append(f"Tier inválido: {metadata['tier']}")
    
    # Convergencia
    if 'convergencia_score' not in metadata:
        errores.append("Falta metadata.convergencia_score")
    elif not (0 <= metadata['convergencia_score'] <= 100):
        errores.append(f"convergencia_score fuera de rango: {metadata['convergencia_score']}")
    
    # Trazabilidad
    if 'trazabilidad_nivel' not in metadata:
        errores.append("Falta metadata.trazabilidad_nivel")
    elif metadata['trazabilidad_nivel'] not in TRAZABILIDAD_NIVELES:
        errores.append(f"trazabilidad_nivel inválido: {metadata['trazabilidad_nivel']}")
    
    return errores


def validar_claim(claim_id: str, claim_data: Dict) -> List[str]:
    """Valida un claim individual"""
    errores = []
    
    # Formato de ID
    if not re.match(r'^C[0-9]+_[A-Z_]+$', claim_id):
        errores.append(f"Formato de ID incorrecto: {claim_id}")
    
    # Text
    if 'text' not in claim_data:
        errores.append(f"{claim_id}: Falta 'text'")
    elif len(claim_data['text']) > 300:
        errores.append(f"{claim_id}: text demasiado largo ({len(claim_data['text'])} chars)")
    
    # Anclas bíblicas
    if 'anclas_biblicas' not in claim_data:
        errores.append(f"{claim_id}: Falta 'anclas_biblicas'")
    elif len(claim_data['anclas_biblicas']) < 2:
        errores.append(f"{claim_id}: Mínimo 2 anclas bíblicas (tiene {len(claim_data['anclas_biblicas'])})")
    else:
        for idx, ancla in enumerate(claim_data['anclas_biblicas']):
            if 'ref' not in ancla:
                errores.append(f"{claim_id}: Ancla {idx} sin referencia")
            elif not re.match(REGEX_REFERENCIA_BIBLICA, ancla['ref']):
                errores.append(f"{claim_id}: Referencia inválida: {ancla['ref']}")
            
            if 'texto' not in ancla:
                errores.append(f"{claim_id}: Ancla {idx} sin texto")
    
    # Tier
    if 'tier' not in claim_data:
        errores.append(f"{claim_id}: Falta 'tier'")
    
    # Peso generativo
    if 'peso_generativo' not in claim_data:
        errores.append(f"{claim_id}: Falta 'peso_generativo'")
    elif not (1 <= claim_data['peso_generativo'] <= 10):
        errores.append(f"{claim_id}: peso_generativo fuera de rango (1-10)")
    
    return errores


def validar_relaciones(relaciones: List, claims: Dict) -> List[str]:
    """Valida relaciones entre claims"""
    errores = []
    claim_ids = set(claims.keys())
    
    for idx, rel in enumerate(relaciones):
        # Campos obligatorios
        if 'from' not in rel:
            errores.append(f"Relación {idx}: Falta 'from'")
        elif rel['from'] not in claim_ids:
            errores.append(f"Relación {idx}: 'from' apunta a claim inexistente: {rel['from']}")
        
        if 'to' not in rel:
            errores.append(f"Relación {idx}: Falta 'to'")
        elif rel['to'] not in claim_ids:
            errores.append(f"Relación {idx}: 'to' apunta a claim inexistente: {rel['to']}")
        
        if 'type' not in rel:
            errores.append(f"Relación {idx}: Falta 'type'")
        elif rel['type'] not in RELACION_TIPOS:
            errores.append(f"Relación {idx}: Tipo inválido: {rel['type']}")
        
        if 'explicacion' not in rel:
            errores.append(f"Relación {idx}: Falta 'explicacion'")
        
        # Fuerza (opcional pero recomendado)
        if 'fuerza' in rel and not (1 <= rel['fuerza'] <= 10):
            errores.append(f"Relación {idx}: fuerza fuera de rango (1-10)")
    
    return errores


def validar_trazabilidad(claims: Dict, nivel_requerido: str) -> Tuple[bool, str]:
    """Valida que los claims cumplan el nivel de trazabilidad requerido"""
    requisitos = TRAZABILIDAD_NIVELES[nivel_requerido]
    min_versiculos = requisitos['min_versiculos']
    min_libros = requisitos['min_libros']
    
    for claim_id, claim_data in claims.items():
        if 'anclas_biblicas' not in claim_data:
            return False, f"{claim_id}: Sin anclas bíblicas"
        
        num_versiculos = len(claim_data['anclas_biblicas'])
        if num_versiculos < min_versiculos:
            return False, f"{claim_id}: Solo {num_versiculos} versículos (requiere {min_versiculos} para {nivel_requerido})"
        
        # Contar libros únicos
        libros = set()
        for ancla in claim_data['anclas_biblicas']:
            if 'ref' in ancla:
                # Extraer libro de referencia (ej: "Juan 3:16" -> "Juan")
                libro = re.match(r'^([1-3]?\s?[A-Za-zéÉíÍóÓúÚñÑ\s]+)', ancla['ref'])
                if libro:
                    libros.add(libro.group(1).strip())
        
        if len(libros) < min_libros:
            return False, f"{claim_id}: Solo {len(libros)} libros diferentes (requiere {min_libros} para {nivel_requerido})"
    
    return True, "Trazabilidad cumplida"


def validar_convergencia(metadata: Dict) -> Tuple[bool, str]:
    """Valida que la convergencia cumpla el mínimo para el tier"""
    tier = metadata.get('tier')
    convergencia = metadata.get('convergencia_score', 0)
    
    if tier not in TIER_REQUISITOS:
        return False, f"Tier desconocido: {tier}"
    
    min_convergencia = TIER_REQUISITOS[tier]['convergencia_min']
    
    if convergencia < min_convergencia:
        return False, f"Convergencia {convergencia}% < mínimo {min_convergencia}% para tier {tier}"
    
    return True, f"Convergencia {convergencia}% cumple requisitos de tier {tier}"


def validar_tests_status(tests: Dict) -> List[str]:
    """Valida que todos los tests estén en PASS"""
    advertencias = []
    
    for test_id, test_data in tests.items():
        if 'status' not in test_data:
            advertencias.append(f"{test_id}: Sin status")
        elif test_data['status'] == 'FAIL':
            advertencias.append(f"{test_id}: Test FALLANDO")
        elif test_data['status'] == 'PENDING':
            advertencias.append(f"{test_id}: Test PENDIENTE")
    
    return advertencias


def generar_reporte(
    ruta_archivo: Path,
    data: Dict,
    errores_estructura: List[str],
    errores_metadata: List[str],
    errores_claims: List[str],
    errores_relaciones: List[str],
    resultado_trazabilidad: Tuple[bool, str],
    resultado_convergencia: Tuple[bool, str],
    advertencias_tests: List[str]
) -> bool:
    """Genera reporte de validación"""
    
    log_seccion(f"📋 REPORTE DE VALIDACIÓN: {ruta_archivo.name}")
    
    # Información básica
    if 'metadata' in data:
        metadata = data['metadata']
        log_info(f"ID: {metadata.get('id', 'N/A')}")
        log_info(f"Título: {metadata.get('titulo', 'N/A')}")
        log_info(f"Tier: {metadata.get('tier', 'N/A')}")
        log_info(f"Convergencia: {metadata.get('convergencia_score', 'N/A')}%")
        log_info(f"Trazabilidad: {metadata.get('trazabilidad_nivel', 'N/A')}")
        log_info(f"Versión: {data.get('produccion', {}).get('version', 'N/A')}")
        log_info(f"Estado: {data.get('produccion', {}).get('estado', 'N/A')}")
    
    print()
    
    # Errores críticos
    total_errores = (
        len(errores_estructura) +
        len(errores_metadata) +
        len(errores_claims) +
        len(errores_relaciones)
    )
    
    if total_errores > 0:
        log_seccion("❌ ERRORES CRÍTICOS")
        
        if errores_estructura:
            log_error("Errores de estructura:")
            for e in errores_estructura:
                print(f"  • {e}")
        
        if errores_metadata:
            log_error("Errores en metadata:")
            for e in errores_metadata:
                print(f"  • {e}")
        
        if errores_claims:
            log_error("Errores en claims:")
            for e in errores_claims:
                print(f"  • {e}")
        
        if errores_relaciones:
            log_error("Errores en relaciones:")
            for e in errores_relaciones:
                print(f"  • {e}")
        
        print()
    
    # Validaciones de calidad
    log_seccion("🔍 VALIDACIONES DE CALIDAD")
    
    # Trazabilidad
    if resultado_trazabilidad[0]:
        log_exito(f"Trazabilidad: {resultado_trazabilidad[1]}")
    else:
        log_error(f"Trazabilidad: {resultado_trazabilidad[1]}")
    
    # Convergencia
    if resultado_convergencia[0]:
        log_exito(f"Convergencia: {resultado_convergencia[1]}")
    else:
        log_error(f"Convergencia: {resultado_convergencia[1]}")
    
    print()
    
    # Advertencias
    if advertencias_tests:
        log_seccion("⚠️  ADVERTENCIAS")
        for adv in advertencias_tests:
            log_advertencia(adv)
        print()
    
    # Resultado final
    exito = (
        total_errores == 0 and
        resultado_trazabilidad[0] and
        resultado_convergencia[0]
    )
    
    log_seccion("🎯 RESULTADO FINAL")
    if exito:
        if advertencias_tests:
            log_advertencia(f"APROBADA CON ADVERTENCIAS ({len(advertencias_tests)} warnings)")
        else:
            log_exito("✨ APROBADA - Servilleta válida y lista para review teológica")
    else:
        log_error(f"❌ RECHAZADA - {total_errores} errores críticos")
    
    print()
    
    return exito


def validar_servilleta(ruta: Path, schema: Dict = None) -> bool:
    """Función principal de validación"""
    
    try:
        # Cargar YAML
        log_info(f"Cargando {ruta}...")
        data = cargar_yaml(ruta)
        
        # Validar contra schema JSON (si está disponible)
        if schema:
            try:
                validate(instance=data, schema=schema)
                log_exito("Schema JSON validado")
            except ValidationError as e:
                log_advertencia(f"Violación de schema JSON: {e.message}")
        
        # Validaciones estructurales
        errores_estructura = validar_estructura_basica(data)
        errores_metadata = validar_metadata(data.get('metadata', {}))
        
        # Validar claims
        errores_claims = []
        claims = data.get('claims', {})
        for claim_id, claim_data in claims.items():
            errores_claims.extend(validar_claim(claim_id, claim_data))
        
        # Validar relaciones
        errores_relaciones = validar_relaciones(
            data.get('relaciones', []),
            claims
        )
        
        # Validar trazabilidad
        nivel_requerido = data.get('metadata', {}).get('trazabilidad_nivel', 'BRONCE')
        resultado_trazabilidad = validar_trazabilidad(claims, nivel_requerido)
        
        # Validar convergencia
        resultado_convergencia = validar_convergencia(data.get('metadata', {}))
        
        # Validar tests
        advertencias_tests = validar_tests_status(data.get('tests', {}))
        
        # Generar reporte
        exito = generar_reporte(
            ruta,
            data,
            errores_estructura,
            errores_metadata,
            errores_claims,
            errores_relaciones,
            resultado_trazabilidad,
            resultado_convergencia,
            advertencias_tests
        )
        
        return exito
        
    except Exception as e:
        log_error(f"Error durante validación: {e}")
        return False


def main():
    """Función principal"""
    if len(sys.argv) < 2:
        print("Uso: python validate_yaml.py <archivo.yaml>")
        print("      python validate_yaml.py --all")
        sys.exit(1)
    
    # Cargar schema
    schema_path = Path(__file__).parent.parent / 'schemas' / 'servilleta.schema.json'
    schema = None
    if schema_path.exists():
        try:
            schema = cargar_schema(schema_path)
            log_info(f"Schema cargado desde {schema_path}")
        except Exception as e:
            log_advertencia(f"No se pudo cargar schema: {e}")
    
    # Validar archivo(s)
    if sys.argv[1] == '--all':
        # Validar todas las servilletas
        servilletas_dir = Path(__file__).parent.parent / 'servilletas'
        if not servilletas_dir.exists():
            log_error(f"Directorio no encontrado: {servilletas_dir}")
            sys.exit(1)
        
        archivos = sorted(servilletas_dir.glob('S*.yaml'))
        if not archivos:
            log_advertencia("No se encontraron servilletas para validar")
            sys.exit(0)
        
        log_seccion(f"🔍 VALIDANDO {len(archivos)} SERVILLETAS")
        
        resultados = []
        for archivo in archivos:
            exito = validar_servilleta(archivo, schema)
            resultados.append((archivo.name, exito))
        
        # Resumen final
        log_seccion("📊 RESUMEN FINAL")
        aprobadas = sum(1 for _, exito in resultados if exito)
        rechazadas = len(resultados) - aprobadas
        
        log_info(f"Total: {len(resultados)}")
        log_exito(f"Aprobadas: {aprobadas}")
        if rechazadas > 0:
            log_error(f"Rechazadas: {rechazadas}")
        
        sys.exit(0 if rechazadas == 0 else 1)
    
    else:
        # Validar archivo individual
        ruta = Path(sys.argv[1])
        if not ruta.exists():
            log_error(f"Archivo no encontrado: {ruta}")
            sys.exit(1)
        
        exito = validar_servilleta(ruta, schema)
        sys.exit(0 if exito else 1)


if __name__ == '__main__':
    main()
