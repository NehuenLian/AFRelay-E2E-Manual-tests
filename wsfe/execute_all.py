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
from fecae_reg_informativo import fecae_reg_informativo
from fecaea_solicitar import fecaea_solicitar
from fecaea_sin_movimiento_informar import fecaea_sin_movimiento_informar
from fecaea_sin_movimiento_consultar import fecaea_sin_movimiento_consultar
from fecaea_consultar import fecaea_consultar

# Execute all functions one by one
response = fecae_solicitar()
if response["status"] == "success":
    print("FECAESolicitar=success")
else:
    print("FECAESolicitar=error")

response = fecomp_totx_request()
if response["status"] == "success":
    print("FECompTotXRequest=success")
else:
    print("FECompTotXRequest=error")

response = fe_comp_ultimo_autorizado()
if response["status"] == "success":
    print("FECompUltimoAutorizado=success")
else:
    print("FECompUltimoAutorizado=error")

response = fe_comp_consultar()
if response["status"] == "success":
    print("FECompConsultar=success")
else:
    print("FECompConsultar=error")

response = fecae_reg_informativo()
if response["status"] == "success":
    print("FECAEARegInformativo=success")
else:
    print("FECAEARegInformativo=error")

response = fecaea_solicitar()
if response["status"] == "success":
    print("FECAEASolicitar=success")
else:
    print("FECAEASolicitar=error")

response = fecaea_sin_movimiento_consultar()
if response["status"] == "success":
    print("FECAEASinMovimientoConsultar=success")
else:
    print("FECAEASinMovimientoConsultar=error")

response = fecaea_sin_movimiento_informar()
if response["status"] == "success":
    print("FECAEASinMovimientoInformar=success")
else:
    print("FECAEASinMovimientoInformar=error")

response = fecaea_consultar()
if response["status"] == "success":
    print("FECAEAConsultar=success")
else:
    print("FECAEAConsultar=error")

response = fe_param_get_cotization()
if response["status"] == "success":
    print("FEParamGetCotizacion=success")
else:
    print("FEParamGetCotizacion=error")

response = fe_param_get_tipos_tributos()
if response["status"] == "success":
    print("FEParamGetTiposTributos=success")
else:
    print("FEParamGetTiposTributos=error")

response = fe_param_get_tipos_monedas()
if response["status"] == "success":
    print("FEParamGetTiposMonedas=success")
else:
    print("FEParamGetTiposMonedas=error")

response = fe_param_get_tipos_iva()
if response["status"] == "success":
    print("FEParamGetTiposIva=success")
else:
    print("FEParamGetTiposIva=error")

response = fe_param_get_tipos_opcional()
if response["status"] == "success":
    print("FEParamGetTiposOpcional=success")
else:
    print("FEParamGetTiposOpcional=error")

response = fe_param_get_tipos_concepto()
if response["status"] == "success":
    print("FEParamGetTiposConcepto=success")
else:
    print("FEParamGetTiposConcepto=error")

response = fe_param_get_ptos_venta()
if response["status"] == "success":
    print("FEParamGetPtosVenta=success")
else:
    print("FEParamGetPtosVenta=error")

response = fe_param_get_tipos_cbte()
if response["status"] == "success":
    print("FEParamGetTiposCbte=success")
else:
    print("FEParamGetTiposCbte=error")

response = fe_param_get_condicion_iva_receptor()
if response["status"] == "success":
    print("FEParamGetCondicionIvaReceptor=success")
else:
    print("FEParamGetCondicionIvaReceptor=error")

response = fe_param_get_tipos_doc()
if response["status"] == "success":
    print("FEParamGetTiposDoc=success")
else:
    print("FEParamGetTiposDoc=error")

response = fe_param_get_tipos_paises()
if response["status"] == "success":
    print("FEParamGetTiposPaises=success")
else:
    print("FEParamGetTiposPaises=error")

response = fe_param_get_actividades()
if response["status"] == "success":
    print("FEParamGetActividades=success")
else:
    print("FEParamGetActividades=error")
