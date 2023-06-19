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

two_months = {'name': 'Two Months',
              'req_abstynence_time': timedelta(weeks=8),
              'icon': None,
              'is_active': False}

three_months = {'name': 'Three Months',
                'req_abstynence_time': timedelta(weeks=12),
                'icon': None,
                'is_active': False}

six_months = {'name': 'Six Months',
              'req_abstynence_time': timedelta(weeks=24),
              'icon': None,
              'is_active': False}

one_year = {'name': 'One Year',
            'req_abstynence_time': timedelta(weeks=52),
            'icon': None,
            'is_active': False}

two_years = {'name': 'Two Years',
             'req_abstynence_time': timedelta(weeks=104),
             'icon': None,
             'is_active': False}

five_years = {'name': 'Five Years',
              'req_abstynence_time': timedelta(weeks=260),
              'icon': None,
              'is_active': False}

init_list = [one_day,
             two_days,
             three_days,
             one_week,
             two_weeks,
             three_weeks,
             one_month,
             two_months,
             three_months,
             six_months,
             one_year,
             two_years,
             five_years]
