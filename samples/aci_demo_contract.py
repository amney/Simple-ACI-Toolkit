from acitoolkit import *
from credentials import *
""" Create 2 EPGs within the same Context and have
    1 EPG provide a contract to the other EPG.
"""
# Create the Tenant
tenant = Tenant('aci-toolkit-demo')

# Create the Application Profile
app = AppProfile('my-demo-app', tenant)

# Create the EPGs
web_epg = EPG('web-frontend', app)
db_epg = EPG('database-backend', app)

# Create a Context and BridgeDomain
# Place both EPGs in the Context and in the same BD
context = Context('VRF-1', tenant)
bd = BridgeDomain('BD-1', tenant)
bd.add_context(context)
web_epg.add_bd(bd)
db_epg.add_bd(bd)

# Define a contract with a single entry
contract = Contract('mysql-contract', tenant)
entry1 = FilterEntry('entry1',
                     applyToFrag='no',
                     arpOpc='unspecified',
                     dFromPort='3306',
                     dToPort='3306',
                     etherT='ip',
                     prot='tcp',
                     sFromPort='1',
                     sToPort='65535',
                     tcpRules='unspecified',
                     parent=contract)

# Provide the contract from 1 EPG and consume from the other
db_epg.provide(contract)
web_epg.consume(contract)

# Login to APIC and push the config
session = Session(URL, LOGIN, PASSWORD)
session.login()
resp = session.push_to_apic(tenant.get_url(), data=tenant.get_json())
if resp.ok:
    print 'Success'

# Print what was sent 
print 'Pushed the following JSON to the APIC'
print 'URL:', tenant.get_url()
print 'JSON:', tenant.get_json()

# Cleanup (uncomment the next 2 lines to delete the config)
#tenant.mark_as_deleted()
#resp = session.push_to_apic(tenant.get_url(), data=tenant.get_json())
