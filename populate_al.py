import os
import sys
import store
import coordinators_list
import ac_list


def populate_users():

    # Admin 
    os.system("python manage.py syncdb --noinput")
    os.system("python manage.py createsuperuser --username=admin --email=admin@example.com")

    for u in coordinators_list.users:
        # Normal users
        print "Adding user: %s" % u['USERNAME']
        u['USERNAME'] = add_user(u['USERNAME'],
                                 u['FIRSTNAME'],
                                 u['LASTNAME'],
                                 u['EMAIL'],
                                 u['PASSWORD'],)
        
        add_coordinator(user=u['USERNAME'],
                        contact=u['CONTACT'],
                        picture=u['PHOTO'])

    user_list = User.objects.all()
    if user_list:
        print "Following user(s) created successfully."
        for i in user_list:
            print i.username

def populate_ac():

    for ac in ac_list.acs:
        print "Adding AC: %s has coordinator: %s" % (ac['NAME'], ac['COORDINATOR'])
        add_ac(
            ac_id=ac['RC_ID'],
            name=ac['NAME'],
            coordinator=User.objects.get(username=ac['COORDINATOR']),
            city=ac['CITY'],
            state=ac['STATE'],
            status=True)


def add_user(username, first_name, last_name, email, password):
    u = User.objects.create_user(username=username, first_name=first_name,
                                 last_name=last_name,
                                 email=email, password=password)
    return u


def add_coordinator(user, contact, picture):
    up = Coordinator(user=user, contact=contact, picture=picture)
    up.save()

def add_ac(ac_id, name, city, state, coordinator, status):
    ac = AakashCenter(ac_id=ac_id, name=name, city=city,
                      state=state, coordinator=coordinator,
                      status=status)
    ac.save()
    
# start execution here!
if __name__ == '__main__':
    print "Starting Aakashlabs population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aakashlabs.settings')
    from ac.models import AakashCenter, Coordinator
    from django.contrib.auth.models import User

    if os.path.exists('ac.db'):
        os.system("rm ac.db")

    populate_users()
    populate_ac()
