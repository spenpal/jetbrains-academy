# IMPORTS #
from collections import namedtuple

# Constants
DEPARTMENTS = ['Biotech', 'Chemistry', 'Engineering', 'Mathematics', 'Physics']
Applicant = namedtuple('Applicant',
                       ['name', 'physics', 'chemistry', 'math', 'computer_science', 'special', 'dept1', 'dept2',
                        'dept3'])
DEPT_EXAMS = {
    'Physics': ('physics', 'math'),
    'Chemistry': ('chemistry',),
    'Mathematics': ('math',),
    'Engineering': ('computer_science', 'math'),
    'Biotech': ('chemistry', 'physics')
}


# FUNCTIONS #
def parse_application(data):
    name = ' '.join([data[0], data[1]])
    grades = [float(grade) for grade in data[2:-3]]
    depts = data[-3:]
    return name, *grades, *depts


def parse_applications():
    applications = set()
    with open('applicants.txt') as f:
        for line in f:
            line = line.strip()
            applicant_data = parse_application(line.split())
            applicant = Applicant(*applicant_data)
            applications.add(applicant)
    return applications


def remove_applicants(general, apps):
    for app in apps:
        general.remove(app)


def get_mean_score(applicant, dept):
    return sum(getattr(applicant, exam) for exam in DEPT_EXAMS[dept]) / len(DEPT_EXAMS[dept])


def review_applications(applications):
    accepted_applicants = {dept: [] for dept in DEPARTMENTS}

    for dept_num in ['dept1', 'dept2', 'dept3']:
        for dept in DEPARTMENTS:
            if len(accepted_applicants[dept]) >= max_dept_students:
                continue

            dept_applicants = [applicant for applicant in applications if getattr(applicant, dept_num) == dept]
            dept_applicants.sort(key=lambda app: (-max(get_mean_score(app, dept), app.special), app.name))

            top_applicants = dept_applicants[:max_dept_students - len(accepted_applicants[dept])]
            accepted_applicants[dept].extend(top_applicants)

            remove_applicants(applications, top_applicants)

    for dept in accepted_applicants:
        accepted_applicants[dept].sort(key=lambda app: (-max(get_mean_score(app, dept), app.special), app.name))

    return accepted_applicants


def log_accepted_applicants(accepted_applicants):
    for dept in DEPARTMENTS:
        with open(f'{dept.lower()}.txt', 'w') as f:
            output = [f'{applicant.name} {max(get_mean_score(applicant, dept), applicant.special)}' for applicant in
                      accepted_applicants[dept]]
            f.write('\n'.join(output))


# MAIN #
max_dept_students = int(input())

applications = parse_applications()
accepted_applicants = review_applications(applications)
log_accepted_applicants(accepted_applicants)
