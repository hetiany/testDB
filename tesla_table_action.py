import sqlite3


class DBHandle:
    def __init__(self):
        pass

    def init_db(self):
        conn = sqlite3.connect('tesla.db')
        c = conn.cursor()
        query_create_script = '''
        create table if not exists plays (
        id int not null,
        title varchar(40) not null,
        writer varchar(40) not null,
        unique(id));

        insert into plays values (109, 'Queens', 'Paul');
        insert into plays values (123, 'Merlin', 'Lee');
        insert into plays values (142, 'Key', 'Max');
        insert into plays values (144, 'ROMEance', 'Bohring');
        insert into plays values (145, 'Nameless', 'Note');

        create table if not exists reservations (
        id int not null,
        play_id int not null,
        number_of_tickets int not null,
        theater varchar(40) not null,
        unique(id));

        insert into reservations values (13, 109, 12, 'Mc');
        insert into reservations values (24, 109, 34, 'Mc');
        insert into reservations values (37, 145, 84, 'Mc');
        insert into reservations values (49, 145, 45, 'Mc');
        insert into reservations values (51, 145, 41, 'Mc');
        insert into reservations values (68, 123, 3, 'Mc');
        insert into reservations values (83, 142, 46, 'Mc');
        '''
        c.executescript(query_create_script)
        conn.commit()
        conn.close()

    def do_get_result(self):
        conn = sqlite3.connect('tesla.db')
        c = conn.cursor()
        query_create_script = '''
        select play_id, title, sum(number_of_tickets) as reserved_tickets 
        from plays left outer join reservations on plays.id = reservations.play_id 
        group by play_id 
        order by reserved_tickets DESC;
        '''
        resp = c.execute(query_create_script)
        # return resp
        raw_rt = resp.fetchall()
        # raw_rt = resp.fetchone()
        conn.close()
        if raw_rt:
            return raw_rt
        else:
            return None


if __name__ == '__main__':
    dbhandle = DBHandle()
    # dbhandle.init_db()
    res = dbhandle.do_get_result()
    print(res)
    for i in range(0,len(res)):
        print(res[i])


