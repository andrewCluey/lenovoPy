from xcapy.data import xclarity

#discovery = xc.xca_discoverdev(api_user,api_pass,api_url,'192.168.10.224')
#print(discovery)

cred = xclarity.xca_storedcred(api_user,api_pass,api_url)
print(cred)
