from colorama import Fore, init
from fe_param_get_tipos_tributos import fe_param_get_tipos_tributos
from fe_param_get_tipos_paises import fe_param_get_tipos_paises
from fe_param_get_tipos_opcional import fe_param_get_tipos_opcional
from fe_param_get_tipos_monedas import fe_param_get_tipos_monedas
from fe_param_get_tipos_iva import fe_param_get_tipos_iva
from fe_param_get_tipos_doc import fe_param_get_tipos_doc
from fe_param_get_tipos_concepto import fe_param_get_tipos_concepto
from fe_param_get_tipos_cbte import fe_param_get_tipos_cbte
from fe_param_get_ptos_venta import fe_param_get_ptos_venta
from fe_param_get_cotizacion import fe_param_get_cotization
from fe_param_get_condicion_iva_receptor import fe_param_get_condicion_iva_receptor
from fe_param_get_actividades import fe_param_get_actividades
from fe_comp_ultimo_autorizado import fe_comp_ultimo_autorizado
from fe_comp_totX_request import fecomp_totx_request
from fe_comp_consultar import fe_comp_consultar
from fecae_solicitar import fecae_solicitar
from fecaea_reg_informativo import fecae_reg_informativo
from fecaea_solicitar import fecaea_solicitar
from fecaea_sin_movimiento_informar import fecaea_sin_movimiento_informar
from fecaea_sin_movimiento_consultar import fecaea_sin_movimiento_consultar
from fecaea_consultar import fecaea_consultar

init(autoreset=True)

def print_result(name, status):
    color = Fore.GREEN if status == "success" else Fore.RED
    print(f"{color}{name}={status}")

# Execute all functions one by one
response = fecae_solicitar()
print_result("FECAESolicitar", response["status"])

response = fecomp_totx_request()
print_result("FECompTotXRequest", response["status"])

response = fe_comp_ultimo_autorizado()
print_result("FECompUltimoAutorizado", response["status"])

response = fe_comp_consultar()
print_result("FECompConsultar", response["status"])

response = fecae_reg_informativo()
print_result("FECAEARegInformativo", response["status"])

response = fecaea_solicitar()
print_result("FECAEASolicitar", response["status"])

response = fecaea_sin_movimiento_consultar()
print_result("FECAEASinMovimientoConsultar", response["status"])

response = fecaea_sin_movimiento_informar()
print_result("FECAEASinMovimientoInformar", response["status"])

response = fecaea_consultar()
print_result("FECAEAConsultar", response["status"])

response = fe_param_get_cotization()
print_result("FEParamGetCotizacion", response["status"])

response = fe_param_get_tipos_tributos()
print_result("FEParamGetTiposTributos", response["status"])

response = fe_param_get_tipos_monedas()
print_result("FEParamGetTiposMonedas", response["status"])

response = fe_param_get_tipos_iva()
print_result("FEParamGetTiposIva", response["status"])

response = fe_param_get_tipos_opcional()
print_result("FEParamGetTiposOpcional", response["status"])

response = fe_param_get_tipos_concepto()
print_result("FEParamGetTiposConcepto", response["status"])

response = fe_param_get_ptos_venta()
print_result("FEParamGetPtosVenta", response["status"])

response = fe_param_get_tipos_cbte()
print_result("FEParamGetTiposCbte", response["status"])

response = fe_param_get_condicion_iva_receptor()
print_result("FEParamGetCondicionIvaReceptor", response["status"])

response = fe_param_get_tipos_doc()
print_result("FEParamGetTiposDoc", response["status"])

response = fe_param_get_tipos_paises()
print_result("FEParamGetTiposPaises", response["status"])

response = fe_param_get_actividades()
print_result("FEParamGetActividades", response["status"])
