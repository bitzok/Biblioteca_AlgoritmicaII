class create_user:
    def __init__(self, user):
        self.user = user

    def validate_user(self):        
        vals = {
        'El usuario debe contener un digito.': lambda s: any(x.isdigit() for x in s),
        'El usuario debe contener al menos 3 caracteres.': lambda s: len(s) >= 3,
        'El usuario no debe contener espacios.': lambda s: not any(x.isspace() for x in s)            
        } 
        valid = True  
        for n, val in vals.items():                         
           if not val(self.user):                   
               valid = False
               return n
        return valid 