################################
###  Start of the test code  ###
################################

from acitoolkit import *

LOGIN = 'admin'
PASSWORD = 'ins3965!'
URL = 'http://172.23.102.91:80/'
DRYRUN = False

session = Session(URL, LOGIN, PASSWORD, DRYRUN)
session.login()

tenant = Tenant('michsmit2')
app = AppProfile('app1', tenant)
epg = EPG('epg1', app)
bd = BridgeDomain('bd1', tenant)
#sub1 = Subnet('s1', bd)
ctx = Context('ctx1', tenant)
bd.add_context(ctx)
if1 = Interface('eth', '1', '101', '1', '8', None)
if2 = Interface('eth', '1', '101', '1', '9', None)
if3 = Interface('eth', '1', '101', '1', '12', None)
#pc = PortChannel('pc1', None)
#pc.add_if(if1)
#pc.add_if(if2)
#pc.add_if(if3)
epg.add_to_interface(if1, L2IFAttachment('vlan', '5'))
epg.add_to_interface(if2, L2IFAttachment('vlan', '5'))
#epg.add_to_interface(pc, 'vlan', '5')

#print tenant.get_json()
#pc_data = pc.get_json()
#print pc.get_xml(pc.get_json())

url = 'api/mo/uni.json'
resp = session.post(url, data=json.dumps(tenant.get_json()))
print resp, resp.text

url1 = 'api/mo/uni/fabric.json'
url2 = 'api/mo/uni.json'

#(data1, data2) = pc.get_json()
#print 'url1:', url1
#print 'data1:', data1
#resp = session.post(url1, data=json.dumps(data1))
#print resp, resp.text
#print 'url2:', url2
#print 'data2:', data2
#resp = session.post(url2, data=json.dumps(data2))
#print resp, resp.text

#epg.add_to_interface(if1)
#contract = Contract('contract1', tenant)
#entry = FilterEntry('entry1', True, None, 80, 80,
#'ip', 'tcp', 1024, 65535, None, contract)

#print tenant.get_json()

