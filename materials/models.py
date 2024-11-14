from django.db import models


class Course(models.Model):
    name = models.CharField(
        verbose_name="Name", help_text="Name of the course", max_length=50
    )
    preview = models.ImageField(
        verbose_name="Picture", upload_to="materials/pictures", blank=True, null=True
    )
    description = models.TextField(
        verbose_name="Description",
        help_text="Describe the course",
        max_length=500,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(
        verbose_name="Name", help_text="Name of the lesson", max_length=50
    )
    preview = models.ImageField(
        verbose_name="Picture", upload_to="materials/pictures", blank=True, null=True
    )
    description = models.TextField(
        verbose_name="Description",
        help_text="Describe the lesson",
        blank=True,
        null=True,
    )
    video = models.TextField(
        verbose_name="Video URL", help_text="Add the link to the video"
    )
    course = models.ForeignKey(
        "Course", on_delete=models.CASCADE, verbose_name="Course"
    )

    class Meta:
        verbose_name = "Lesson"
        verbose_name_plural = "Lessons"

    def __str__(self):
        return self.name
