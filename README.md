# Todoable
A frontend and back end to save your todo lists

## Todoable UI
https://master.d1ivirx6vomsvr.amplifyapp.com/

##
I have deployed the UI for todoable app in AWS Amplify for continious integration.

##
The todoable backend is deployed on a lambda function and can be access by API Gateway.

## API Endpoint
https://xwyir2jma1.execute-api.us-east-1.amazonaws.com/prod

## Usage:
```
https://xwyir2jma1.execute-api.us-east-1.amazonaws.com/prod/todos?function=login&username=yourusername&password=yourpassword
```

# To run in your local
```
git clone https://github.com/vkd225/todoable.git
```

## UI
```
cd todo-ui
npm install
npm start
```

## Backend API
```
cd lambda
```

edit test_event.json with appropriate function name and values
```
python -r requirements.txt
python lambda_handler.py
```

## Running test cases
Edit `/tests/test_todowrapper.py` with appropriate test values.
You can also add more test cases if you want.
```
py.test
```

### Things for future.
1. Ofcourse, Better UI. :P
2. Handling Token better in the front end.
3. Better state management between components.