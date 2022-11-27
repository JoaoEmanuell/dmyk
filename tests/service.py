from sys import path

path.append('..')

from source_android import service, ServiceInterface, Service

def test_answer():
    assert issubclass(Service, ServiceInterface)
    assert service.start_service() == False
    assert service.stop_service() == False