from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_colony.db")
    app.run()


if __name__ == '__main__':
    main()
    captain = User()
    captain.surname = "Scott"
    captain.name = "Ridley"
    captain.age = 21
    captain.position = "captain"
    captain.speciality = "research engineer"
    captain.address = "module_1"
    captain.email = "scott_chief@mars.org"
    user1 = User()
    user1.surname = "Donaldson"
    user1.name = "Jimmy"
    user1.age = 24
    user1.position = "PR manager"
    user1.speciality = "no spec"
    user1.address = "module_1"
    user1.email = "mrbeast@mars.org"
    user2 = User()
    user2.surname = "Perry"
    user2.name = "Nicholas"
    user2.age = 30
    user2.position = "cook"
    user2.speciality = "performance arts"
    user2.address = "module_1"
    user2.email = "nikocado@mars.org"
    user3 = User()
    user3.surname = "McNutt"
    user3.name = "Ronnie"
    user3.age = 33
    user3.position = "guard"
    user3.speciality = "no spec"
    user3.address = "module_1"
    user3.email = "ronnut@mars.org"
    job1 = Jobs()
    job1.team_leader = 1
    job1.job = "deployment of residential modules 1 and 2"
    job1.work_size = 15
    job1.collaborators = "2, 3"
    job1.is_finished = False
    db_sess = db_session.create_session()
    db_sess.add(captain)
    db_sess.add(user1)
    db_sess.add(user2)
    db_sess.add(user3)
    db_sess.add(job1)
    db_sess.commit()