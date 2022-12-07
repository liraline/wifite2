from .wep_result import CrackResultWEP
from .wpa_result import CrackResultWPA
from .wps_result import CrackResultWPS
from .pmkid_result import CrackResultPMKID

class ResultFactory(object):
    def create_wep_result(self, bssid, essid, hex_key, ascii_key):
        result = CrackResultWEP(bssid, essid, hex_key, ascii_key)
        return result

    def create_wpa_result(self, bssid, essid, handshake_file, key):
        result = CrackResultWPA(bssid, essid, handshake_file, key)
        return result

    def create_wps_result(self, bssid, essid, pin, psk):
        result = CrackResultWPS(bssid, essid, pin, psk)
        return result
    
    def create_pmkid_result(self, bssid, essid, pmkid_file, key):
        result = CrackResultPMKID(bssid, essid, pmkid_file, key)
        return result