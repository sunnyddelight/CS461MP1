__author__ = 'Sunny'
from pymd5 import md5
h=md5(state='a18b85b3099848d6a57c91432d95af22'.decode("hex"), count=512)
h.update('&command3=DeleteAllFiles')
print h.hexdigest()