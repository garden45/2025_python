class User:
    def __init__(self, username, email):
        self.username=username
        self.email=email

    def __eq__(self, other):
        return self.email==other.email
    
u1=User("Jane", "jane@korea.korea")
u2=User("jennnie", "jane@korea.korea")

if u1==u2:
    print("중복된 이메일 입니다.")