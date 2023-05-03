from django.db import models

# class Skill(models.Model):
#     name = models.CharField(max_length=120)

class Position(models.Model):
    job_title = models.CharField(max_length=120)
    yoe = models.IntegerField()
    skills = models.TextField(null=True)

class Description(models.Model):
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name="descriptions")
    text = models.TextField()


class Resume(models.Model):
    text = models.TextField()
    summary = models.TextField()


resume_sample = """Yan Yukhnovets
Java Developer
As a Java developer with over 5 years of experience in software
development, I have a solid understanding of Java and related
technologies, and have experience in both microservices and
monolith applications. I have worked in both small and large
teams, from 3 to 25 members, and have developed skills in
collaborating effectively with cross-functional teams on time.
Experience
Mar 2022 -
Jan 2023
Nov 2020 -
Mar 2022
Nov 2019 -
Oct 2020
Aug 2017 -
Nov 2019
TelQ SMS testing
Java developer / Serbia, remote
Participated in the conversion of an SMS
routing service from PHP to Java,
including debugging for Android
compatibility.
Participated in the development of an
analytical service from scratch, including
creating ETL jobs in Redshift
Tochka Bank Digital bank for business
Java developer / Russia, remote
●
Revived a dormant project, resulting in a
more user-friendly experience for clients.
Designed and developed new service that
simplified internal bank communication by
replacing an outdated system.
• Implemented a notification service for
clients, resulting in a decrease in client
inquiries regarding employee verification
status.
Wellink Company Consulting company
Java developer / Russia, remote
Contributed to the development of a
backend system for issuing consumer
loans at a large bank
Developed an MVP of a system for
personal lawyer consultation from the
ground up
Zaycev.net Music streaming service
Java/Scala developer / Russia, Chelyabinsk
Assisted in the design and development of
a GeolP-based content system for
streaming and downloading music.
Led the effort to update major versions of
key frameworks in a monolith system and
refactored nearly 400 integration tests,
resulting in a significant reduction in testing
time and an increase in development
speed.
Personal Info
Phone
+381-629-377-469
E-mail
yukhnovets.yan@gmail.com
Linkedin
linkedin.com/in/yan-yukhnovets
Skills
●
●
Java, Kotlin, Scala
MySQL, PostgreSQL,
MongoDB, Oracle
Spring (Boot, Cloud, Core,
WebFlux), Hibernate, Netty
RabbitMQ, Kafka, ActiveMQ
Grafana, Zabbix
• Docker, Kubernetes, Jenkins,
Teamcity, Gitlab, Maven,
Gradle, AWS
Education
South Ural State University
2014 - 2020
Master of Computer Science"""
