# test_sistema.py
import pytest
from sistema import Cliente, CalculadoraPedidoService


# Fixture: cria o serviço uma vez para usar em todos os testes
@pytest.fixture
def service():
    return CalculadoraPedidoService()


# --- Teste do Caminho Feliz ---

def test_caminho_feliz(service):
    cliente = Cliente( 0, "sp")
    assert  service.processar_pedido(cliente, 100)


# --- Testes RN01 ---

# Perfil Básico
def test_rn01_basico(service):
    cliente = Cliente( 0, "sp")
    assert  service.processar_pedido(cliente, 100)

# Perfil Bronze
def test_rn01_bronze(service):
    cliente = Cliente( 1, "sp")
    assert  service.processar_pedido(cliente, 100)

#Perfil Prata
def test_rn01_prata(service):
    cliente = Cliente( 2, "sp")
    assert  service.processar_pedido(cliente, 100)

#Perfil Ouro
def test_rn01_ouro(service):
    cliente = Cliente( 3, "sp")
    assert  service.processar_pedido(cliente, 100)

# Perfil inválido
def test_rn01_invalido(service):
    cliente = Cliente( 4, "sp")
    assert  service.processar_pedido(cliente, 100)



# --- Testes RN02 ---

# Estado de SP
def test_rn02_sp(service):
    cliente = Cliente( 0, "sp")
    assert  service.processar_pedido(cliente, 100)

# Estado do Sudeste
def test_rn02_sudeste(service):
    cliente = Cliente( 0, "es")
    assert  service.processar_pedido(cliente, 100)

# Estado do Brasil
def test_rn02_brasil(service):
    cliente = Cliente( 0, "am")
    assert  service.processar_pedido(cliente, 100)

# Estado Inválido
def test_rn02_invalido(service):
    cliente = Cliente( 0, "texas")
    assert  service.processar_pedido(cliente, 100)

