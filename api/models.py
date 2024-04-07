from django.db import models

class JobPosting(models.Model):
    FULL_TIME = 1
    PART_TIME = 2
    CONTRACT = 3
    INTERNSHIP = 4
    TEMPORARY = 5
    JOB_TYPE = (
        (FULL_TIME, 'Full Time'),
        (PART_TIME, 'Part Time'),
        (CONTRACT, 'Contract'),
        (TEMPORARY, 'Internship'),
        (TEMPORARY, 'Temporary'),
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    website = models.URLField()
    job_family = models.CharField(max_length=100)
    job_type = models.CharField(max_length=4, choices=JOB_TYPE, default=FULL_TIME)
    company = models.ForeignKey('users.UserProfile', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.job_family} - {self.location} - {self.job_type}"
