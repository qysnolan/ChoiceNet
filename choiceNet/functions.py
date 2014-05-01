from django.shortcuts import render, HttpResponse
from django.core.context_processors import csrf
from Crypto.Cipher import AES

import json
import binascii
import datetime
# import zlib


from .models import Session


class MenuObject:
    name = None
    url = None
    forceSubmenu = False
    icon = None

    submenu = []

    def __init__(self, name, url=None, icon=None, disabled=False):
        self.name = name
        self.icon = icon

        self.forceSubmenu = False
        self.submenu = []

        if url is None:
            self.forceSubmenu = True
        else:
            self.url = url

        self.disabled = disabled

    def addSubMenu(self, menu):
        self.submenu.append(menu)

    def addSubitem(self, name, url, icon=None, disabled=False):
        self.submenu.append(MenuObject(name, url, icon, disabled))

    def hasSubmenu(self):
        return self.submenu

    def canShow(self):
        if self.forceSubmenu and self.hasSubmenu():
            return True
        elif not self.forceSubmenu:
            return True
        return False


def render_with_user(request, template_name, context={}):
    from website.settings import DEBUG

    context["debugMode"] = DEBUG

    user = request.user
    context["menu"] = []

    if user.is_authenticated():
        context["name"] = user.fullname()
        context["user"] = request.user
        context.update(csrf(request))

        speedMenu = MenuObject("High Speed")
        speedMenu.addSubitem("Normal High Speed", "help")
        speedMenu.addSubitem("Very High Speed", "help")
        speedMenu.addSubitem("Extreme High Speed", "help")
        context["menu"].append(speedMenu)

        priceMenu = MenuObject("Low price")
        priceMenu.addSubitem("Normal Low price", "help")
        priceMenu.addSubitem("Very Low price", "help")
        priceMenu.addSubitem("Extreme Low price", "help")
        context["menu"].append(priceMenu)

        securityMenu = MenuObject("High Security")
        securityMenu.addSubitem("Normal High Security", "help")
        securityMenu.addSubitem("Very High Security", "help")
        securityMenu.addSubitem("Extreme High Security", "help")
        context["menu"].append(securityMenu)

        worldMenu = MenuObject("World Network")
        stateMenu = MenuObject("States")
        stateMenu.addSubitem("Massachusetts", "help")
        stateMenu.addSubitem("Other states", "help")
        worldMenu.addSubMenu(stateMenu)
        # context["menu"].append(worldMenu)

        return render(request, template_name, context)

    else:
        context["user"] = None
        context["name"] = "Login or sign up"

        loginMenu = MenuObject("Login to get full function", "login")
        context["menu"].append(loginMenu)

        return render(request, template_name, context)


def render_with_session(session_id, input_data):

    try:
        s = Session.objects.all().get(id=session_id)
    except:
        data = {"is_session": False, "data": None, "expire": True}
        json_data = json.dumps(data)
        return HttpResponse(json_data)

    from django.utils.timezone import utc
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    if now > s.end_time:
        data = {"is_session": True, "data": None, "expire": True}
        json_data = json.dumps(data)
        return HttpResponse(json_data)

    input_data = encrypt(input_data, s.key)
    data = {"is_session": True, "data": input_data, "expire": False}
    json_data = json.dumps(data)

    return HttpResponse(json_data)


def check_session(session_id, session):

    data = {"is_session": False, "data": None, "expire": True}
    json_data = json.dumps(data)

    try:
        s = Session.objects.all().get(id=session_id)
    except:
        return HttpResponse(json_data)

    if session == 0 or session != s.session or not s.is_login:
        return HttpResponse(json_data)

    return True


def encrypt(data, key):

    IV = 16 * '\x00'
    encrypt = AES.new(key[:32], AES.MODE_CFB, IV)
    json_data = json.dumps(data)

    ciphertext = encrypt.encrypt(str(json_data))
    bin_data = bin(int(binascii.hexlify(ciphertext), 16))

    return str(bin_data)
    # return zlib.compress(str(bin_data))


def decrypt(data, key):

    # data = zlib.decompress(str(data))
    if not data:
        return None
    n = int(data, 2)
    cipher_text = binascii.unhexlify('%x' % n)

    IV = 16 * '\x00'
    decrypt = AES.new(key[:32], AES.MODE_CFB, IV)
    plain_text = decrypt.decrypt(cipher_text)
    plain_text = json.loads(plain_text)

    return plain_text


from binascii import hexlify
import hashlib
import Crypto.Random.random

# If a secure random number generator is unavailable, exit with an error.
try:
    secure_random = Crypto.Random.random.getrandbits
except ImportError:
    import OpenSSL
    secure_random = lambda x: long(hexlify(OpenSSL.rand.bytes(x >> 3)), 16)


class DiffieHellman(object):
    """
    An implementation of the Diffie-Hellman protocol.
    This class uses the 6144-bit MODP Group (Group 17) from RFC 3526.
    This prime is sufficient to generate an AES 256 key when used with a 540+
    bit exponent.
    """

    prime = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA18217C32905E462E36CE3BE39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF6955817183995497CEA956AE515D2261898FA051015728E5A8AAAC42DAD33170D04507A33A85521ABDF1CBA64ECFB850458DBEF0A8AEA71575D060C7DB3970F85A6E1E4C7ABF5AE8CDB0933D71E8C94E04A25619DCEE3D2261AD2EE6BF12FFA06D98A0864D87602733EC86A64521F2B18177B200CBBE117577A615D6C770988C0BAD946E208E24FA074E5AB3143DB5BFCE0FD108E4B82D120A92108011A723C12A787E6D788719A10BDBA5B2699C327186AF4E23C1A946834B6150BDA2583E9CA2AD44CE8DBBBC2DB04DE8EF92E8EFC141FBECAA6287C59474E6BC05D99B2964FA090C3A2233BA186515BE7ED1F612970CEE2D7AFB81BDD762170481CD0069127D5B05AA993B4EA988D8FDDC186FFB7DC90A6C08F4DF435C93402849236C3FAB4D27C7026C1D4DCB2602646DEC9751E763DBA37BDF8FF9406AD9E530EE5DB382F413001AEB06A53ED9027D831179727B0865A8918DA3EDBEBCF9B14ED44CE6CBACED4BB1BDB7F1447E6CC254B332051512BD7AF426FB8F401378CD2BF5983CA01C64B92ECF032EA15D1721D03F482D7CE6E74FEF6D55E702F46980C82B5A84031900B1C9E59E7C97FBEC7E8F323A97A7E36CC88BE0F1D45B7FF585AC54BD407B22B4154AACC8F6D7EBF48E1D814CC5ED20F8037E0A79715EEF29BE32806A1D58BB7C5DA76F550AA3D8A1FBFF0EB19CCB1A313D55CDA56C9EC2EF29632387FE8D76E3C0468043E8F663F4860EE12BF2D5B0B7474D6E694F91E6DCC4024FFFFFFFFFFFFFFFF
    generator = 2

    def __init__(self):
        """
        Generate the public and private keys.
        """
        self.privateKey = self.genPrivateKey(576)
        self.publicKey = self.genPublicKey()

    def genPrivateKey(self, bits):
        """
        Generate a private key using a secure random number generator.
        """
        return secure_random(bits)

    def genPublicKey(self):
        """
        Generate a public key X with g**x % p.
        """
        return pow(self.generator, self.privateKey, self.prime)

    def checkPublicKey(self, otherKey):
        """
        Check the other party's public key to make sure it's valid.
        Since a safe prime is used, verify that the Legendre symbol is equal to
        one.
        """
        if 2 < otherKey < self.prime - 1:
            if pow(otherKey, (self.prime - 1)/2, self.prime) == 1:
                return True
        return False

    def genSecret(self, privateKey, otherKey):
        """
        Check to make sure the public key is valid, then combine it with the
        private key to generate a shared secret.
        """
        if self.checkPublicKey(otherKey) is True:
            sharedSecret = pow(otherKey, privateKey, self.prime)
            return sharedSecret
        else:
            raise Exception("Invalid public key.")

    def genKey(self, otherKey):
        """
        Derive the shared secret, then hash it to obtain the shared key.
        """
        self.sharedSecret = self.genSecret(self.privateKey, otherKey)
        s = hashlib.sha256()
        s.update(str(self.sharedSecret))
        self.key = s.digest()

    def getKey(self):
        """
        Return the shared secret key
        """
        return self.key

    def showParams(self):
        """
        Show the parameters of the Diffie Hellman agreement.
        """
        print "Parameters:"
        print
        print "Prime: ", self.prime
        print "Generator: ", self.generator
        print "Private key: ", self.privateKey
        print "Public key: ", self.publicKey
        print

    def showResults(self):
        """
        Show the results of a Diffie-Hellman exchange.
        """
        print "Results:"
        print
        print "Shared secret: ", self.sharedSecret
        print "Shared key: ", hexlify(self.key)
        print


