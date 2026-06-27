from django.db import models

class Status(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Statuses"
        

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=150)

    type = models.ForeignKey(
        Type,
        on_delete=models.CASCADE,
        related_name="categories"
    )

    class Meta:
        unique_together = ("name", "type")
        ordering = ["name"]
        verbose_name_plural = "Categories"


    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=150)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="subcategories"
    )

    class Meta:
        unique_together = ("name", "category")
        ordering = ["name"]
        verbose_name_plural = "Subcategories"


    def __str__(self):
        return self.name

class Transaction(models.Model):
    created_at = models.DateField(auto_now_add=True)

    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT
    )

    type = models.ForeignKey(
        Type,
        on_delete=models.PROTECT
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT
    )

    subcategory = models.ForeignKey(
        SubCategory,
        on_delete=models.PROTECT
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    comment = models.TextField(
        blank=True
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.created_at} {self.amount}"