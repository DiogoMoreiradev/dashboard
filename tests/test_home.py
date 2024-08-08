import time

def testar_home(browser):
	url = 'http:127.0.0.1:8081'
	browser.get(url)
	time.sleep(10)
	assert browser.title == "Dash"
	print("Página da home testada com sucesso!")
