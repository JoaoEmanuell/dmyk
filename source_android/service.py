from .interfaces import ServiceInterface

class Service(ServiceInterface):
    def __init__(self, platform: str='') -> None:
        self.__platform = platform
        self.__invalid_platform_message = 'Invalid platform to service'
        if self.__platform == 'android':
            from android import AndroidService # type: ignore
            self.__service = AndroidService('Baixador yt', 'running')

    def start_service(self) -> bool:
        if self.private__validate_service_platform():
            print("Start Service")
            self.__service.start('Service started')
            return True
        else:
            print(self.__invalid_platform_message)
            return False

    def stop_service(self) -> bool:
        if self.private__validate_service_platform():
            print("Stop service")
            self.__service.stop()
            return True
        else:
            print(self.__invalid_platform_message)
            return False

    def private__validate_service_platform(self) -> bool:
        if self.__platform == 'android' and self.__service != None:
            return True
        else: return False