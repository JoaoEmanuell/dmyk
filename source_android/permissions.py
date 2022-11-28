class Android:
    def __init__(self) -> None:
        try:
            '''
            https://github.com/kivy/kivy/issues/6944#issuecomment-927382493
            '''
            from android.permissions import ( # type: ignore
                Permission, check_permission, request_permissions
            )
            perms = [Permission.WRITE_EXTERNAL_STORAGE]
            if not all([check_permission(perm) for perm in perms]):
                request_permissions(perms)
        except:
            print('Plataforma invalida, permissões do android invalidas!')