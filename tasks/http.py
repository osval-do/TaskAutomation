import requests, json
from models.task import Task
from models.program import Program

class Login(Task):
    url: str
    user: str
    passw: str
    tprop: str
    bearer_var = 'jwt_bearer'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'DjangoLogin'
        self.url = kwargs.get('url')
        self.user = kwargs.get('user')
        self.passw = kwargs.get('pass')
        self.tprop = kwargs.get('token_prop')

    def execute(self, program: Program):
        data = {
            'username': self.parseVar(self.user),
            'password': self.parseVar(self.passw)
        }
        url = self.parseVar(self.url)
        self.info('login',url)
        try:
            response_login = requests.post(url, json=data).json()
        except Exception as e:
            #print(response_login)
            self.err(e)
            return -1
        if self.tprop in response_login:
            program.context[self.bearer_var]=response_login[self.tprop]
            # print(program.context[self.bearer_var])
            return 1
        self.err('JWT token no se encontró en resultado de autenticación')
        return -1


class Http(Task):
    action = 'post'
    url: str
    bearer_var = 'jwt_bearer'
    fields: dict
    files: dict
    timeout = None
    result_var = 'http_result'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.action = kwargs.get('action', self.action)
        self.url = kwargs.get('url')
        self.bearer_var = kwargs.get('bearer_var', self.bearer_var)
        self.result_var = kwargs.get('result_var', self.result_var)
        self.fields = kwargs.get('fields', {})
        self.files = kwargs.get('files', {})

    def execute(self, program: Program) -> int:
        values = {}
        for name in self.fields:
            values[name] = self.parseVar(self.fields[name])
        json=None
        for file in self.files:
            file_path = self.parseVar(self.files[file])
            self.files[file] = open(file_path,'rb')
        hed = {}
        # if self.action == 'post': hed['Content-Type'] = 'multipart/form-data'
        if self.bearer_var in program.context:
            hed['Authorization'] = 'Bearer ' + program.context[self.bearer_var]
        url = self.parseVar(self.url)
        action = self.parseVar(self.action)
        self.info(action,url)
        try:
            result = requests.request(
                action,
                url,
                data=values,
                json=json,
                files=self.files,
                headers=hed,
                timeout=self.timeout)
            if result.status_code != 200:
                self.err('Acción HTTP',self.action,'failed with code',str(result.status_code))
                print(result.content)
                return -1
            print(result)
            program.context[self.result_var]=result
            return 1
        except Exception as e:
            self.err(e)
            return -1