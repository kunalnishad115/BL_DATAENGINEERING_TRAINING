import pandas as pd

data = {
    'student_id': [
        101,101,101,
        102,102,102,
        103,103,103,
        104,104,104
    ],

    'subject': [
        'Math','Science','English',
        'Math','Science','English',
        'Math','Science','English',
        'Math','Science','English'
    ],

    'marks': [
        80,35,90,
        20,25,60,
        70,75,30,
        40,15,20
    ],

    'exam_date': [
        '2026-05-01',
        '2026-05-01',
        '2026-05-01',
        '2026-05-01',
        '2026-05-01',
        '2026-05-01',
        '2026-05-01',
        '2026-05-01',
        '2026-05-01',
        '2026-05-01',
        '2026-05-01',
        '2026-05-01'
    ]
}

df = pd.DataFrame(data)

print(df)


# Convert exam_date into datetime


df['exam_date'] = pd.to_datetime(df['exam_date'])


# Pass/Fail Column
# Assume passing marks = 40


df['result'] = df['marks'] >= 40

print("\nPass/Fail Status:\n")
print(df)


# Subject-wise Pass Percentage


pass_percentage = df.groupby(
    'subject'
)['result'].mean() * 100

print("\nSubject-wise Pass Percentage:\n")
print(pass_percentage)


# Students failing in more than one subject


# Count failures
failures = df[df['marks'] < 40]

fail_count = failures.groupby(
    'student_id'
)['subject'].count()

# More than one failure
multiple_failures = fail_count[
    fail_count > 1
]

print("\nStudents Failing in More Than One Subject:\n")
print(multiple_failures)


# Performance Summary Report


summary = df.groupby(
    'student_id'
).agg({

    'marks':['mean','max','min'],
    'subject':'count'

})

print("\nPerformance Summary Report:\n")
print(summary)