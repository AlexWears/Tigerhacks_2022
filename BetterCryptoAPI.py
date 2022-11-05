import cryptocompare

cryptocompare.cryptocompare._set_api_key_parameter("ab505607f96675cb996706983700a1497b4fa06a9218fc525549f0e50fa0d470")

#print(cryptocompare.get_coin_list(format=True))
#print(cryptocompare.get_price('DESO', currency='USD', full=False).pop("DESO").pop('USD'))

class CryptoAPI:

    def __init__(self, JimRs_Garage):
        self.settings = JimRs_Garage.settings
        self.screen = JimRs_Garage.screen
        self.screen_rect = JimRs_Garage.screen

    def get_DeSo_price():
        return cryptocompare.get_price('DESO', currency='USD', full=False).pop("DESO").pop('USD')

