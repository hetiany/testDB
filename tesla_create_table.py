import sqlite3

conn = sqlite3.connect('tesla.db')

c = conn.cursor()

# query_create_plays = '''
# create table if not exists plays (
# id int,
# tile varchar(40) not null,
# writer varchar(40) not null);
# '''
#
# query_create_reservations = '''
# create table if not exists reservations (
# id int not null,
# play_id int not null,
# number_of_tickets int not null,
# theater varchar(40) not null,
# unique(id));
# '''

query_create_script = '''
create table if not exists plays (
id int not null,
tile varchar(40) not null,
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

# c.execute(query_create_plays)
# c.execute(query_create_reservations)

conn.commit()
conn.close()

if __name__ == '__main__':
    pass
