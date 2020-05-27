import os

pluginPath = str(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
pluginPath = os.path.join(pluginPath, 'icons')

INTERSECTA = 0
CONTIENE = 1
IGUALA = 2
TOCA = 3
SOLAPA = 4
DENTRO = 5
CRUZA = 6

COUNT = 0
UNIQUE = 1
MIN = 2
MAX = 3
INTERVALO = 4
SUM = 5
MEDIA = 6
MEDIANA = 7


IGUAL = 0
DIFERENTE = 1
MAYOR = 2
MAYORIGUAL = 3
MENOR = 4
MENORIGUAL=5
COMIENZACON = 6
CONTINE = 7
IS_NULL = 8 
NOT_NULL = 9
NOCONTINETE = 10


DISCARD_NONMATCHING = True
UNDISCARD_NONMATCHING = False

P_CELL_SIZE = 300

#{'key':['attr', 'file', 'title']}

NAMES_INDEX = {
	'IA01': ['iA01_DenHab','iA01_DenHab','A01 Densidad neta de habitantes'],
	'IA02': ['iA02_DenViv','iA02_DenViv','A02 Densidad neta de viviendas'],
	'IA03': ['iA03_Compac','iA03_Compac','A03 Compacidad absoluta'],
	'IA04': ['iA04_EficTerrit','iA04_EficTerrit','A04 Eficiencia en el uso del territorio'],
	'IA05': ['iA05_PredVaci','iA05_PredVaci','A05 Área de predios vacíos'],
	'IA06': ['iA06_PropCalle','iA06_PropCalle','A06 Proporción de la calle'],
	'IA07': ['iA07_EquipUrba','iA07_EquipUrba','A07 Proximidad a servicios urbanos básicos'],
	'IA08': ['iA08_ProxEPA','iA08_ProxEPA','A08 Proximidad al espacio público abierto'],
	'IA09': ['iA09_ActComCot','iA09_ActComCot','A09 Cobertura de actividades comerciales cotinianas'],
	'IA10': ['iA10_RelaActViv','iA10_RelaActViv','A10 Relación entre actividad y residencia'],
	'IA11': ['iA11_CompUrba','iA11_CompUrba','A11 Complejidad urbana'],
	'IA12': ['iA12_DenInterPea','iA12_DenInterPea','A12 Densidad de intersecciones peatonales'],
	'IA13': ['iA13_Sinerg','iA13_Sinerg','A13 Sinergia'],
	'IB01': ['iB01_CalAire','iB01_CalAire','B01 Calidad del aire'],
	'IB02': ['iB02_IlumVia','iB02_IlumVia','B02 Luminación nocturna del viario público'],
	'IB03': ['iB03_ContAcus','iB03_ContAcus','B03 Confort acústico'],
	'IB04': ['iB04_ProxVerd','iB04_ProxVerd','B04 Proximidad al espacio verde público más cercano'],	
	'IB05': ['iB05_SupVerHab','iB05_SupVerHab','B05 Superficie verde por habitante'],
	'IB06': ['iB06_SupAgri','iB06_SupAgri','B06 Superficie de área agrícola/huertos'],	
	'IB07': ['iB07_PermSue','iB07_PermSue','B07 Permeabilidad del suelo'],
	'IC01': ['iC01_RepaVia','iC01_RepaVia','C01 Reparto del viario público peatonal'],
	'IC03': ['iC03_ViasHab','iC03_ViasHab','C03 Vías públicas por habitante'],
	'IC04': ['iC04_ProxTranAlt','iC04_ProxTranAlt','C04 Proximidad a redes de transporte alternativo'],
	'IC05': ['iC05_EspaParq','iC05_EspaParq','C05 Espacio público ocupado por vehículos parqueados'],
	'IC09': ['iC09_ConElecViv','iC09_ConElecViv','C09 Consumo de energía eléctrica en la vivienda' ],
	# 'IC10': ['ic10','ic10',''],
	# 'IC11': ['ic11','ic11',''],
	# 'IC12': ['ic12','ic12',''],
	'IC13': ['iC13_CobAlcan','iC13_CobAlcan','C13 Cobertura del sistema de servicio de alcantarillado'],
	# 'IC14': ['ic14','ic14',''],
	# 'IC15': ['ic15','ic15',''],
	# 'IC16': ['ic16','ic16',''],
	# 'IC17': ['ic17','ic17',''],
	# 'IC18': ['ic18','ic18',''],
	# 'IC19': ['ic19','ic19',''],
	# 'IC20': ['ic20','ic20',''],
	'ID01': ['iD01_CobServBas','iD01_CobServBas','D01 Viviendas con cobertura total de servicios básicos'],
	'ID02': ['iD02_CarenConst','iD02_CarenConst','D02 Viviendas con carencias constructivas'],
	'ID03': ['iD03_ZonRiesgo','iD03_ZonRiesgo','D03 Viviendas emplazadas en zonas vulnerables y de riesgo'],
	'ID04': ['iD04_EPAMejoras','iD04_EPAMejoras','D04 Espacios públicos abiertos que necesitan mejoras'],
	'ID05': ['iD05_AccInter','iD05_AccInter','D05 Acceso a internet'],
	'ID06': ['iD06_UsoTiemp','iD06_UsoTiemp','D06 Uso del tiempo'],	
	'ID07': ['iD07_IndCaliVida','iD07_IndCaliVida','D07 Indice de calidad de vida'],
	'ID08': ['iD08_AccAlim','iD08_AccAlim','D08 Cercanía y asequibilidad a alimentos'],
	'ID09': ['iD09_Robos','iD09_Robos','D09 Robos por número de habitantes'],
	'ID10': ['iD10_TenenViv','iD10_TenenViv','D10 Seguridad de tenencia de la vivienda'],
	'ID11': ['iD11_Desemp','iD11_Desemp','D11 Tasa de desempleo'],	
	'ID12': ['iD12_MujeTrab','iD12_MujeTrab','D12 Mujeres en la fuerza de trabajo remunerado'],	
	'ID13': ['iD13_EstUniv','iD13_EstUniv','D13 Población activa con estudios universitarios'],
	'ID14': ['iD14_EstabComu','iD14_EstabComu','D14 Estabilidad de la comunidad'],	
	'ID15': ['iD15_PercInseg','iD15_PercInseg','D15 Percepción de inseguridad'],	
	'ID16': ['iD16_IndiEnvej','iD16_IndiEnvej','D16 Índice de envejecimiento'],
	'ID17': ['iD17_SegrEspa','iD17_SegrEspa','D17 Segregación Espacial'],
	'X01': ['iD17_SegrEspaMan','iD17_SegrEspaMan','D17 Segregación Espacial'],
	'X02': ['iD17_SegrEspaMalla','iD17_SegrEspaMalla','D17 Segregación Espacial']
}

TEXT_GRID_INPUT = 'Malla hexagonal del área de estudio'
OPTIONAL_GRID_INPUT = False

TIME_TRAVEL_COST = 300 #segundos (5min)
DSITANCE_TRAVEL_COST = 300 #metros

STRATEGY_TIME = 1
STRATEGY_DISTANCE = 0
