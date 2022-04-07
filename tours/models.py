from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Tour(models.Model):
    title = models.CharField("Название", max_length=100)
    image = models.ImageField("Фото", upload_to="tours/")
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    created = models.DateTimeField("Создано", auto_now_add=True)
    updated = models.DateTimeField("Обновлено", auto_now=True)
    is_active = models.BooleanField("Активный", default=False)

    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'
        ordering = ['-created']

    def __str__(self):
        return self.title


class RegularTour(models.Model):
    TOUR_STATUS_WAITING = 'waiting'
    TOUR_STATUS_START = 'start'
    TOUR_STATUS_COMPLETED = 'completed'
    TOUR_STATUS_REJECTED = 'rejected'
    TOUR_STATUSES = (
        (TOUR_STATUS_WAITING, "Идет набор"),
        (TOUR_STATUS_START, "Начался"),
        (TOUR_STATUS_COMPLETED, "Завершен"),
        (TOUR_STATUS_REJECTED, "Отменен")
    )

    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    start = models.DateTimeField("Начало")
    end = models.DateTimeField("Конец")
    places_count = models.PositiveSmallIntegerField("Количество мест")
    status = models.CharField("Статус", max_length=10, choices=TOUR_STATUSES, default=TOUR_STATUS_WAITING)

    class Meta:
        verbose_name = 'Регулярный тур'
        verbose_name_plural = 'Регулярные туры'
        ordering = ['-start']

    def __str__(self):
        return f'{self.tour.title} - {self.start}'


class TourBooking(models.Model):
    STATUS_NEW = "new"
    STATUS_CONFIRMED = "confirmed"
    STATUS_FINISHED = "finished"
    STATUS_REJECTED = "rejected"
    BOOKING_STATUS = (
        (STATUS_NEW, "Новый"),
        (STATUS_CONFIRMED, "Подтвержден"),
        (STATUS_FINISHED, "Завершен"),
        (STATUS_REJECTED, "Отменен")
    )

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    tour = models.ForeignKey(RegularTour, on_delete=models.DO_NOTHING)
    place_count = models.PositiveSmallIntegerField('Места')
    mobile = models.CharField('Номер телефона', max_length=10)
    status = models.CharField('Статус', max_length=11, choices=BOOKING_STATUS, default=STATUS_NEW)
    is_paid = models.BooleanField('Оплачено', null=False)
    notice = models.CharField('Дополнительная информация', max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'
        ordering = ['-created']

    def __str__(self):
        return f'Бронь №{self.id}'
