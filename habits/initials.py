from django.utils.timezone import timedelta

one_day = {'name': 'One Day',
           'req_abstynence_time': timedelta(days=1),
           'icon': None,
           'is_active': True}

two_days = {'name': 'Two Days',
            'req_abstynence_time': timedelta(days=2),
            'icon': None,
            'is_active': False}

three_days = {'name': 'Three Days',
              'req_abstynence_time': timedelta(days=3),
              'icon': None,
              'is_active': False}

one_week = {'name': 'One Week',
            'req_abstynence_time': timedelta(weeks=1),
            'icon': None,
            'is_active': False}

two_weeks = {'name': 'Two Weeks',
             'req_abstynence_time': timedelta(weeks=2),
             'icon': None,
             'is_active': False}

three_weeks = {'name': 'Three Weeks',
               'req_abstynence_time': timedelta(weeks=3),
               'icon': None,
               'is_active': False}

one_month = {'name': 'One Month',
             'req_abstynence_time': timedelta(weeks=4),
             'icon': None,
             'is_active': False}

init_list = [one_day,
             two_days,
             three_days,
             one_week,
             two_weeks,
             three_weeks,
             one_month]
