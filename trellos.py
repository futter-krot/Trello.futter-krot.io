import requests, sys
auth_params = {    
    'key': "7693692e0ccb908d324012f786735925",    
    'token': "c5593eff41ef41eb5fc03e0d6717f89b69c135638900821270b6d7d5e2cea8f3", 
    }  
base_url = "https://api.trello.com/1/{}"  
board_id = "qa34eJh1"
def read():
	column_data = requests.get(base_url.format('boards') + '/' + board_id + '/lists', params=auth_params).json()
	for column in column_data:
		print(column['name'])
		task_data = requests.get(base_url.format('lists') + '/' + column['id'] + '/cards', params=auth_params).json()
		if not task_data:
			print('\t' + 'Нет задач!')
			continue
		for task in task_data:
			print('\t' + task['name'])
def create(name, column_name):
	column_data = requests.get(base_url.format('boards') + '/' + board_id + '/lists', params=auth_params).json()
	for column in column_data:
		if column['name'] == column_name:
			requests.post(base_url.format("cards"), data={'name': name, 'idList': column['id'], **auth_params})
			break
def move(name, column_name):
	column_data = requests.get(base_url.format('boards') + '/' + board_id + '/lists', params=auth_params).json()
	task_id = None
	for column in column_data:
		column_tasks = requests.get(base_url.format('lists') + '/' + column['id'] + '/cards', params=auth_params).json()
		for task in column_tasks:
			if task['name'] == name:
				task_id = task['id']
				break
		if task_id:
			break
	for column in column_data:
		if column['name'] == column_name:
			requests.put(base_url.format('cards') + '/' + task_id + '/idList', data={'value': column['id'], **auth_params})
			break
if __name__ == "__main__":
	if len(sys.argv) <= 2:
		read()
	elif sys.argv[1] == 'create':
		create(sys.argv[2], sys.argv[3])
	elif sys.argv[1] == 'move':
		move(sys.argv[2], sys.argv[3]) 