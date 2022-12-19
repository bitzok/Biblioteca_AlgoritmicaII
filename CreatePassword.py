class create_password:
    def __init__(self, password):
        self.password = password

    def validate(self):        
        vals = {
        'La contraseña debe contener una letra mayuscula.': lambda s: any(x.isupper() for x in s),
        'La contraseña debe contener una letra minuscula.': lambda s: any(x.islower() for x in s),
        'La contraseña debe contener un digito.': lambda s: any(x.isdigit() for x in s),
        'La contraseña debe contener al menos 3 caracteres.': lambda s: len(s) >= 3,
        'La contraseña no debe contener espacios.': lambda s: not any(x.isspace() for x in s)            
        } 
        valid = True  
        for n, val in vals.items():                         
           if not val(self.password):                   
               valid = False
               return n
        return valid                

    def compare(self, password2):
        if self.password == password2:
            return True