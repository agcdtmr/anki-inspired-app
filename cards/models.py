from django.db import models

# Create your models here.

NUM_BOXES = 5
BOXES = range(1, NUM_BOXES + 1)


class Card(models.Model):
    question = models.CharField(max_length=1000)
    answer = models.CharField(max_length=1000)

    # choices make sure that models.IntegerField must contain
    #  that is within the BOXES range
    box = models.IntegerField(
        choices=zip(BOXES, BOXES),
        default=BOXES[0],
    )

    # automatically timestamp the creation
    # and control which is the newest to oldest card
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.question

    def move(self, solved):

        # move a card to the next box if you recall its answer.
        new_box = self.box + 1 if solved else BOXES[0]

        if new_box in BOXES:
            self.box = new_box
            self.save()

        return self

