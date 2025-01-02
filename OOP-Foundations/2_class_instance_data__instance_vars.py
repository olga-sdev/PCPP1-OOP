'''
Python allows for variables to be used at the instance level or the class level:
Variables at the instance level -> instance variables.
During the object's initialization, performed by the __init__ method, or later at any moment of the object's life.
'''


class Application:
    def __init__(self, name):
        self.instance_var = name


app_messanger = Application('MS Teams')
app_calendar = Application('Calendly')


print(f'app_messanger intance varible is equal to: {app_messanger.instance_var}')
print(f'app_calendar intance varible is equal to: {app_calendar.instance_var}')


# create instance var out of __init__ method
app_calendar.another_var = 'Description. Calendly is the modern scheduling platform.'

print(app_messanger.__dict__)
print(app_calendar.__dict__)
