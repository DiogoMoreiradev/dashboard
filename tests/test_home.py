import time

def testar_home(browser):
	browser.get('http://127.0.0.1:8081')
	time.sleep(5)
	assert browser.title == "Dash"
	print("Página da home testada com sucesso!")
