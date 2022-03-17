from django.utils.timezone import timedelta

one_day = {'name': 'One Day',
           'req_abstynence_time': timedelta(days=1),
           'icon': None}

two_days = {'name': 'Two Days',
            'req_abstynence_time': timedelta(days=2),
            'icon': None}

three_days = {'name': 'Three Days',
              'req_abstynence_time': timedelta(days=3),
              'icon': None}

one_week = {'name': 'One Week',
            'req_abstynence_time': timedelta(weeks=1),
            'icon': None}

two_weeks = {'name': 'Two Weeks',
             'req_abstynence_time': timedelta(weeks=2),
             'icon': None}

three_weeks = {'name': 'Three Weeks',
               'req_abstynence_time': timedelta(weeks=3),
               'icon': None}

one_month = {'name': 'One Month',
             'req_abstynence_time': timedelta(weeks=4),
             'icon': None}

init_list = [one_day,
             two_days,
             three_days,
             one_week,
             two_weeks,
             three_weeks,
             one_month]
