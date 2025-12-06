# test_sistema.py
import pytest
from sistema import Cliente, CalculadoraPedidoService


# --- DRIVER ---
@pytest.fixture
def service():
    return CalculadoraPedidoService()


# --- CAMINHO FELIZ ---

def test_caminho_feliz(service):
    # STUB: Instanciação de um objeto Cliente com estado fixo para teste
    cliente = Cliente(0, "sp")

    # Verificação: Perfil Básico (0% desc) + SP (0% frete) -> 100 permanece 100
    assert service.processar_pedido(cliente, 100) == 100.0


# --- TESTES RN01 ---

def test_rn01_basico(service):
    # STUB: Cliente Básico
    cliente = Cliente(0, "sp")
    # Assert: Verifica se o valor final é exatamente 100 (sem alteração)
    assert service.processar_pedido(cliente, 100) == 100.0


def test_rn01_bronze(service):
    # STUB: Cliente Bronze (3% desconto)
    cliente = Cliente(1, "sp")
    # Assert: 100 - 3 = 97
    assert service.processar_pedido(cliente, 100) == 97.0


def test_rn01_prata(service):
    # STUB: Cliente Prata (5% desconto)
    cliente = Cliente(2, "sp")
    # Assert: 100 - 5 = 95
    assert service.processar_pedido(cliente, 100) == 95.0


def test_rn01_ouro(service):
    # STUB: Cliente Ouro (10% desconto)
    cliente = Cliente(3, "sp")
    # Assert: 100 - 10 = 90
    assert service.processar_pedido(cliente, 100) == 90.0


def test_rn01_invalido(service):
    # STUB: Cliente com perfil inexistente
    cliente = Cliente(4, "sp")

    # Tratamento de Exceção: É esperado um erro aqui
    with pytest.raises(ValueError):
        service.processar_pedido(cliente, 100)


# --- TESTES RN02 ---

def test_rn02_sp(service):
    # STUB: Estado SP (Isento de frete)
    cliente = Cliente(0, "sp")
    assert service.processar_pedido(cliente, 100) == 100.0


def test_rn02_sudeste(service):
    # STUB: Estado ES (Sudeste = 5% frete)
    cliente = Cliente(0, "es")
    # Assert: 100 + 5 (frete) = 105
    assert service.processar_pedido(cliente, 100) == 105.0


def test_rn02_brasil(service):
    # STUB: Estado AM (Outros = 8% frete)
    cliente = Cliente(0, "am")
    # Assert: 100 + 8 (frete) = 108
    assert service.processar_pedido(cliente, 100) == 108.0


def test_rn02_invalido(service):
    # STUB: Estado fora do Brasil
    cliente = Cliente(0, "texas")

    # Tratamento de Exceção: O sistema deve impedir o cálculo
    with pytest.raises(ValueError):
        service.processar_pedido(cliente, 100)