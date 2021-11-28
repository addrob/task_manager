import sqlite3
import sys


conn = sqlite3.connect('tm.db')
cursor = conn.cursor()

# TODO добавить коммиты

def create_item(table, values):
    cursor.execute(f'insert into {table} values {values}')
    ## нерабочий код! проверить как передавать values чтобы был в скобочках как в команде

## этот метод обращается по айдишнику как <<таблица_айди>>,
# поэтому с таблицами где id сделан не так этот метод работать не будет!!!
#TODO переосмыслить и убрать коммент выше, но добавить информацию в доку на твой проект
def edit_table_item(table, item_id, field, value):
    cursor.execute(f'update {table} set {field} = {value} where {table}_id={item_id}')

#TODO сделать метод удаления айтема какой-то таблицы по какому-то айдишнику
def delete_table_item():
    pass

def create_table(table_name):
    cursor.execute(f'create table {table_name} ({table_name}_id integer not null unique, '
                   f'primary key("{table_name}_id" autoincrement) )')

##TODO сделать метод добавления столбцов в таблицу
def alter_table_add_columns():
    pass

class DbObject:
    def __init__(self, table_name):
        self.table = table_name
        self.prefix = table_name.lower()


class Project(DbObject):
    def __init__(self):
        super().__init__('Project')
        last_object_id = cursor.execute(f'SELECT MAX (project_id) FROM {self.table}').fetchone()
        self.id = last_object_id[0] + 1 ## не нужно +1, потому что мы берём id только последней записи, чтобы именно её изменять

    def create_newproject(self, name):
        create_item(self.table, name)

    def create(self):
        name = input('name ')
        description = input('description')
        start = input('start')
        deadline = input('deadline')
        parent_id = input('parent_id')
        favourite = input('favourite')
        archive = input('archive')
        priority = input('priority')
        ready_check = input('ready_check')
        cursor.execute(f'INSERT INTO {self.table} ({self.prefix}name, {self.prefix}description, {self.prefix}start,'
                       f'{self.prefix}deadline, {self.prefix}parent, {self.prefix}favourite, {self.prefix}archive,'
                       f'{self.prefix}priority, {self.prefix}ready)  '
                       f'VALUES (\'{name}\', \'{description}\', {start},{deadline},{parent_id},'
                       f'{favourite},{archive},{priority},{ready_check})')
        conn.commit()

#TODO сделать норм
    def edit(self):
        edit_target = input('edit what?')
        edit_value = input('content?')
        cursor.execute(f'UPDATE {self.table} SET {edit_target} = \'{edit_value}\''
                       f' WHERE {self.table}_id = {self.id} ')
        conn.commit()

    def remove(self, element_id):
        cursor.execute(f'DELETE FROM {self.table} WHERE {self.prefix}id = {element_id} ')

    def archive(self):
        pass

class Task(DbObject):
    def __init__(self):
        super().__init__('Task')

class SubTask(DbObject):
    def __init__(self):
        super().__init__('Subtask')


class Notification:
    pass


if __name__ == '__main__':

    user_query = ''

    while user_query != 'stop':

        if len(user_query)==0:
            user_query = input('Your query?:')
        if user_query=='создать таблицу':
            ask_for_table_name = input('название?: ')
            create_table(ask_for_table_name)
        elif user_query=='создать проект':
            ask_for_project_name=input('название?: ')
            new_project=Project()
            new_project.create_newproject(ask_for_project_name)


# aboba = Project()
# aboba.create()
# aboba.edit()

#task = Task()
#task.create()
#task.edit()