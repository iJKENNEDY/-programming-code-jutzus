
@echo lista de redes wifi::
netsh wlan show networks

@echo lista de conexiones anteriores a las redes wifi
netsh wlan show profile

@echo  password de wifis conectados anteriormente(modo admin)
netsh wlan show profile nombreDelWifi key=clear