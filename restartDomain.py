def restart_domain():
	connect('weblogic','oracle123','t3://192.168.0.101:7001')	
	print 'connected'
	#connect('http://uiosoap01:20001/console/', 'AdminServer')	
	shutdown_managed_servers()
	shutdown_admin_server()	
	#startServer([adminServerName], [domainName], [url], [username], [password], [domainDir], [block], [timeout], [serverLog], [systemProperties], [jvmArgs] [spaceAsJvmArgsDelimiter])
	startServer('AdminServer','mega_domain','t3://192.168.0.101:7001',username='weblogic',password='oracle123',domainDir='/u01/Oracle/Middleware/Oracle_Home/user_projects/domains/mega_domain',block='true',timeout=240000)
	start_domain()
	

def shutdown_admin_server():
	print '**** Apagando AdminServer ****'	 	
	#shutdown([name], [entityType], [ignoreSessions], [timeOut], [force], [block])
	shutdown('AdminServer','Server', ignoreSessions='true',force='true',block='true')

	
def shutdown_managed_servers():
	print '**** Shutdown Servers ****'
	domainConfig() 
	serverList=cmo.getServers(); 
	domainRuntime()
	
	for server in serverList:		 
		name=server.getName()	 
		if name != 'AdminServer':
			cd('/ServerLifeCycleRuntimes/'+name)
			
			serverState=cmo.getState() 
			if serverState != 'SHUTDOWN':
				print '**** Apagando Servidores ****'	 
				print 'Servidor *****'+ name +'***** Estado ***** '+serverState			
				shutdown(name,'Server','true',force='true', block='true')
				print 'Servidor *****'+ name +'***** Estado Actual ***** '+serverState
		
def start_domain(): 
	connect('weblogic','oracle123','t3://192.168.0.101:7001')	
	print 'connectado'
	domainConfig() 
	serverList=cmo.getServers(); 
	domainRuntime() 
		
	for server in serverList:	 
		name=server.getName()	 
		cd('/ServerLifeCycleRuntimes/'+name)	 
		serverState=cmo.getState() 
		if serverState=='SHUTDOWN' and name != 'OSB_server01' and name != 'SOA_Server1': 
			print '**** Iniciando Servidores ****'	 
			print 'Servidor *****'+ name +'***** Estado ***** '+serverState
			start(name,'Server',block='true')		 
			print 'Servidor *****'+ name +'***** Estado Actual***** '+serverState	
	disconnect()
			

# ================================================================

#           Main

# ================================================================

if __name__== "main":

        print 'Reiniciar Dominio';
        restart_domain()
		#shutdown_domain()
		#start_domain()
		
			
